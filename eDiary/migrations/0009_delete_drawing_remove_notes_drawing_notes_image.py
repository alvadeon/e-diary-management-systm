# Generated by Django 4.2.2 on 2023-08-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eDiary', '0008_delete_uploadimage_alter_notes_drawing'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Drawing',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='drawing',
        ),
        migrations.AddField(
            model_name='notes',
            name='image',
            field=models.ImageField(default=True, upload_to='myimages/'),
        ),
    ]
