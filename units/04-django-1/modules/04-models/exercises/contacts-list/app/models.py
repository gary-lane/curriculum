from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=30)
  email = models.CharField(max_length=50)
  phone = models.CharField(max_length=10)
  is_favorite = models.BooleanField

def create_contact(name, email, phone, is_favorite):
  c = Contact(name,email,phone,is_favorite)
  c.save()

def all_contacts():
  c = Contact.objects.all

def find_contact_by_name(name):
  c = Contact.objects.filter(name)

def favorite_contacts():
  c = Contact.objects.filter(is_favorite=True)

def update_contact_email(name, new_email):
  c = Contact.objects.get(name)
  c.email = new_email
  c.save()

def delete_contact(name):
  c = Contact.objects.get(name)
  c.delete()