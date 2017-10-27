import logging

import uuid
from givealittlelove.gall.models import Coupon

logger = logging.getLogger(__name__)

def create_coupon(code):
    coupon = Coupon()
    coupon.code = code
    coupon.save()
    return coupon

def update_coupon(coupon):
    coupon.save()
    return coupon

def get_coupon(coupon_id):
    coupon = None
    try:
        coupon = Coupon.objects.get(pk=coupon_id)
    except:
        pass
    return coupon

def get_coupon_by_code(code):
    coupon = None
    try:
        coupon = Coupon.objects.get(code=code)
    except:
        pass
    return coupon

def get_unsent_coupons(amount=None):
    coupons = Coupon.objects.filter(sent=False).order_by('created')
    if amount:
        coupons = coupons[:amount]
    return list(coupons)

def get_unsent_coupon():
    return get_unsent_coupons(amount=1)[0]

