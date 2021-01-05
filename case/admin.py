from django.contrib import admin
from case.models import BaseModel, FileUpload


# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    exclude = ('create_time', 'update_time', 'delete_time')
    list_per_page = 12


@admin.register(FileUpload)
class FileUploadAdmin(BaseAdmin):
    list_display = ['id', 'file_name', 'file_cover', 'file_size', 'create_time']
