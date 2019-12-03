# Generated by Django 2.2.7 on 2019-11-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0020_auto_20191128_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='email_autor_1',
            field=models.EmailField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='email_autor_2',
            field=models.EmailField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='email_autor_3',
            field=models.EmailField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='email_orientador_1',
            field=models.EmailField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='email_orientador_2',
            field=models.EmailField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='status',
            field=models.CharField(choices=[('AA', 'Aguardando Avaliação'), ('R', 'Rejeitado'), ('A', 'Aceito')], default='Aguardando Avaliação', max_length=100),
        ),
    ]
