# Generated by Django 3.2.8 on 2023-03-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0009_alter_jasa_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jasa',
            name='gambar',
            field=models.ImageField(default='static/artikel/mebel.jpg', upload_to='static/'),
        ),
    ]
