import logging

from django.db import models
from givealittlelove.gall.models.basemodel import BaseModel

class ActivationManager(models.Manager):
    pass

class Activation(BaseModel):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    code = models.CharField(max_length=6)
    coupon_id = models.IntegerField(default=-1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = ActivationManager()

    class Meta:
        db_table = 'gall_activation'
        app_label = 'gall'

    def __unicode__(self):
        return self.name + ':' + str(self.id)

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['name'] = self.name
        json['email'] = self.email
        json['code'] = self.code
        json['coupon_id'] = self.coupon_id
        return json