from django.contrib import admin
from tree.models import UserModel, CommitModel, IndexPackage, ResourceModel


# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    exclude = ('create_time', 'update_time', 'delete_time')


@admin.register(UserModel)
class UserAdmin(BaseAdmin):
    list_display = ['user_id', 'user_name', 'user_phone', 'enabled']
    list_filter = ['enabled', 'user_sex']
    search_fields = ['user_name', 'user_id']
    ordering = ['id']


@admin.register(CommitModel)
class CommitAdmin(BaseAdmin):
    list_filter = ['works', 'user']
    list_display = ['id', 'works', 'user', 'content', 'parent_id']
    ordering = ['id']


@admin.register(ResourceModel)
class ResourceAdmin(BaseAdmin):
    list_filter = ['resource_type', 'status']
    list_display = ['id', 'resource_name', 'resource_type', 'cover', 'status']
    search_fields = ['resource_name']
    ordering = ['id']


@admin.register(IndexPackage)
class IndexPackageAdmin(BaseAdmin):
    list_display = ['id', 'package_name', 'title', 'resource', 'cover', 'like_nums', 'collect_nums', ]
    search_fields = ['package_name']
    ordering = ['id']
