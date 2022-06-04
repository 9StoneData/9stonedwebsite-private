from django.db import models
from companies.models import Company
# Create your models here.
class Dispensary(models.Model):
    # id                          =   models.AutoField(primary_key=True)
    Market_Focus                =   models.CharField(max_length=2)
    Pull_Date                   =   models.DateTimeField()
    Dispenary_base_leaf_url     =   models.CharField(primary_key=True,max_length=400)
    Dispensary_name             =   models.TextField()
    Name_Tag                    =   models.CharField(max_length=100)
    Member_Since                =   models.DecimalField(max_digits=10,decimal_places=6)
    License                     =   models.CharField(max_length=100)
    COMPANY                     =   models.ForeignKey(Company,on_delete=models.CASCADE)

class Dispensary_Time(models.Model):
    Dispensary_name         =   models.TextField()
    total_products          =   models.FloatField()
    Dispenary_base_leaf_url =   models.ForeignKey(Dispensary,on_delete=models.CASCADE)
    Last_update             =   models.CharField(max_length=30)
    Total_Followers         =   models.FloatField()
    Leafly_review_count     =   models.FloatField()
    ggl_score               =   models.FloatField()
    ggl_number_of_reviews   =   models.FloatField()
    time                    =   models.DateTimeField(primary_key=True)