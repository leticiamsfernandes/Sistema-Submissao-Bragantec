# Generated by Django 2.2.7 on 2019-11-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0019_auto_20191128_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='alteracoes',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]