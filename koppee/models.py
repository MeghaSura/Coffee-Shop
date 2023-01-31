from django.db import models

# Create your models here.
class admindb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Uname = models.CharField(max_length=100, null=True, blank=True)
    Pswrd = models.CharField(max_length=100, null=True, blank=True)
    Cnfrm = models.CharField(max_length=100, null=True, blank=True)


class catdb(models.Model):
    Catname= models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class coffeedb(models.Model):
    Coffeename = models.CharField(max_length=100, null=True, blank=True)
    Price = models.CharField(max_length=100, null=True, blank=True)
    About = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)

class contactdb(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    mail=models.EmailField(null=True, blank=True)
    subject=models.CharField(max_length=100, null=True, blank=True)
    msg=models.CharField(max_length=100, null=True, blank=True)





