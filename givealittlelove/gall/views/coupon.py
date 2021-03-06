import logging

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from givealittlelove.gall.views.response import *
import givealittlelove.gall.api.coupon as coupon_api

logger = logging.getLogger(__name__)

@require_POST
@csrf_exempt
def create(request):
    codes = get_request_var(request, 'codes')

    if not codes:
        response_dict = error_dict()
        response_dict['error_code'] = 100
        response_dict['error_msg'] = 'Missing codes param'
        return render_json(request, response_dict)

    #codes = codes.split(',')
    codes = [s.strip() for s in codes.splitlines()]

    coupons = []
    for code in codes:
        coupon = coupon_api.create_coupon(code)
        coupons.append(coupon)

    # return response
    response_dict = success_dict()
    response_dict['coupons'] = coupons
    return render_json(request, response_dict)

@csrf_exempt
def get_unsent(request):
    amount = get_request_var(request, 'amount')

    try:
        amount = int(amount)
    except:
        amount = None

    coupons = coupon_api.get_unsent_coupons(amount=amount)
    # return response
    response_dict = success_dict()
    response_dict['coupons'] = coupons
    return render_json(request, response_dict)