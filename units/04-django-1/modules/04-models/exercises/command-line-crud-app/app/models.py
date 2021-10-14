from django.db import models

# Create your models here.
class Item(models.Model):
  name = models.TextField(max_length=30)
  value = models.DecimalField(decimal_places=2,max_digits=30)
  amount = models.PositiveIntegerField()
  is_favorite = models.BooleanField()

def add_item(name,value,amount,is_favorite):
  i = Item(name = name,value = value,amount = amount,is_favorite = is_favorite)
  i.save()
  return i

def all_items():
  return Item.objects.all()

def find_item_by_name(name):
  try:
    return Item.objects.get(name = name)
  except:
    None

def favorite_items():
  return Item.objects.filter(is_favorite = True)

def update_item_amount(name, new_amount):
  i = Item.objects.get(name = name)
  i.amount = new_amount
  i.save()

def delete_item(name):
  i = Item.objects.get(name = name)
  i.delete()