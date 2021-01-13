from django.db import models
from django.utils.timezone import now
from django.db.models.query import QuerySet
import datetime


# Create your models here.

class TimestampQuerySet(QuerySet):
    # 逻辑删除
    def delete(self, hard=False):
        if hard:
            return super().delete()
        else:
            return self.update(delete_time=datetime.datetime.now())


# 重写queryset查询
class TimestampManager(models.Manager):
    _queryset_class = TimestampQuerySet

    def get_queryset(self):
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints
        return self._queryset_class(**kwargs).filter(delete_time__isnull=True, enabled=True)


class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", default=now)
    update_time = models.DateTimeField(verbose_name="修改时间", default=now)
    delete_time = models.DateTimeField(verbose_name="删除时间", null=True, blank=True)
    enabled = models.BooleanField(verbose_name="是否有效", default=1)

    class Meta:
        abstract = True

    object = TimestampManager()


RESOURCE_TYPE = (
    (0, '图片'),
    (1, '音频'),
    (2, '视频'),
)


class ResourceModel(BaseModel):
    resource_name = models.CharField(verbose_name="资源名称", max_length=50)
    resource_type = models.IntegerField(verbose_name="资源类型", choices=RESOURCE_TYPE)
    cover = models.CharField(verbose_name="封面", max_length=120)
    status = models.CharField(verbose_name="资源状态:(Y:已上架,N:未上架,D:已下架)", max_length=1, default="N")

    class Meta:
        verbose_name = "资源"
        verbose_name_plural = "资源"
        db_table = "resource"


class IndexPackage(BaseModel):
    package_name = models.CharField(verbose_name="资源包名称", max_length=50)
    title = models.CharField(verbose_name="标题", max_length=200, null=True, blank=True)
    resource = models.ForeignKey(ResourceModel, verbose_name="资源", to_field='id', related_name='resource',
                                 on_delete=models.DO_NOTHING)
    cover = models.CharField(verbose_name="封面", max_length=120)
    like_nums = models.IntegerField(verbose_name="点赞数", null=True, blank=True, default=0)
    collect_nums = models.IntegerField(verbose_name="收藏数", null=True, blank=True, default=0)
    order_on = models.IntegerField(verbose_name="顺序", default=0)

    class Meta:
        verbose_name = "资源包"
        verbose_name_plural = "资源包"
        db_table = "resource_package"


SEX_TYPE = (
    (0, '男'),
    (1, '女')
)


class UserModel(BaseModel):
    user_id = models.CharField(verbose_name="用户id", max_length=32, unique=True)
    user_name = models.CharField(verbose_name="用户昵称", max_length=20)
    user_sex = models.IntegerField(verbose_name="用户性别", default=0)
    user_phone = models.CharField(verbose_name="用户电话", max_length=11, unique=True)
    user_pwd = models.CharField(verbose_name="用户密码", max_length=32)
    avatar = models.CharField(verbose_name="用户头像", max_length=120)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
        db_table = "user"


class CommitModel(BaseModel):
    parent_id = models.IntegerField(verbose_name="根节点", null=True)
    object = models.ForeignKey(ResourceModel, verbose_name="评论对象", to_field="id", related_name='object',
                               on_delete=models.DO_NOTHING)
    user = models.ForeignKey(UserModel, verbose_name="用户", to_field="id", related_name='user',
                             on_delete=models.DO_NOTHING)
    content = models.CharField(verbose_name="评论内容", max_length=1800)
    like_nums = models.IntegerField(verbose_name="点赞数", default=0)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
        db_table = "commit"
