# Generated by Django 5.1.4 on 2025-01-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_member_data_alter_member_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='data',
            field=models.DateField(max_length=100, verbose_name='Дата приема на работу'),
        ),
    ]
