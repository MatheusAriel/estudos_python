# Generated by Django 4.0.4 on 2022-05-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0008_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]
