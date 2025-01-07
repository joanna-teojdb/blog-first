from django import forms
from .models import Post, Category
from django.core.exceptions import ValidationError

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","content","category"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        forbidden_words = ["php", "!bin/bash", "eval()"]
        for word in forbidden_words:
            if word in title.lower():
                raise ValueError(f"Tytul zawiera zakazane slowo {word}")

        return title
    
    def clean_content(self):
        content = self.cleaned_data.get("content")
        forbidden_words = ["php", "!bin/bash", "eval()"]
        for word in forbidden_words:
            if word in content.lower():
                raise ValueError(f"Tytul zawiera zakazane slowo {word}")

        return content


class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name","description"]
    

