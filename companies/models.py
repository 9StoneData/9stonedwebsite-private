from django.db import models
from geos.models import State,Zip

# Create your models here.
class Company(models.Model):
    COMPANY                         = models.TextField(primary_key=True, unique=True)
    TYPE                            = models.CharField(max_length=20, default="tbd")
    Pull_Date                       = models.DateTimeField(auto_now=False)
    google_map                      = models.CharField(max_length=400, default="tbd")
    Street                          = models.CharField(max_length=100, default="tbd")
    Town                            = models.CharField(max_length=100, default="tbd")
    zip_code                        = models.ForeignKey(Zip,null=True, blank=True,on_delete=models.CASCADE)
    State                           = models.ForeignKey(State,null=True, blank=True,on_delete=models.CASCADE)
    Email                           = models.CharField(max_length=100, default="tbd")
    Phone                           = models.CharField(max_length=100, default="tbd")
    Website                         = models.CharField(max_length=200, default="tbd")
    ACTIVE_on_LEAFLY                = models.CharField(max_length=10, default="tbd")
    Best_Google_Map_Url             = models.CharField(max_length=400, default="tbd")
    lat                             = models.DecimalField(max_digits=10,decimal_places=6, default=1)
    lon                             = models.DecimalField(max_digits=10,decimal_places=6, default=1)
    ggl_name                        = models.TextField(max_length=100, default="tbd")
    Confidence                      = models.CharField(max_length=10, default="tbd")
    ggl_Street                      = models.CharField(max_length=100, default="tbd")
    ggl_Town                        = models.CharField(max_length=100, default="tbd")
    ggl_State                       = models.CharField(max_length=2, default="tbd")
    ggl_Website                     = models.CharField(max_length=100, default="tbd")            
    ggl_Phone                       = models.CharField(max_length=100, default="tbd")               
    CLIENT                          = models.CharField(max_length=10, default="tbd")  