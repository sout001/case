from django.contrib import admin
from case.models import BaseModel, FileUpload, StudentModel, ClassModel, TeacherModel


# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    exclude = ('create_time', 'update_time', 'delete_time')
    list_per_page = 12


@admin.register(FileUpload)
class FileUploadAdmin(BaseAdmin):
    list_display = ['id', 'file_name', 'file_cover', 'image_display', 'file_size', 'create_time']


@admin.register(StudentModel)
class StudentAdmin(BaseAdmin):
    list_display = ['stu_id', 'stu_name', 'stu_sex', 'stu_class']
    search_fields = ['stu_name', ]
    list_filter = ['stu_class']
    ordering = ['-stu_id']


@admin.register(ClassModel)
class ClassAdmin(BaseAdmin):
    list_display = ['class_name', 'class_nums', ]


@admin.register(TeacherModel)
class ClassAdmin(BaseAdmin):
    list_display = ['tea_id', 'tea_name', 'tea_sex', ]
