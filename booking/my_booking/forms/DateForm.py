from datetime import datetime

from django import forms

yesterday = datetime.today()
min_day_value = yesterday.strftime('%Y-%m-%d')


class DateForm(forms.Form):
    start_date = forms.DateField(label='Дата заезда', widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
               'min': min_day_value, 'name': 'Дата заезда'})
    )
    end_date = forms.CharField(label='Дата выезда', widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
               'min': min_day_value, 'name': 'Дата выезда'})
    )