# Generated by Django 3.1.7 on 2021-08-29 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sauron_ecommerce', '0002_auto_20210826_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image1',
            field=models.ImageField(default=0, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image2',
            field=models.ImageField(default=0, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image3',
            field=models.ImageField(default=0, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image4',
            field=models.ImageField(default=0, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image5',
            field=models.ImageField(default=0, null=True, upload_to=None),
        ),
    ]
