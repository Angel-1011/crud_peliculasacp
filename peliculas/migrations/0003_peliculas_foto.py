# Generated by Django 5.1.2 on 2024-10-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_rename_fecha_es_peliculas_año'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='peliculas_fotos/'),
        ),
    ]
