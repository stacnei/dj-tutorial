# Generated by Django 2.1 on 2018-09-08 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20180908_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='index_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='courses',
            name='index_str',
            field=models.CharField(editable=False, max_length=10),
        ),
    ]
