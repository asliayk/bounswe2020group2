# Generated by Django 3.1.3 on 2021-01-23 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0029_merge_20210123_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.product')),
            ],
        ),
    ]
