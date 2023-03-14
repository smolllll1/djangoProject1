from django import forms
from .models import Reservation
from datetime import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'visit_datetime', 'quests', 'message')

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                                         'id': "resName",
                                                                         'type': "text",
                                                                         'name': "res_name",
                                                                         'required': "",
                                                                         }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                           'id': "resEmail",
                                                           'type': "email",
                                                           'name': "res_email",
                                                           'required': "",
                                                           }))
    phone = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                                         'id': "resNumber",
                                                                         'type': "number",
                                                                         'name': "res_number",
                                                                         'required': "",
                                                                         }))
    visit_datetime = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M'], widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                             'id': "resDate",
                                                             'type': "text",
                                                             'name': "res_date",
                                                             'required': "",
                                                             }))
    quests = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                                 'id': "resPeople",
                                                                 'type': "number",
                                                                 "name": "res_people",
                                                                 'required': "",
                                                                 }))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                                            'id': "request",
                                                                            'rows': "7",
                                                                            'name': "res_request",
                                                                            'required': "",
                                                                            }))
