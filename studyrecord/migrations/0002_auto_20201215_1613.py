# Generated by Django 3.1.3 on 2020-12-15 14:13

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('studyrecord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='grade',
            field=django_cryptography.fields.encrypt(models.IntegerField(default=0)),
        ),
    ]