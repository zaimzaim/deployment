# Generated by Django 4.1.4 on 2023-02-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('itemName', models.TextField()),
                ('category', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
