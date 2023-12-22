# Generated by Django 4.2.8 on 2023-12-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('effect', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(verbose_name='Review Date'),
        ),
        migrations.AddField(
            model_name='guitar',
            name='pedals',
            field=models.ManyToManyField(to='main_app.pedal'),
        ),
    ]
