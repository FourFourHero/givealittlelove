import logging

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.mail import send_mail

from givealittlelove.gall.views.response import *
import givealittlelove.gall.api.ambassador as ambassador_api
import givealittlelove.gall.api.activation as activation_api
import givealittlelove.gall.api.coupon as coupon_api

logger = logging.getLogger(__name__)

@require_POST
@csrf_exempt
def create(request):
    name = get_request_var(request, 'name')
    email = get_request_var(request, 'email')
    code = get_request_var(request, 'code')

    if not name:
        response_dict = error_dict()
        response_dict['error_code'] = 100
        response_dict['error_msg'] = 'Missing name param'
        return render_json(request, response_dict)

    if not email:
        response_dict = error_dict()
        response_dict['error_code'] = 200
        response_dict['error_msg'] = 'Missing email param'
        return render_json(request, response_dict)

    if not code:
        response_dict = error_dict()
        response_dict['error_code'] = 300
        response_dict['error_msg'] = 'Missing code param'
        return render_json(request, response_dict)

    ambassador = ambassador_api.get_ambassador_by_code(code)
    if not ambassador:
        response_dict = error_dict()
        response_dict['error_code'] = 400
        response_dict['error_msg'] = 'Invalid code'
        return render_json(request, response_dict)

    activation = activation_api.create_activation(name, email, code)


    activations = activation_api.get_activations_by_code(code)
    if len(activations) == 5:
        self._send_coupons(activations)

    # return response
    response_dict = success_dict()
    response_dict['ambassador'] = ambassador
    response_dict['activation'] = activation
    return render_json(request, response_dict)

@require_POST
@csrf_exempt
def get_by_code(request):
    code = get_request_var(request, 'code')

    if not code:
        response_dict = error_dict()
        response_dict['error_code'] = 100
        response_dict['error_msg'] = 'Missing code param'
        return render_json(request, response_dict)

    ambassador = ambassador_api.get_ambassador_by_code(code)
    if not ambassador:
        response_dict = error_dict()
        response_dict['error_code'] = 200
        response_dict['error_msg'] = 'Invalid code'
        return render_json(request, response_dict)

    activations = activation_api.get_activations_by_code(code)

    # return response
    response_dict = success_dict()
    response_dict['ambassador'] = ambassador
    response_dict['activations'] = activations
    return render_json(request, response_dict)

@require_POST
@csrf_exempt
def test_mail(request):
    try:
        send_mail('GALL Test Mail', 'Here is the message.', 'aschulak@ag.com',
            ['aschulak@gmail.com'], fail_silently=False)
    except:
        logging.exception('mail tets failed')

    response_dict = success_dict()
    return render_json(request, response_dict)

###
### PRIVATE
###

def _send_coupons(activations):
    coupons = coupon_api.get_unsent_coupons(amount=len(activations))
    for activation in activations:
        coupon.activation_id = activation.id
        coupon.sent = True
        coupon_api.update_coupon(coupon)

        #send_mail('Subject here', 'Here is the message.', 'from@example.com',
        #    ['to@example.com'], fail_silently=False)
