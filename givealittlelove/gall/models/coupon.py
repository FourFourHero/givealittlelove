import logging

from django.db import models
from givealittlelove.gall.models.basemodel import BaseModel

class CouponManager(models.Manager):
    pass

class Coupon(BaseModel):
    code = models.CharField(unique=True, max_length=17)
    sent = models.BooleanField(default=False)
    activation_id = models.IntegerField(default=-1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    objects = CouponManager()

    class Meta:
        db_table = 'gall_coupon'
        app_label = 'gall'

    def __unicode__(self):
        return self.code + ':' + str(self.id)

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['code'] = self.code
        json['sent'] = str(self.sent)
        json['activation_id'] = self.activation_id
        return json