from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    comments = GenericRelation('Comment')  # 使用GenericRelation可以建立该类与Comment类的反向关联，
                                           # 那么可以通过该类的实例来创建对应的comment

class Picture(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    comments = GenericRelation('Comment')

class Comment(models.Model):
    #  user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    body = models.TextField(blank=True)

    # step1
    # ForeignKey为外键，即在Comment类中，content_type对应了django_content_type表中的某个对象
    content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE)  # 与数据库中的django_content_type表关联起来

    # step2
    object_id = models.PositiveIntegerField()  # 正整数类型，在被关联的表中的实例id，以此来定位具体的实例

    # step3
    content_object = GenericForeignKey()  # 根据content_type和object_id来指向一个模型中的具体实例