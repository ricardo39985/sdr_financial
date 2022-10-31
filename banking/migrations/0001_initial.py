# Generated by Django 4.1.2 on 2022-10-29 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('balance', models.IntegerField()),
                ('type', models.CharField(choices=[('C', 'Checkings'), ('S', 'Savings')], default='C', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Transaction Date')),
                ('amount', models.IntegerField()),
                ('remaining_balance', models.IntegerField()),
                ('description', models.TextField(max_length=12)),
                ('type', models.CharField(choices=[('W', 'Withdraw'), ('D', 'Deposit'), ('P', 'Purchase')], default='W', max_length=1)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.account')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]