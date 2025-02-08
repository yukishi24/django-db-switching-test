from django.db import models

# ユーザーモデルをカスタマイズして作成
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)  # ユーザー名（ユニーク）
    email = models.EmailField(unique=True)  # メールアドレス（ユニーク）
    password = models.CharField(max_length=255)  # パスワード（ハッシュ化されることを想定）
    created_at = models.DateTimeField(auto_now_add=True)  # アカウント作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 最終更新日時

    def __str__(self):
        return self.username


# タスクモデル
class Task(models.Model):
    title = models.CharField(max_length=255)  # タイトル
    description = models.TextField(blank=True, null=True)  # 詳細（任意）
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時（自動設定）
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時（自動設定）
    due_date = models.DateTimeField(blank=True, null=True)  # 締切日（任意）
    completed = models.BooleanField(default=False)  # 完了フラグ
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')  # タスクの所有者（ユーザー）

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # 作成日時の降順で並べる
