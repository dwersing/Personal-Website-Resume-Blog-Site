# Generated by Django 2.2 on 2020-10-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default=None, max_length=45),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(max_length=200),
        ),
    ]
