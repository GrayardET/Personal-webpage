from django import forms


class CommentView(forms.Form):
    content = forms.Textarea()
