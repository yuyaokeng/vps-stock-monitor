# Generated by Django 2.2.5 on 2020-06-15 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='arch',
            field=models.CharField(choices=[('KVM', 'KVM'), ('OpenVZ', 'OpenVZ')], max_length=256, verbose_name='架构'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='dc',
            field=models.CharField(max_length=256, verbose_name='机房'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='ram',
            field=models.CharField(max_length=256, verbose_name='内存'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='stock',
            field=models.IntegerField(choices=[(0, '无货'), (1, '有货')], default=0, verbose_name='库存'),
        ),
    ]
