# Generated by Django 2.2.2 on 2019-06-20 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_book_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='customer',
        ),
    ]