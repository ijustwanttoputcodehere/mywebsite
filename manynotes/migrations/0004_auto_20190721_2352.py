# Generated by Django 2.2.2 on 2019-07-21 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manynotes', '0003_auto_20190721_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='category',
            field=models.CharField(choices=[('Kid', 'Dzieci'), ('Mix', 'Mieszany'), ('Women', 'Kobiecy'), ('W', 'Warsztaty'), ('Men', 'Meski')], default='W', max_length=5),
        ),
    ]