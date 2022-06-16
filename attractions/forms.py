from django import forms
from attractions.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }


