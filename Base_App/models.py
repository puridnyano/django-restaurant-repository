from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

class Item(models.Model):
    Item_name = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name="Name", on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField()
    Rating = models.IntegerField()

class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()