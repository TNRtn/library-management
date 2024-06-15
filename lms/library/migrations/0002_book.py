# Generated by Django 3.0 on 2023-11-17 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('isbn', models.CharField(max_length=20)),
                ('year', models.DateField(null=True)),
                ('size', models.IntegerField()),
                ('authorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Author')),
            ],
        ),
    ]