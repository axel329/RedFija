# Generated by Django 3.0.5 on 2020-04-18 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0002_auto_20200409_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seguimiento',
            name='tipo_seguimiento',
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='tipo_seguimiento',
            field=models.ManyToManyField(to='seguimiento.Tipo_seguimiento', verbose_name='Tipo'),
        ),
    ]