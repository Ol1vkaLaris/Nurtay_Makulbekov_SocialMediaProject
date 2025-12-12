from modeltranslation.translator import register, TranslationOptions 
from .models import Post, Comments

@register(Post)
class PostTranslation(TranslationOptions):
    fields = ('title', 'content')

@register(Comments)
class CommentTransaltion(TranslationOptions):
    fields = ('content',)