# Generated by Django 5.0.2 on 2024-03-02 03:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_cartitem_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]