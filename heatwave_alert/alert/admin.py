from django.contrib import admin
from .models import Subscriber
from django.http import HttpResponse
from .views import check_heat_wave

class SubscriberAdmin(admin.ModelAdmin):
    actions = ['trigger_heat_wave_alerts']

    def trigger_heat_wave_alerts(self, request, queryset):
        response = check_heat_wave(request)
        self.message_user(request, "Heat wave alerts have been sent.")
        return response

    trigger_heat_wave_alerts.short_description = "Trigger heat wave alerts for selected subscribers"

admin.site.register(Subscriber, SubscriberAdmin)
