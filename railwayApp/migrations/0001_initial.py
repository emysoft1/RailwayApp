# Generated by Django 4.1.3 on 2022-12-03 18:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_station', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=225)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_title', models.CharField(default='text', max_length=255)),
                ('sub_title', models.CharField(default='text', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_train', models.CharField(max_length=255)),
                ('train_number', models.CharField(max_length=255)),
                ('available_seat', models.IntegerField()),
                ('seat_type', models.CharField(choices=[('Economy', 'Economy'), ('Vip', 'Vip'), ('Others', 'Others')], max_length=255)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('duration', models.DurationField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railwayApp.route')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railwayApp.station')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to='railwayApp.station'),
        ),
        migrations.AddField(
            model_name='route',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From', to='railwayApp.station'),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Adult', 'Adult'), ('Child', 'Child'), ('Others', 'Others')], max_length=255)),
                ('no_of_person', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=255)),
                ('ticket_number', models.CharField(default=uuid.uuid4, max_length=36)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railwayApp.route')),
            ],
        ),
    ]
