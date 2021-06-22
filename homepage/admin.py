from django.contrib import admin
from .models import experience, education, publication, extracurricular
# Register your models here.

admin.site.register(experience)
admin.site.register(education)
admin.site.register(publication)
admin.site.register(extracurricular)