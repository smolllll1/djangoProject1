# Generated by Django 4.1.7 on 2023-03-07 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_galerys'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('position',), 'verbose_name': 'Dish'},
        ),
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ('position',), 'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='galerys',
            options={'verbose_name': 'Galery photo'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service'},
        ),
    ]
