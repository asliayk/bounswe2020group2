# Generated by Django 3.1.3 on 2020-12-20 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0016_auto_20201219_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='surname',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('owner_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('serial_number', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('expiration_month', models.IntegerField(blank=True, default=0, null=True)),
                ('expiration_year', models.IntegerField(blank=True, default=0, null=True)),
                ('cvv', models.IntegerField(blank=True, default=0, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.user')),
            ],
        ),
    ]