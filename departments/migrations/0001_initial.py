# Generated by Django 4.2.4 on 2023-09-10 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('payed_at', models.DateTimeField(auto_now_add=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='departments.invoice')),
            ],
            options={
                'ordering': ['-payed_at', 'invoice'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('head_doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('specializations', models.ManyToManyField(to='hospital.specialization')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveBigIntegerField(default=1, unique=True)),
                ('availability', models.CharField(choices=[('available', 'Available'), ('occupied', 'Occupied')], default='availabale', max_length=9)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Amdission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('canceled', 'Canceled'), ('completed', 'Completed')], default='scheduled', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.bed')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
