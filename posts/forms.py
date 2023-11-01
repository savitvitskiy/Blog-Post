from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"placeholder": "Your Name"}
        )
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Leave a comment.", "rows": 2}
        )
    )