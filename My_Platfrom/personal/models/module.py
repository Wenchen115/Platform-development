from django.db import models
from personal.models.project import Project


class Module(models.Model):
    """
    模块表
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)  # 长度50，默认不为空
    describe = models.TextField(default="")
    status = models.BooleanField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)  # 默认为取当前时间
