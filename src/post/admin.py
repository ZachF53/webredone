from django.contrib import admin

# Register your models here.
from .models import Portfolio, Services, Additional

admin.site.register(Portfolio)
admin.site.register(Services)
admin.site.register(Additional)
