from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('title',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    search_fields = ['question_text']
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)