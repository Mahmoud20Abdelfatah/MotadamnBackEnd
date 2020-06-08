# Generated by Django 3.0.7 on 2020-06-08 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supercategory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'supercategory',
                'verbose_name_plural': 'supercategories',
                'db_table': 'supercategory',
                'managed': True,
            },
        ),
    ]
