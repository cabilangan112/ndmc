from django import forms
from django.contrib.auth import get_user_model
from .models import Course, Index, Thumbnail, Parallax, PersonalInformation

User = get_user_model()

# ORGANIZATION_TYPE = (
#     ('Private', 'Private'),
#     ('Public', 'Public'),
#     ('NGO', 'NGO'),
#     ('Non-Profit', 'Non-Profit')
# )

# RELATED_JOB = (
#     ('Yes', 'Yes'),
#     ('No', 'No')
# )

# PLACE_WORK = (
#     ('Local', 'Local'),
#     ('Abroad', 'Abroad')
# )

# JOB_STATUS = (
#     ('Permanent', 'Permanent'),
#     ('Contractual', 'Contractual'),
#     ('Casual', 'Casual')
# )

class PersonalInformationForm(forms.ModelForm):
    # type_of_organization        = forms.ChoiceField(choices=ORGANIZATION_TYPE, widget=forms.RadioSelect())
    # related_job                 = forms.ChoiceField(choices=RELATED_JOB, widget=forms.RadioSelect())
    # place_of_work               = forms.ChoiceField(choices=PLACE_WORK, widget=forms.RadioSelect())
    # finish_graduate_degree      = forms.ChoiceField(choices=RELATED_JOB, widget=forms.RadioSelect())
    # job_status                  = forms.ChoiceField(choices=JOB_STATUS, widget=forms.RadioSelect())
    # persuing_degree_ndmc        = forms.ChoiceField(choices=RELATED_JOB, widget=forms.RadioSelect())
    class Meta:
        model = PersonalInformation
        fields = [
            'last_name',
            'first_name',
            'middle_name',
            'gender',
            'date_of_birth',
            'civil_status',
            'email',
            'mobile_number',
            'course',
        ]