# Generated by Django 4.1.4 on 2023-01-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ageRating', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ageRating', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('totalCost', models.CharField(default='£2.50', max_length=6)),
                ('showingDate', models.CharField(default='08/10/2023', max_length=10)),
                ('showingTime', models.CharField(default='14:00', max_length=10)),
                ('seating', models.CharField(default='[A,3]', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(default='20005074', max_length=20)),
                ('password', models.CharField(default='Password123', max_length=20)),
                ('name', models.CharField(default='Will', max_length=30)),
                ('dob', models.CharField(default='12/07/2002', max_length=10)),
                ('phone', models.CharField(default='07576928525', max_length=11)),
                ('email', models.CharField(default='william2.robertson@live.uwe.ac.uk', max_length=50)),
                ('address', models.CharField(default='BS1 1QY', max_length=100)),
            ],
        ),
    ]
