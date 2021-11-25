from django import forms
from backend import models
# from solarpvsite.backend.models import Client


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = "__all__"


class CertificateForm(forms.ModelForm):
    class Meta:
        model = models.Certificate
        fields = "__all__"


class LocationForm(forms.ModelForm):
    class Meta:
        model = models.Location
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Location
        fields = "__all__"


class TestStandardForm(forms.ModelForm):
    class Meta:
        model = models.Teststandard
        fields = "__all__"
