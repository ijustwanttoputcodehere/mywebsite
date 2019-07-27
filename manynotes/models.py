from django.db import models
from django.forms import ModelForm
# Create your models here.


class Notes(models.Model):

    CATEGORIES = [
        ('Kid', 'Dzieci'),
        ('Mix', 'Mieszany'),
        ('Women', 'Kobiecy'),
        ('W', 'Warsztaty'),
        ('Men', 'Meski'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='notes/pdfs')
    category = models.CharField(max_length=5, choices=CATEGORIES, default='W')

    def __str__(self):
        return self.title

    def delete(self , *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)


class NoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'author', 'pdf', 'category']
