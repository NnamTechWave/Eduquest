# Generated by Django 5.1.2 on 2024-11-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0005_remove_module_course_delete_lesson_delete_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='course_videos/'),
        ),
    ]
