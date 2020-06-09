# Generated by Django 3.0.7 on 2020-06-08 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('features', '0001_initial'),
        ('subcategory', '0008_auto_20200608_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubcategoryFeatures',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.Features')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subcategory.Subcategory')),
            ],
            options={
                'db_table': 'subcategory_features',
                'managed': True,
            },
        ),
    ]