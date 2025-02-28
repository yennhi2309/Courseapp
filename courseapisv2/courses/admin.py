from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import path, include

from courses.models import Category, Course, Lesson, Tag

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class MyLessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'created_date']
    search_fields = ['subject']
    list_editable = ['subject']
    readonly_fields = ['image_view']
    form = LessonForm

    def image_view(self, lesson):
        if lesson:
            return mark_safe(f"<img src='/static/{lesson.image.name}' width='200 />")

    class Media:
        css = {
            'all': ('/static/css/styles.css', )
        }


class MyAdminSite(admin.AdminSite):
    site_header = 'OUeCourse Online'

    def get_urls(self):
        return [path('', include('courses.urls'))] + super().get_urls()

admin_site = MyAdminSite(name='eCourse')


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, MyLessonAdmin)
admin.site.register(Tag)


