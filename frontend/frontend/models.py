from django.db import models

# Create your models here.
class rsvps(models.Model):
    # ... (your existing model fields)

    @staticmethod
    def get_all_rsvps():
        return rsvps.query.all()
