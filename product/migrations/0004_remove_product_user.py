# Generated by Django 5.0.2 on 2024-03-02 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]