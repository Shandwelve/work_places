from django.db import models


class JobOffer(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
