# Generated by Django 4.1.2 on 2022-10-10 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_alter_artist_social_links_alter_artist_stage_name'),
        ('albums', '0002_alter_album_creation_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='artists.artist'),
            preserve_default=False,
        ),
    ]