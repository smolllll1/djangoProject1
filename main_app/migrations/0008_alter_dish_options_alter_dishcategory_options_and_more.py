# Generated by Django 4.1.7 on 2023-03-07 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_dish_options_alter_dishcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('position',)},
        ),
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ('position',)},
        ),
        migrations.AlterModelOptions(
            name='galerys',
            options={},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={},
        ),
    ]
