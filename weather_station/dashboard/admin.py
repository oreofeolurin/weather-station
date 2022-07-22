from django.contrib import admin
from .models import dashboard


class dashboard_Admin(admin.ModelAdmin):
    list_display =('temperature','Humidity','pressure','altitude', 'lightInt', 'lastUpdated')
    # search_fields = ('lastUpdated')
    # list_filter = ('lastUpdated')
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = False

admin.site.register(dashboard, dashboard_Admin)
