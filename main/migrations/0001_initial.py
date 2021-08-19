# Generated by Django 3.0 on 2021-08-19 19:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ANC', 'Anc'), ('INF', 'Inf'), ('GYNAC', 'Gynac')], default='ANC', max_length=5)),
                ('case_paper_number', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(10)])),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(65)])),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Female', max_length=10)),
                ('mobile_number', models.CharField(max_length=12)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address_line_1', models.CharField(blank=True, max_length=100)),
                ('address_line_2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('pin_code', models.IntegerField(blank=True, null=True)),
                ('referred_by', models.CharField(blank=True, max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_inf', models.BooleanField(default=False)),
                ('is_anc', models.BooleanField(default=False)),
                ('is_gynac', models.BooleanField(default=False)),
            ],
        ),
    ]