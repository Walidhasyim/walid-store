from django.db import models

# Create your models here.

class Books(models.Model):
    judul = models.CharField(max_length=255, unique=True)
    penulis = models.CharField(max_length=255)
    harga = models.IntegerField()
    tanggal_terbit = models.DateField()
    image = models.FileField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return self.judul