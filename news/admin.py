from django.contrib import admin
from news.models import News
from modeltranslation.admin import TranslationAdmin


class NewsTranslator(TranslationAdmin):
    pass


admin.site.register(News, NewsTranslator)
