# Generated by Django 2.1.2 on 2018-10-30 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181030_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota_Adoptante',
            fields=[
                ('id_socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.Socio')),
                ('id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Mascota')),
            ],
        ),
    ]