from django.db import models
from django.utils.timezone import now
from case.utils import get_upload_path, file_upload_path
from django.utils.html import format_html


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
    file_cover = models.ImageField(verbose_name="文件封面", upload_to=get_upload_path)
    file_uid = models.UUIDField(verbose_name="文件uid", null=True, blank=True)
    file = models.FileField(verbose_name="文件", upload_to=file_upload_path)
    file_size = models.CharField(verbose_name="文件大小", max_length=100)

    class Meta:
        verbose_name = "资源中心"
        verbose_name_plural = "资源中心"
        db_table = "resource_center"

    def __str__(self):
        return "id:" + str(self.id) + "-" + "文件名称" + self.file_name

    def image_display(self):
        return format_html('<a href="{}"><img src="{}" width="48px" height="48px"/></a>'
                           , self.file_cover.url, self.file_cover.url)

    image_display.short_description = '文件封面'
