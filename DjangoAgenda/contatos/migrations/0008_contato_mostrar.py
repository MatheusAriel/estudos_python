# Generated by Django 4.0.4 on 2022-05-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0007_remove_contato_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
