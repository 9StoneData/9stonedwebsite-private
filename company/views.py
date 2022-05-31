from django.shortcuts import render
from .models import Company
import pandas as pd

# Create your views here.
def companies(request):
    qs=Company.objects.filter(State="AZ")
    df=pd.DataFrame.from_records(qs.values())
    print(df.shape)
    df['Center_Coord']=list(zip(df.lat,df.lon))
    context = {
        "object": df['Center_Coord']
    }
    print("DF ready to pass")
    return render(request, "company/companies.html", context=context)