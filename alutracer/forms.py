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

RELATED_JOB = (
    ('Yes', 'Yes'),
    ('No', 'No')
)

PLACE_WORK = (
    ('Local', 'Local'),
    ('Abroad', 'Abroad')
)

JOB_STATUS = (
    ('Permanent', 'Permanent'),
    ('Contractual', 'Contractual'),
    ('Casual', 'Casual')
)

class PersonalInformationForm(forms.ModelForm):
    type_of_organization        = forms.ChoiceField(choices=ORGANIZATION_TYPE, widget=forms.RadioSelect())
    related_job                 = forms.ChoiceField(choices=RELATED_JOB, widget=forms.RadioSelect())
    place_of_work               = forms.ChoiceField(choices=PLACE_WORK, widget=forms.RadioSelect())
    finish_graduate_degree      = forms.ChoiceField(choices=RELATED_JOB, widget=forms.RadioSelect())
    job_status                  = forms.ChoiceField(choices=JOB_STATUS, widget=forms.RadioSelect())
    persuing_degree_ndmc        = forms.ChoiceField(choices=RELATED_JOB, widget=forms.RadioSelect())
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
            'address',
            'country',
            'social_media_account',
            'mobile_number',
            'course',
            'date_graduated',
            'organization_or_employer',
            'address_organization_or_employer',
            'type_of_organization',
            'related_job',
            'number_year_company',
            'place_of_work',
            'finish_graduate_degree',
            'reason_staying_job',
            'designation',
            'department_division',
            'job_status',
            'monthly_range_income',
            'persuing_degree_ndmc',
            'obtaining_degree_ndmc',
            'advertisement_media',
            'nature_of_employment',
            'number_of_years',
            'monthly_income',
            'case_of_unemployed',
            'persuing_futher_studies',
            'not_persuing_futher_studies'
        ]