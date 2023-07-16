# Generated by Django 4.2.2 on 2023-07-09 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='media/')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]