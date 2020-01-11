# Generated by Django 2.2.5 on 2020-01-08 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20200108_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='metn',
        ),
        migrations.RemoveField(
            model_name='category',
            name='post_id',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.Category'),
        ),
    ]
