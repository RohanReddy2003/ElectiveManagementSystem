from django.shortcuts import render
import pandas as pd
from .models import DummyTable

# Create your views here.

def index(request):
    if request.method=='POST':
        data=pd.read_csv(request.FILES.get('myfile'))
        # add data to database
        data_dict = data.to_dict(orient='records')
        DummyTable.objects.bulk_create([DummyTable(**entry) for entry in data_dict])
    return render(request,'admin_portal/index.html')