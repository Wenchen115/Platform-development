from django.db import models
from project_app.models import Project


class Module(models.Model):
    """
    模块表
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=50, null=False)  # 长度50，默认不为空
    describe = models.TextField("描述", default="")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)  # 默认为取当前时间

    def __str__(self):
        return self.name
