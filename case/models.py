from django.db import models
from django.utils.timezone import now


# Create your models here.

# django文件上传

class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", default=now)
    update_time = models.DateTimeField(verbose_name="修改时间", default=now)
    delete_time = models.DateTimeField(verbose_name="删除时间", null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.create_time is None:
            self.create_time = now()
        if self.update_time is None:
            self.update_time = now()
        super(BaseModel, self).save(*args, **kwargs)

    def update(self):
        self.update_time = now()


class FileUpload(BaseModel):
    file_name = models.CharField(verbose_name="文件名称", max_length=100)
    file_cover = models.ImageField(verbose_name="文件封面", upload_to="")
    file_uid = models.UUIDField(verbose_name="文件uid", null=True, blank=True)
    file = models.FileField(verbose_name="文件", upload_to="")
    file_size = models.CharField(verbose_name="文件大小", max_length=100)

    class Meta:
        verbose_name = "资源中心"
        verbose_name_plural = "资源中心"
        db_table = "resource_center"

    def __str__(self):
        return "id:" + str(self.id) + "-" + "文件名称" + self.file_name


class UserModel(models.Model):
    user_name = models.CharField(verbose_name="用户名字", max_length=100, default="")
    user_tel = models.CharField(verbose_name="用户电话", max_length=11)
    user_pwd = models.CharField(verbose_name="用户密码", max_length=20)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
        db_table = "用户"

