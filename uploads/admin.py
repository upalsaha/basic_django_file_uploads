from django.contrib import admin

# Register your models here.

from .models import ModelWithFileField

admin.site.register(ModelWithFileField)