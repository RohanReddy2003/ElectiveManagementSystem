from django.shortcuts import render
import pandas as pd
from .models import StudentInfo,ElectivesInfo
import secrets
import string
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Create your views here.

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# Function to send login email
def send_login_email(student_email, username, password):
    subject = 'Your Elective Registration Login Credentials'
    message = f'Your username: {username}\nYour password: {password}'
    from_email = 'gmrit.edu.in'
    recipient_list = [student_email]
    send_mail(subject, message, from_email, recipient_list)

def index(request):
    if request.method=='POST':
        if request.method=='POST':
            student_data=pd.read_csv(request.FILES.get('s_data'))
            elective_data=pd.read_csv(request.FILES.get('e_data'))
            
            # Loop through student data, generate passwords, and send emails
            for index, student in student_data.iterrows():
                email = student['email']
                password = generate_random_password()

                # Create a User and set the password using Django's make_password
                user = User.objects.create(username=email, email=email, password=make_password(password))

                # Send login email to the student
                send_login_email(email, email, password)

            # add data to database
            student_column_mapping = {
                's_id': 's_id',
                'name': 'name',
                'jntu_no':'jntu_no',
                'department':'department',
                'section':'section',
                'email':'email',
                'curr_sem':'curr_sem',
            }

            elective_column_mapping = {
                'course_code': 'course_code',
                'elective_name': 'elective_name',
                'offering_department':'offering_department',
                'offering_strength':'offering_strength',
                'not_allowed_students':'not_allowed_students',
            }

            # Rename columns in the DataFrame
            student_data.rename(columns=student_column_mapping, inplace=True)
            elective_data.rename(columns=elective_column_mapping, inplace=True)

            # Convert DataFrame to a list of dictionaries
            student_data_dict = student_data.to_dict(orient='records')
            elective_data_dict = elective_data.to_dict(orient='records')

            # Bulk insert data into the DummyTable model
            StudentInfo.objects.bulk_create([StudentInfo(**entry) for entry in student_data_dict])
            ElectivesInfo.objects.bulk_create([StudentInfo(**entry) for entry in elective_data_dict])
    return render(request,'admin_portal/index.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        
    return render(request,'admin_portal/login.html')