from django import forms

from .models import Join


class JoinForm(forms.ModelForm):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'placeholder': "Your Email",
                'class': 'form-control'
            }
        ))

    class Meta:
        model = Join
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = Join.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already exists")
        return email
