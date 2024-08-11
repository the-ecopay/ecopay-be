from django.contrib import admin
from pickup_request.models import PickupRequest,PickupRequestItem

admin.site.register(PickupRequest)
admin.site.register(PickupRequestItem)