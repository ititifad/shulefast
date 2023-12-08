# Generated by Django 4.2.7 on 2023-12-07 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_schooljoining_show_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schoolgallery', to='core.school')),
            ],
        ),
    ]