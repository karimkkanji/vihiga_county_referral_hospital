# Generated by Django 3.1.4 on 2020-12-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=1200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
