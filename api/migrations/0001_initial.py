# Generated by Django 4.1.6 on 2023-03-18 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=254)),
                ('fullname', models.CharField(default='', max_length=254)),
                ('home_address', models.TextField(blank=True, default='', max_length=600, null=True)),
                ('city', models.CharField(default='', max_length=254)),
                ('state', models.CharField(default='', max_length=254)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('cartItems', models.CharField(default='', max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemIDArr', models.CharField(default='', max_length=900)),
                ('itemTotalPrice', models.DecimalField(decimal_places=2, max_digits=10000000)),
                ('hasPaid', models.BooleanField(default=False)),
                ('deliveryStatus', models.IntegerField(choices=[(0, 'pending'), (1, 'confirmed'), (2, 'shipped'), (3, 'delivered'), (4, 'rejected')], default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
