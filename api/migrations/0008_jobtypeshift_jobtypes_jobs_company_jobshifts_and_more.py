# Generated by Django 4.1.4 on 2022-12-22 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_remove_jobtypeshift_created_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobTypeShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift1', models.CharField(blank=True, max_length=255, null=True)),
                ('shift2', models.CharField(blank=True, max_length=255, null=True)),
                ('shift3', models.CharField(blank=True, max_length=255, null=True)),
                ('shift4', models.CharField(blank=True, max_length=255, null=True)),
                ('shift5', models.CharField(blank=True, max_length=255, null=True)),
                ('shift6', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('record_status', models.CharField(default='created', max_length=255)),
                ('created_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobtypeshift_created_id', to=settings.AUTH_USER_MODEL)),
                ('modified_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobtypeshift_modified_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type1', models.CharField(blank=True, max_length=255, null=True)),
                ('type2', models.CharField(blank=True, max_length=255, null=True)),
                ('type3', models.CharField(blank=True, max_length=255, null=True)),
                ('type4', models.CharField(blank=True, max_length=255, null=True)),
                ('type5', models.CharField(blank=True, max_length=255, null=True)),
                ('type6', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('record_status', models.CharField(default='created', max_length=255)),
                ('created_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobtypes_created_id', to=settings.AUTH_USER_MODEL)),
                ('modified_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobtypes_modified_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jobs',
            name='company_jobshifts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='company_jobshifts', to='api.jobtypeshift'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='company_jobtypes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='company_jobtypes', to='api.jobtypes'),
        ),
    ]
