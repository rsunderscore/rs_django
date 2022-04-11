# Generated by Django 3.2.5 on 2022-04-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20220321_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='target completion date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
