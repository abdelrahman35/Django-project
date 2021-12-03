from django import forms
from django.db.models import fields
from .models import Projects, Projectcomments

class ProjectAddForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'project_details', 'total_target','total_donations','avg_rate', 'start_date', 'end_date', 'tag', 'category']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Projectcomments
        fields = ['comment', 'project_id']
