from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class FooTest(models.Model):
    foo = models.TextField('Всякая всячина', default = 'foo', blank = True)
    ord = models.PositiveSmallIntegerField('Порядок', blank = True)
    dt_create = models.DateTimeField('Дата создания', default = timezone.now, blank = True)
    dt_edit = models.DateTimeField('Дата изменения', default = timezone.now, blank = True)
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.SET_NULL)
    def __str__(self):
        return str(self.id) + ":" + self.foo
