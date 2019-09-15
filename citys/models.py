import uuid

from django.db import models


# Create your models here.
class CitysModel(models.Model):
    id = models.UUIDField(primary_key=True,
                          verbose_name='城市编号')
    name = models.CharField(max_length=20,
                            verbose_name='城市名称',
                            null=False)
    fever = models.BooleanField(verbose_name='是否热门',
                                choices=((True, '是'),
                                         (False, '否')))
    s_letter = models.CharField(max_length=1,
                                verbose_name='排行名称')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()

    class Meta:
        db_table = 'db_citys'
        verbose_name = '各大城市'
        verbose_name_plural = verbose_name
