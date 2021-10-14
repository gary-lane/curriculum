from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.TextField()
  email = models.EmailField()
  phone = models.CharField(max_length=15)
  is_favorite = models.BooleanField()

def create_contact(name,email,phone,is_favorite):
  c = Contact(name = name,email = email,phone = phone,is_favorite = is_favorite)
  c.save()
  return c

def all_contacts():
  return Contact.objects.all()

def find_contact_by_name(name):
  try:
    return Contact.objects.get(name = name)
  except:
    None


def favorite_contacts():
  return Contact.objects.filter(is_favorite = True)

def update_contact_email(name, new_email):
  c = Contact.objects.get(name = name)
  c.email = new_email
  c.save()

def delete_contact(name):
  c = Contact.objects.get(name = name)
  c.delete()