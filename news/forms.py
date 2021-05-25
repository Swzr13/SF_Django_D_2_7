from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['autor', 'type_post', 'title', 'category', 'text']