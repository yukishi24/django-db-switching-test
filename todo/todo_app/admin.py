from django.contrib import admin
from .models import User, Task

# Userモデルの管理画面
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)

# Taskモデルの管理画面
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'due_date', 'created_at')
    list_filter = ('completed', 'user')  # フィルター機能
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
