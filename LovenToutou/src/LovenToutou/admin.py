from django.contrib import admin

from .models import Dog
from .models import Owner

admin.site.register(Dog)
admin.site.register(Owner)
# Register your models here.
