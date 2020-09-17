from django.db import models

# Create your models here.

class Message(models.Model):
    """Represent a Test row in our system"""

    id = models.CharField(max_length=11, primary_key=True)
    message = models.CharField(max_length=10)

    class Meta:
         db_table = "message"

    def __str__(self):
        """Django use this when it needs to convert the object to a string"""

        return self.id
