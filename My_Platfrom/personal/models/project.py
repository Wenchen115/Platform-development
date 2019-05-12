from django.db import models

# Create your models here.


class Project(models.Model):
    """
    项目表
    """
    name = models.CharField(max_length=50, null=False)  # 长度50，默认不为空
    describe = models.TextField(default="")
    status = models.BooleanField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)  # 默认为取当前时间

