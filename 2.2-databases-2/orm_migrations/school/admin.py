from django.contrib import admin

from .models import Student, Teacher, Relationship

class RelationshipInline(admin.TabularInline):
    model = Relationship


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [RelationshipInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
