from django.db import models

# 每次更改完执行
# python manage.py makemigrations
# python manage.py migrate


class Login(models.Model):
    account = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

# 增
# Login.objects.create(account="123456", password="6666")
# 删
# Login.objects.filter(id=5).delete()
# 查
# data = Login.objects.filter(id=6)
# for obj in data:
#     print(obj.id, obj.account, obj.password)
# 改
# Login.objects.filter(id=6).update(password="9999")
