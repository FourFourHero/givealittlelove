import logging

from django.db import models
from givealittlelove.gall.models.basemodel import BaseModel

class AmbassadorManager(models.Manager):
    pass

class Ambassador(BaseModel):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True, max_length=254)
    code = models.CharField(unique=True, max_length=6)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = AmbassadorManager()

    class Meta:
        db_table = 'gall_ambassador'
        app_label = 'gall'

    def __unicode__(self):
        return self.name + ':' + str(self.id)

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['name'] = self.name
        json['email'] = self.email
        json['code'] = self.code
        return json

