from django.contrib import admin

from .models import Attachment, TaskList, Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on')


admin.site.register(Task, TaskAdmin)


class TaskListAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on')


admin.site.register(TaskList, TaskListAdmin)


class AttachmentAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on')


admin.site.register(Attachment, AttachmentAdmin)
