# Generated by Django 4.2.16 on 2024-10-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('salary_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('position', models.CharField(max_length=100)),
                ('doj', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('mobile_no', models.CharField(max_length=15)),
            ],
        ),
    ]
