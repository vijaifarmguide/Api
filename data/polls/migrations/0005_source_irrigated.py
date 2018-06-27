# Generated by Django 2.0.6 on 2018-06-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180620_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='source_irrigated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=200)),
                ('net_government_canal', models.IntegerField()),
                ('net_private_canal', models.IntegerField()),
                ('net_total_canal', models.IntegerField()),
                ('net_tank', models.IntegerField()),
                ('net_tubewell', models.IntegerField()),
                ('net_other_well', models.IntegerField()),
                ('net_total_well', models.IntegerField()),
                ('net_other_source', models.IntegerField()),
                ('net_irrigated_area', models.IntegerField()),
                ('gross_government_canal', models.IntegerField()),
                ('gross_private_canal', models.IntegerField()),
                ('gross_total_canal', models.IntegerField()),
                ('gross_tank', models.IntegerField()),
                ('gross_tubewell', models.IntegerField()),
                ('gross_other_well', models.IntegerField()),
                ('gross_total_well', models.IntegerField()),
                ('gross_other_source', models.IntegerField()),
                ('gross_irrigated_area', models.IntegerField()),
                ('state', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'source_irrigated_area_csv',
                'managed': False,
            },
        ),
    ]