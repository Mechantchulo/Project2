# Generated by Django 4.2.16 on 2024-12-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_propertylisting_num_bathrooms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylisting',
            name='custom_property_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='property_type',
            field=models.CharField(choices=[('house', 'House'), ('apartment', 'Apartment'), ('condo', 'Condo'), ('townhouse', 'Townhouse'), ('villa', 'Villa'), ('studio', 'Studio'), ('loft', 'Loft'), ('duplex', 'Duplex'), ('penthouse', 'Penthouse'), ('bungalow', 'Bungalow'), ('cabin', 'Cabin'), ('farmhouse', 'Farmhouse'), ('ranch', 'Ranch'), ('mobile_home', 'Mobile Home'), ('commercial', 'Commercial'), ('other', 'Other')], max_length=100),
        ),
    ]
