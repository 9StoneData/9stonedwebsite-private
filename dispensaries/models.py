from django.db import models
from companies.models import Company
# Create your models here.
class Dispensary(models.Model):
    id                          =   models.AutoField(primary_key=True)
    Market_Focus                =   models.CharField(max_length=2)
    Pull_Date                   =   models.DateTimeField()
    Dispenary_base_leaf_url     =   models.CharField(max_length=400)
    Dispensary                  =   models.TextField()
    Name_Tag                    =   models.CharField(max_length=100)
    Member_Since                =   models.DecimalField(max_digits=10,decimal_places=6)
    License                     =   models.CharField(max_length=100)
    COMPANY                     =   models.ForeignKey(Company,on_delete=models.CASCADE)