# Generated by Django 2.2.6 on 2019-10-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_auto_20191022_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='tipo',
            field=models.CharField(choices=[('E', 'Estudante'), ('O', 'Orientador')], max_length=100),
        ),
    ]
