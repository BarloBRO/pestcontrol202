# Generated by Django 4.1.3 on 2022-11-10 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee_information', '0005_auto_20220302_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('action_date', models.DateField()),
                ('action_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs_user', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs_employee', to='employee_information.employees')),
            ],
        ),
    ]