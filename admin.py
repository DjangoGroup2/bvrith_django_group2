from django.contrib import admin

# Register your models here.

from .models import TPO_Venue
from .models import TPO_Org
from .models import Student

admin.site.register(TPO_Venue)
admin.site.register(TPO_Org)
admin.site.register(Student)
