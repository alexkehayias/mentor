from django import forms
from django.contrib.auth import login, authenticate

from accounts.models import P2PUProfile
from mentorships.models import Sponsor

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
        exclude = ('project', )
        widgets = {
            'email': forms.widgets.TextInput(
                attrs = {
                    'placeholder':'Enter you email address.'}),
            }

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['skills'].help_text = "Start typing the name of a skill then press tab to add it to the list."
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = P2PUProfile
        exclude = ('user', 'p2pu_id', 'picture')

    def save(self):
        profile = super(ProfileForm, self).save()
        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        


