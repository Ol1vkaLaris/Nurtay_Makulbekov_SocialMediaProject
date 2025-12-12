from django.contrib import admin
from .models import Post, PostAttachments, Comments
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

# admin.site.register(Post)
# admin.site.register(PostAttachments)
# admin.site.register(Comments)

@admin.register(Post)
class CustomPostAdmin(TranslationAdmin):
    fieldsets = (
        (_('Автор'), {'fields' : ('author',)}),
        (_('Основная информация поста (Русский)'), {'fields' : ('title_ru', 'content_ru')}),
        (_('Основная информация поста (Английский)'), {'fields' : ('title_en', 'content_en')}),
        (_('Доп. информация поста'), {'fields' : ('likes', 'time_stamp', 'edited')}),
    )
    add_fieldsets = (
        (_('Автор'), {'fields' : ('author',)}),
        (_('Основная информация поста (Русский)'), {'fields' : ('title_ru', 'content_ru')}),
        (_('Основная информация поста (Английский)'), {'fields' : ('title_en', 'content_en')}),
    )

    list_display = ('title', 'time_stamp', 'edited')
    search_fields = ('title', 'content')
    ordering = ('-time_stamp',)
    filter_horizontal = ('likes',)

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets
    
@admin.register(PostAttachments)
class CustomPostAttachmentsAdmin(admin.ModelAdmin):
    fieldsets = (
         (('Пост'), {'fields' : ('post',)}),
         (('основная информация картинки'), {'fields' : ('name', 'file')}),
    )

    add_fieldsets = (
         (('Пост'), {'fields' : ('post',)}),
         (('основная информация картинки'), {'fields' : ('file',)}),
    )
    list_display = ('name', 'file',)
    


    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets
    
@admin.register(Comments)
class CustomCommentsAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Информация об авторе'), {'fields' : ('author',)}),
        (('Основная информация комментария'), {'fields' : ('post', 'content',)}),
        (('Доп. информация комментария'), {'fields' : ('time_stamp', 'edited', 'pinned',)}),
    )
    add_fieldsets = (
        (('Информация об авторе'), {'fields' : ('author',)}),
         (('Основная информация комментария'), {'fields' : ('post', 'content',)}),
    )
    
    list_display = ('post', 'author', 'time_stamp', 'content')
    search_fields = ('content',)

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets

# crud structure 