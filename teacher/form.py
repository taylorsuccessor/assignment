from django import forms
from teacher.models import get_upload_path


class SearchForm(forms.Form):

    search_text = forms.CharField(label='',
                                  max_length=100,
                                  required=None,
                                  widget=forms.TextInput(attrs={
                                      'placeholder': 'Search,first,last,subjects taught'
                                  }))

class UploadTeacherForm(forms.Form):
    teacher_list_csv = forms.FileField(label='Upload Your teacher List',required=None )
