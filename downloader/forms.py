from django import forms
from .models import Link
from django.utils.translation import ugettext_lazy as _


class LinkDown(forms.ModelForm):

    class Meta:

        model = Link
        fields = ('url',)
        labels = {
            'url': _(''),
        }
