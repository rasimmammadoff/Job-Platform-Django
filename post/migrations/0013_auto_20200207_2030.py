# Generated by Django 2.2.5 on 2020-02-07 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]