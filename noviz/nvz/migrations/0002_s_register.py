# Generated by Django 2.2.5 on 2019-10-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nvz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('roll', models.TextField(null=True)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
