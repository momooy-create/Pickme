# Generated by Django 3.0 on 2019-12-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Women', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='women',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
