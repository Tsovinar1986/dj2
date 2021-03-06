# Generated by Django 3.2.5 on 2022-05-30 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Brand name')),
                ('about', models.TextField(verbose_name='Brand about')),
                ('img', models.ImageField(upload_to='media', verbose_name='Brand image')),
                ('shoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes_brand_name', to='main.shoes')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.DeleteModel(
            name='Firm',
        ),
    ]
