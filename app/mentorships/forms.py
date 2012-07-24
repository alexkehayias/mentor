from django import forms

from mentorships.models import JoinRequest, Project, ProjectLog

class JoinRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JoinRequestForm, self).__init__(*args, **kwargs)
        self.fields['note'].label = "Write them a note about why you're interested"
    
    class Meta:
        model = JoinRequest
        exclude = ('added_by', 'closed', 'project')

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['skills'].help_text = "Start typing a skill and hit the tab key."
        self.fields['project_type'].help_text = "Select whether you are looking for a mentor or want to mentor someone."
    
    class Meta:
        model = Project
        fields = (
                'project_type',
                'description', 
                'title', 
                'skills', 
                'looking_for'
            )
        exclude = ('added_by', 'members')

class ProjectLogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectLogForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""
    class Meta:
        model = ProjectLog
        exclude = ('added_by', 'project')
