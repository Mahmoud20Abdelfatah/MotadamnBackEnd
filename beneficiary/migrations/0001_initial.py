# Generated by Django 3.0.7 on 2020-06-08 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('charity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('national_id', models.BigIntegerField(unique=True)),
                ('gender', models.IntegerField()),
                ('martial_status', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('photo', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.Charity')),
            ],
            options={
                'db_table': 'beneficiary',
                'managed': True,
            },
        ),
    ]