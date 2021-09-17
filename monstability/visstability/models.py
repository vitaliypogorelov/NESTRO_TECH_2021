"""
    'AutoField', 'BLANK_CHOICE_DASH', 'BigAutoField', 'BigIntegerField',
    'BinaryField', 'BooleanField', 'CharField', 'CommaSeparatedIntegerField',
    'DateField', 'DateTimeField', 'DecimalField', 'DurationField',
    'EmailField', 'Empty', 'Field', 'FieldDoesNotExist', 'FilePathField',
    'FloatField', 'GenericIPAddressField', 'IPAddressField', 'IntegerField',
    'NOT_PROVIDED', 'NullBooleanField', 'PositiveIntegerField',
    'PositiveSmallIntegerField', 'SlugField', 'SmallAutoField',
    'SmallIntegerField', 'TextField', 'TimeField', 'URLField', 'UUIDField',
"""
from django.db import models

class Nodes(models.Model):
    """ вершины графа устойчивости"""

    NODES_TYPE = [
        ('metric', 'метрика'),
        ('or', 'И'),
        ('and', 'ИЛИ'),
        ('true', 'единица'),
        ('service', 'сервис'),
    ]
    LAYER_TYPE = [
        ('it', 'ИТ-ресурс'),
        ('bs', 'Бизнес-система'),
        ('bu', 'Бизнес-услуга'),
        ('br', 'Бизнес-решение'),
        ('bp', 'Бизнес-процесс'),
        ('ot', 'Прочее'),
    ]
    id_gr= models.CharField('idgr',
                            help_text='id вершины',
                            max_length=10,
                            )
    label_gr = models.CharField('label',
                                help_text='Название вершины',
                                max_length=100,
                                )
    type_gr = models.CharField('type',
                               help_text='Тип вершины графа',
                               max_length=10,
                               choices=NODES_TYPE,
                               )
    layer = models.CharField('layer',
                              help_text='Бизнес-слой',
                              max_length=4,
                              choices=LAYER_TYPE,
                              )
    access = models.IntegerField('access',
                                  help_text='Доступность',
                                  )

    stead = models.FloatField('stead',
                              help_text='Устойчивость',
                              )
    costdown = models.FloatField('costdown',
                              help_text='Стоимость простоя',
                              )

    def __str__(self):
        return f"{self.label_gr} ({self.id_gr})"

    class Meta:
        verbose_name = 'Вершина графа устойчивости'
        verbose_name_plural = 'Вершины графа устойчивости'

class Edges(models.Model):
    """ ребра графа устойчивости"""

    id_gr= models.CharField('idgr',
                            help_text='id ребра',
                            max_length=10,
                            )
    source = models.CharField('source',
                            help_text='Верхина начало',
                            max_length=10,
                            )
    target = models.CharField('target',
                                help_text='Вершина конец',
                                max_length=10,
                                )
    weight = models.FloatField('weight',
                              help_text='Весм вершины',
                              )
    def __str__(self):
        return f"({self.source}) - ({self.source})"

    class Meta:
        verbose_name = 'Ребро графа устойчивости'
        verbose_name_plural = 'Ребра графа устойчивости'
