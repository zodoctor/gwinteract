# Generated by Django 2.1.2 on 2019-01-08 19:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewPopSynthModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_kstar1', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[13, 15], size=None)),
                ('final_kstar2', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[13, 15], size=None)),
                ('convergence_params', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), default=['mass_1', 'mass_2', 'porb', 'ecc'], size=None)),
                ('initial_samp', models.CharField(choices=[('independent', 'independent'), ('multidim', 'multidim')], max_length=20)),
                ('galaxy_component', models.CharField(choices=[('ThinDisk', 'ThinDisk'), ('Bulge', 'Bulge'), ('ThickDisk', 'ThickDisk'), ('DeltaBurst', 'DeltaBurst'), ('FIRE', 'FIRE')], max_length=20)),
                ('metallicity', models.FloatField(default=0.002)),
                ('Niter', models.IntegerField(default=100000000)),
                ('Nstep', models.IntegerField(default=100000)),
                ('mass_transfer_white_dwarf_to_co', models.BooleanField(default=False)),
                ('select_final_state', models.BooleanField(default=True)),
                ('binary_state', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[0, 1, 2], size=None)),
                ('merger_type', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=4), default=['-001'], size=None)),
                ('LISA_convergence', models.BooleanField(default=False)),
                ('seed', models.IntegerField(default=21)),
                ('neta', models.FloatField(default=0.5)),
                ('bwind', models.FloatField(default=0.0)),
                ('hewind', models.FloatField(default=1.0)),
                ('alpha1', models.FloatField(default=1.0)),
                ('lambdaf', models.FloatField(default=1.0)),
                ('ceflag', models.FloatField(default=0)),
                ('tflag', models.FloatField(default=1)),
                ('ifflag', models.FloatField(default=0)),
                ('wdflag', models.FloatField(default=0)),
                ('bhflag', models.FloatField(default=1)),
                ('nsflag', models.FloatField(default=3)),
                ('mxns', models.FloatField(default=3.0)),
                ('pts1', models.FloatField(default=0.05)),
                ('pts2', models.FloatField(default=0.01)),
                ('pts3', models.FloatField(default=0.02)),
                ('sigma', models.FloatField(default=265.0)),
                ('beta', models.FloatField(default=-1.0)),
                ('xi', models.FloatField(default=0.5)),
                ('acc2', models.FloatField(default=1.5)),
                ('epsnov', models.FloatField(default=0.001)),
                ('eddfac', models.FloatField(default=1.0)),
                ('gamma', models.FloatField(default=-2.0)),
                ('bconst', models.FloatField(default=-3000)),
                ('CK', models.FloatField(default=-1000)),
                ('merger', models.FloatField(default=0)),
                ('windflag', models.FloatField(default=3)),
                ('B_0', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[0.0, 0.0], size=None)),
                ('bacc', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[0.0, 0.0], size=None)),
                ('tacc', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[0.0, 0.0], size=None)),
                ('bkick', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=None)),
                ('massc', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[0.0, 0.0], size=None)),
                ('opsin', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[0.0, 0.0], size=None)),
                ('epoch', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[0.0, 0.0], size=None)),
                ('tphys', models.FloatField(default=0.0)),
                ('ppsn', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False)),
            ],
        ),
    ]
