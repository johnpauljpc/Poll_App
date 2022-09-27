from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class Qadmin(admin.ModelAdmin):
	fieldsets = [
        ('Question',             {'fields': ['question_text']}),
        

    ]
admin.site.register(Question, Qadmin)
admin.site.register(Choice )