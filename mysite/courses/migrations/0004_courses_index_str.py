# Generated by Django 2.1 on 2018-09-08 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_courses_index_str'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='index_str',
            field=models.CharField(default='<django.db.models.fields.AutoField>', editable=False, max_length=10),
        ),
    ]
