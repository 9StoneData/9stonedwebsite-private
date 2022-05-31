from django.db import models

# Create your models here.
class Company(models.Model):
    id                              = models.AutoField(primary_key=True)
    COMPANY                         = models.TextField()
    TYPE                            = models.CharField(max_length=20)
    Pull_Date                       = models.DateTimeField(auto_now=False)
    Dispenary_base_leaf_url         = models.CharField(max_length=400)
    google_map                      = models.CharField(max_length=400)
    Street                          = models.CharField(max_length=100)
    Town                            = models.CharField(max_length=100)
    ggl_Zip                         = models.CharField(max_length=12)
    State                           = models.CharField(max_length=2)
    Email                           = models.CharField(max_length=100)
    Phone                           = models.CharField(max_length=100)
    Website                         = models.CharField(max_length=200)
    ACTIVE_on_LEAFLY                = models.CharField(max_length=10)
    Best_Google_Map_Url             = models.CharField(max_length=400)
    lat                             = models.DecimalField(max_digits=10,decimal_places=6)
    lon                             = models.DecimalField(max_digits=10,decimal_places=6)
    ggl_name                        = models.TextField(max_length=100)
    Confidence                      = models.CharField(max_length=10)
    ggl_Street                      = models.CharField(max_length=100)
    ggl_Town                        = models.CharField(max_length=100)
    ggl_State                       = models.CharField(max_length=2)
    ggl_Website                     = models.CharField(max_length=100)            
    ggl_Phone                       = models.CharField(max_length=100)               
    CLIENT                          = models.CharField(max_length=10)                   