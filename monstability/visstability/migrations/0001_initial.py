# Generated by Django 3.2.7 on 2021-09-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(help_text='Верхина начало', max_length=10, verbose_name='source')),
                ('target', models.CharField(help_text='Вершина конец', max_length=10, verbose_name='target')),
                ('weight', models.FloatField(help_text='Весм вершины', verbose_name='weight')),
            ],
            options={
                'verbose_name': 'Ребро графа устойчивости',
                'verbose_name_plural': 'Ребра графа устойчивости',
            },
        ),
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_gr', models.CharField(help_text='id вершины', max_length=10, verbose_name='id')),
                ('label_gr', models.CharField(help_text='Название вершины', max_length=100, verbose_name='label')),
                ('type_gr', models.CharField(choices=[('metric', 'метрика'), ('or', 'И'), ('and', 'ИЛИ'), ('service', 'сервис')], help_text='Тип вершины графа', max_length=10, verbose_name='type')),
                ('layer', models.CharField(choices=[('it', 'ИТ-ресурс'), ('bs', 'Бизнес-система'), ('bu', 'Бизнес-услуга'), ('br', 'Бизнес-решение'), ('bp', 'Бизнес-процесс'), ('none', 'Прочее')], help_text='Бизнес-слой', max_length=4, verbose_name='layer')),
                ('access', models.IntegerField(help_text='Доступность', verbose_name='access')),
                ('stead', models.FloatField(help_text='Устойчивость', verbose_name='stead')),
            ],
            options={
                'verbose_name': 'Вершина графа устойчивости',
                'verbose_name_plural': 'Вершины графа устойчивости',
            },
        ),
    ]
