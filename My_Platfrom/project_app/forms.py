from django import forms
from project_app.models import Project


class ProjectForm(forms.Form):

    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']