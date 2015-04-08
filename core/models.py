from django.db import models
from django.contrib.auth.models import User

class PDPlan(models.Model):
    user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", blank=True, null=True)

    supervisor = models.ForeignKey(User, null=True, related_name="supervisor")
    peers = models.ManyToManyField(User, null=True, related_name="peer")

    def __unicode__(self):
        return self.name


class ActionItem(models.Model):
    plan = models.ForeignKey(PDPlan)

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

