# Generated by Django 4.1.2 on 2022-10-11 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_alter_artist_social_links_alter_artist_stage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='social_links',
        ),
    ]
