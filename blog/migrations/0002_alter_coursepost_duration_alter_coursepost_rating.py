# Generated by Django 5.0.5 on 2024-05-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepost',
            name='duration',
            field=models.TextField(verbose_name='Kurs davomiyligi '),
        ),
        migrations.AlterField(
            model_name='coursepost',
            name='rating',
            field=models.IntegerField(verbose_name='Kursni baholash uchun'),
        ),
    ]