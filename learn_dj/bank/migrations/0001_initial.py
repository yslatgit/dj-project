# Generated by Django 2.1.7 on 2019-04-01 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50, verbose_name='银行名称')),
                ('city', models.CharField(max_length=30, verbose_name='银行所在城市')),
                ('point', models.CharField(max_length=100, verbose_name='网点')),
            ],
            options={
                'verbose_name': '银行',
                'verbose_name_plural': '银行',
                'db_table': 'Bank',
            },
        ),
        migrations.CreateModel(
            name='CardInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.CharField(max_length=20, verbose_name='卡号')),
                ('card_type', models.CharField(max_length=10, verbose_name='卡类型')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Bank', verbose_name='选择银行')),
            ],
            options={
                'verbose_name': '卡号',
                'verbose_name_plural': '卡号',
                'db_table': 'Card',
            },
        ),
    ]
