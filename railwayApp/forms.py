from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from.models import Reservation

class ReservationForm (forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name', 'status', 'gender', 'Journey', 'no_of_person']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'submit'))