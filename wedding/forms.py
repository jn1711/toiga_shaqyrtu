from django import forms

from .models import RSVPResponse, Wish


class RSVPForm(forms.ModelForm):
    attendance = forms.ChoiceField(
        choices=RSVPResponse.Attendance.choices,
        widget=forms.RadioSelect,
        label='Қатысуым',
    )

    class Meta:
        model = RSVPResponse
        fields = ['full_name', 'attendance']
        labels = {
            'full_name': 'Аты-жөні',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Аты-жөніңіз'}),
        }


class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['name', 'message']
        labels = {
            'name': 'Атыңыз',
            'message': 'Тілегіңіз',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Атыңыз'}),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ізгі тілегіңізді жазыңыз...'}),
        }
