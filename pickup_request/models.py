from django.db import models
from django.contrib.auth.models import User

class PickupRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)
    scheduled_pickup_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return f"Pickup Request {self.id} by {self.user.username}"


class PickupRequestItem(models.Model):
    pickup_request = models.ForeignKey(PickupRequest, related_name='items', on_delete=models.CASCADE)
    recognized_item = models.ForeignKey('gemini_ai.RecognizedItem', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Item {self.recognized_item.item_name} for Pickup Request {self.pickup_request.id}"