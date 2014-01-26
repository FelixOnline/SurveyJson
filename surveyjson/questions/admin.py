from django.contrib import admin
from questions.models import Option, Dependency, Question


class OptionInline(admin.TabularInline):
    model=Option

class DependInline(admin.StackedInline):
    model=Dependency

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
            OptionInline,
            DependInline,
    ]

admin.site.register(Option)
admin.site.register(Dependency)
admin.site.register(Question, QuestionAdmin)
