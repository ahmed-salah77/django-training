# Generated by Django 4.1.2 on 2022-10-26 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(default='images/def.jpg', upload_to='songs/'),
        ),
    ]