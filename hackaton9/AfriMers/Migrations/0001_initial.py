# Generated by Django 3.1.2 on 2020-10-26 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchaser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoldItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('farm_email', models.CharField(max_length=40)),
                ('purch_email', models.CharField(max_length=40)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=20)),
                ('itemimage', models.FileField(max_length=250, upload_to='')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AfriMers.farmer')),
            ],
        ),
    ]
