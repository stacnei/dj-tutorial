# Generated by Django 2.1 on 2018-09-08 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_courses_index_str'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['course', 'distance'], 'verbose_name': 'Course'},
        ),
    ]