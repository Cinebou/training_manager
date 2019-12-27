# Generated by Django 2.1.2 on 2019-12-27 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='sample_10',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_8',
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='練習タイトル'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_2',
            field=models.TextField(blank=True, null=True, verbose_name='練習内容'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_3',
            field=models.IntegerField(blank=True, null=True, verbose_name='1本目：出力(W)'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_4',
            field=models.IntegerField(blank=True, null=True, verbose_name='２本目：出力(W)'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_5',
            field=models.IntegerField(blank=True, null=True, verbose_name='３本目：出力(W)'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_7',
            field=models.DateField(blank=True, null=True, verbose_name='練習 日付'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_9',
            field=models.IntegerField(blank=True, choices=[(1, '優'), (2, '良'), (3, '可'), (4, '不可')], null=True, verbose_name='サンプル項目9_選択肢（固定）'),
        ),
    ]
