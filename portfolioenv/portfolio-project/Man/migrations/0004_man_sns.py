# Generated by Django 3.0 on 2019-12-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Man', '0003_auto_20191213_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='man',
            name='SNS',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
