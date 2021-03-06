# Generated by Django 2.1.7 on 2019-12-14 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('crime_status', models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSE', 'CLOSE'), ('PENDING', 'PENDING')], default='OPEN', max_length=50)),
                ('court', models.CharField(blank=True, max_length=255, null=True)),
                ('verdict', models.CharField(blank=True, max_length=100, null=True)),
                ('country_of_crime', models.CharField(blank=True, max_length=50, null=True)),
                ('state_of_crime', models.CharField(blank=True, choices=[('ABIA', 'ABIA'), ('ADAMAWA', 'ADAMAWA'), ('AKWA IBOM', 'AKWA IBOM'), ('ANAMBRA', 'ANAMBRA'), ('BAUCHI', 'BAUCHI'), ('BAYELSA', 'BAYELSA'), ('BENUE', 'BENUE'), ('BORNO', 'BORNO'), ('CROSS RIVER', 'CROSS RIVER'), ('DELTA', 'DELTA'), ('EBONYI', 'EBONYI'), ('EDO', 'EDO'), ('EKITI', 'EKITI'), ('ENUGU', 'ENUGU'), ('GOMBE', 'GOMBE'), ('IMO', 'IMO'), ('JIGAWA', 'JIGAWA'), ('KADUNA', 'KADUNA'), ('KANO', 'KANO'), ('KASTINA', 'KASTINA'), ('KEBBI', 'KEBBI'), ('KOGI', 'KOGI'), ('KWARA', 'KWARA'), ('LAGOS', 'LAGOS'), ('NASARAWA', 'NASARAWA'), ('NIGER', 'NIGER'), ('OGUN', 'OGUN'), ('ONDO', 'ONDO'), ('OSUN', 'OSUN'), ('OYO', 'OYO'), ('PLATEAU', 'PLATEAU'), ('RIVERS', 'RIVERS'), ('SOKOTO', 'SOKOTO'), ('TARABA', 'TARABA'), ('YOBE', 'YOBE'), ('ZAMFARA', 'ZAMFARA'), ('ABUJA', 'ABUJA')], max_length=50, null=True)),
                ('local_gov_area', models.CharField(blank=True, choices=[('Barkin Ladi L.G.A', 'Barkin Ladi L.G.A'), ('Barkin Ladi Town Area', 'Barkin Ladi Town Area'), ('Bassa West LGA', 'Bassa West LGA'), ('Bokkos L.G.A', 'Bokkos L.G.A'), ('Jos', 'Jos'), ('Jos East L.G.A', 'Jos East L.G.A'), ('Jost North L.G.A', 'Jost North L.G.A'), ('Jos South L.G.A', 'Jos South L.G.A'), ('Kanam L.G.A', 'Kanam L.G.A'), ('Kanke L.G.A', 'Kanke L.G.A'), ('Langtang South L.G.A', 'Langtang South L.G.A'), ('Mangu Zip L.G.A', 'Mangu Zip L.G.A'), ('Mikang L.G.A', 'Mikang L.G.A'), ('Pankshin L.G.A', 'Pankshin L.G.A'), ('Qua', 'Qua'), ('Riyom L.G.A', 'Riyom L.G.A'), ('Shendam L.G.A', 'Shendam L.G.A'), ('Wase L.G.A', 'Wase L.G.A')], max_length=50, null=True)),
                ('city_of_crime', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_crime', models.DateField(blank=True, null=True)),
                ('time_of_crime', models.TimeField(blank=True, null=True)),
                ('statement', models.CharField(blank=True, max_length=255, null=True)),
                ('date_added', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('aliases', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_birth', models.DateField()),
                ('hair_color', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('sex', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], default='Male', max_length=50)),
                ('occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('wanted_status', models.CharField(choices=[('WANTED', 'wanted'), ('NOT_WANTED', 'not_wanted')], default='NOT_WANTED', max_length=50)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('state_of_origin', models.CharField(blank=True, choices=[('ABIA', 'ABIA'), ('ADAMAWA', 'ADAMAWA'), ('AKWA IBOM', 'AKWA IBOM'), ('ANAMBRA', 'ANAMBRA'), ('BAUCHI', 'BAUCHI'), ('BAYELSA', 'BAYELSA'), ('BENUE', 'BENUE'), ('BORNO', 'BORNO'), ('CROSS RIVER', 'CROSS RIVER'), ('DELTA', 'DELTA'), ('EBONYI', 'EBONYI'), ('EDO', 'EDO'), ('EKITI', 'EKITI'), ('ENUGU', 'ENUGU'), ('GOMBE', 'GOMBE'), ('IMO', 'IMO'), ('JIGAWA', 'JIGAWA'), ('KADUNA', 'KADUNA'), ('KANO', 'KANO'), ('KASTINA', 'KASTINA'), ('KEBBI', 'KEBBI'), ('KOGI', 'KOGI'), ('KWARA', 'KWARA'), ('LAGOS', 'LAGOS'), ('NASARAWA', 'NASARAWA'), ('NIGER', 'NIGER'), ('OGUN', 'OGUN'), ('ONDO', 'ONDO'), ('OSUN', 'OSUN'), ('OYO', 'OYO'), ('PLATEAU', 'PLATEAU'), ('RIVERS', 'RIVERS'), ('SOKOTO', 'SOKOTO'), ('TARABA', 'TARABA'), ('YOBE', 'YOBE'), ('ZAMFARA', 'ZAMFARA'), ('ABUJA', 'ABUJA')], max_length=50, null=True)),
                ('foot_size', models.CharField(blank=True, max_length=50, null=True)),
                ('place_of_arrest', models.CharField(blank=True, max_length=255, null=True)),
                ('residence', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_arrest', models.DateField(blank=True, null=True)),
                ('image1', models.ImageField(default='default1.jpg', upload_to='criminal_pics/')),
                ('image2', models.ImageField(default='default2.jpg', upload_to='criminal_pics/')),
                ('crime', models.ManyToManyField(to='Criminal.Crime')),
            ],
        ),
        migrations.CreateModel(
            name='FingerPrint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_thumb', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('right_index', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('right_middle', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('right_ring', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('right_pinky', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('left_thumb', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('left_index', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('left_middle', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('left_ring', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('left_pinky', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('criminal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='criminal_print', to='Criminal.Criminal')),
            ],
        ),
    ]
