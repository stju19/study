from django.contrib import admin
from report_show.models import EC
class EClistAdmin(admin.ModelAdmin):
    list_display = ('number', 'product', 'state', 'theme', 'change_big_type', 'change_small_type', 'submit_date')


admin.site.register(EC, EClistAdmin)

# Register your models here.
