# Generated by Django 4.0.5 on 2022-06-19 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('characteristics', '0001_initial'),
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='characteristics',
            field=models.ManyToManyField(null=True, to='characteristics.characteristic'),
        ),
        migrations.AddField(
            model_name='animal',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.group'),
        ),
    ]
