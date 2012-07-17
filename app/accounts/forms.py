from django import forms
from django.contrib.auth import login, authenticate

from accounts.models import Sponsor, P2PUProfile

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())

    def authenticate(self, request):
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return True
            else:
                return False
        else:
            return False

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        exclude = ('mentorship_request', )
        widgets = {
            'email': forms.widgets.TextInput(
                attrs = {
                    'placeholder':'Enter you email address.'}),
            }

class MentorProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MentorProfileForm, self).__init__(*args, **kwargs)
        self.fields['skills'].help_text = "Start typing the name of a skill then press tab to add it to the list."
    class Meta:
        model = P2PUProfile
        exclude = ('user', 'p2pu_id', 'picture')        
