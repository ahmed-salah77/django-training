# Generated by Django 4.1.2 on 2022-10-23 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0007_artist_approved_albums_alter_artist_social_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='approved_albums',
        ),
    ]