# Generated by Django 3.2.6 on 2021-09-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210902_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='bio',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
