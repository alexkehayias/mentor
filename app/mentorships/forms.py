from django import forms

from mentorships.models import MentorshipRequest, MentorshipLog

class MentorRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MentorRequestForm, self).__init__(*args, **kwargs)
        self.fields['so_far'].label = "What work have you done so far to learn this skill?"
        self.fields['why'].label = "Why do you want to learn? What will you do with it?"
        self.fields['learning'].label = "What are you learning?"
    
    class Meta:
        model = MentorshipRequest
        exclude = ('from_user', 'closed')

class MentorshipLogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MentorshipLogForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""
    class Meta:
        model = MentorshipLog
        exclude = ('added_by', 'mentorship')
