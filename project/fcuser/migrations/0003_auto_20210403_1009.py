# Generated by Django 3.1.7 on 2021-04-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_auto_20210403_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], max_length=24, verbose_name='등급'),
        ),
    ]