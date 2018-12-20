from django import forms
from django.contrib.auth import get_user_model
from .models import Course, Index, Thumbnail, Parallax, PersonalInformation

User = get_user_model()

ORGANIZATION_TYPE = (
    ('Private', 'Private'),
    ('Public', 'Public'),
    ('NGO', 'NGO'),
    ('Non-Profit', 'Non-Profit')
)

class PersonalInformationForm(forms.ModelForm):
    type_of_organization = forms.ChoiceField(choices=ORGANIZATION_TYPE, widget=forms.RadioSelect())
    class Meta:
        model = PersonalInformation
        fields = [
            'last_name',
            'first_name',
            'middle_name',
            'gender',
            'date_of_birth',
            'civil_status',
            # 'age',
            'email',
            'address',
            'country',
            'social_media_account',
            'mobile_number',
            'course',
            'date_graduated',
            'organization_or_employer',
            'address_organization_or_employer',
            'type_of_organization'
        ]