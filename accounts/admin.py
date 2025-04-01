from django.contrib import admin

from accounts.models import User

# Register your models here.

# dev_9
# 기본적인 관리자 페이지에서
admin.site.register(User)
