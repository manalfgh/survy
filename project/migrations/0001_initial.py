# Generated by Django 3.0.7 on 2020-11-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('willaya', models.CharField(blank=True, max_length=30, null=True)),
                ('commune', models.CharField(blank=True, max_length=27, null=True)),
                ('willayaTravail', models.CharField(blank=True, max_length=30, null=True)),
                ('communeTravail', models.CharField(blank=True, max_length=27, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('infection', models.BooleanField()),
                ('nom', models.CharField(blank=True, max_length=20, null=True)),
                ('prenom', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]