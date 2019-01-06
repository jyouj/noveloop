from django import forms
from .models import Novel

# Chap.2-5
class NewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'label': 'タイトル', 'placeholder': '100文字までだよ！', 'class': 'input is-medium is-hovered'}
        self.fields['text'].widget.attrs = {'label': '本文', 'placeholder': '500字まで！', 'class': 'textarea'}

    class Meta:
        model = Novel
        fields = ('title', 'text',)
