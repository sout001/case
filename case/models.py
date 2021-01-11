from django.db import models
from django.utils.timezone import now
from case.utils import get_upload_path, file_upload_path, tea_id, stu_id
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


SEX_TYPE = (
    (0, '男'),
    (1, '女')
)


class ClassModel(BaseModel):
    class_name = models.CharField(verbose_name="班级名称", max_length=50)
    class_nums = models.IntegerField(verbose_name="班级人数", default=30)

    class Meta:
        verbose_name = "班级"
        verbose_name_plural = "班级"
        db_table = "class"

    def __str__(self):
        return "班级-" + self.class_name


class TeacherModel(BaseModel):
    tea_id = models.CharField(verbose_name="教师编号", max_length=18, null=False, blank=False, unique=True,
                              default=tea_id)
    tea_name = models.CharField(verbose_name="教师名称", max_length=50)
    tea_sex = models.IntegerField(verbose_name="教师性别", choices=SEX_TYPE, default=0)
    tea_age = models.IntegerField(verbose_name="教师年龄", null=True, blank=True)
    tea_class = models.ManyToManyField(ClassModel, verbose_name="所教班级")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = "教师"
        db_table = "teacher"

    def __str__(self):
        return "教师-" + self.tea_name


class StudentModel(BaseModel):
    stu_id = models.CharField(verbose_name="学号", max_length=18, null=False, unique=True, blank=False,
                              default=stu_id)
    stu_name = models.CharField(verbose_name="学生姓名", max_length=50, null=False, blank=False)
    stu_age = models.IntegerField(verbose_name="学生年龄")
    stu_sex = models.IntegerField(verbose_name="学生性别", choices=SEX_TYPE, default=0)
    stu_class = models.ForeignKey(ClassModel, verbose_name="所属班级", to_field='id', related_name="stu_class",
                                  on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生"
        db_table = "student"

    def __str__(self):
        return "学生-" + self.stu_name


