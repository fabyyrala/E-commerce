# Generated by Django 5.0.6 on 2024-06-16 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_alter_producto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(blank=True, default=None, upload_to='archivo/productos'),
        ),
    ]
