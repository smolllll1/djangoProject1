# Generated by Django 4.1.7 on 2023-03-10 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_service_body_alter_service_year_in_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='year_in_school',
            new_name='position',
        ),
    ]
