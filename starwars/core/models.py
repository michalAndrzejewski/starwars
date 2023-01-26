from django.db import models


class Metadata(models.Model):
    filename = models.CharField(max_length=255)
    download_date = models.DateTimeField()

    def __str__(self):
        return self.filename
