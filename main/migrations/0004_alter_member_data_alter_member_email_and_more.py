# Generated by Django 4.2.7 on 2024-12-28 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_member_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='data',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
