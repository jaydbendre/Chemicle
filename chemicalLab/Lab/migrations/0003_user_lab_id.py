# Generated by Django 3.0.4 on 2020-03-17 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lab', '0002_remove_user_lab_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lab_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Lab.Lab'),
        ),
    ]
