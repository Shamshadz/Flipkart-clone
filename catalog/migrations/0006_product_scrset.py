# Generated by Django 4.1 on 2022-09-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='scrset',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
