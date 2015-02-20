import logging

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from givealittlelove.gall.views.response import *
import givealittlelove.gall.api.ambassador as ambassador_api
import givealittlelove.gall.api.activation as activation_api
import givealittlelove.gall.api.coupon as coupon_api
import givealittlelove.gall.api.mail as mail_api

logger = logging.getLogger(__name__)

@require_POST
@csrf_exempt
def create(request):
    name = get_request_var(request, 'name')
    email = get_request_var(request, 'email')
    code = get_request_var(request, 'code')
    origin = get_request_var(request, 'origin')

    if not name:
        response_dict = error_dict()
        response_dict['error_code'] = 100
        response_dict['error_msg'] = 'Missing name param'
        if not origin:
            return render_json(request, response_dict)
        else:
            return render_template(request, response_dict, 'gall/site/error.html')

    if not email:
        response_dict = error_dict()
        response_dict['error_code'] = 200
        response_dict['error_msg'] = 'Missing email param'
        if not origin:
            return render_json(request, response_dict)
        else:
            return render_template(request, response_dict, 'gall/site/error.html')

    if not code:
        response_dict = error_dict()
        response_dict['error_code'] = 300
        response_dict['error_msg'] = 'Missing code param'
        if not origin:
            return render_json(request, response_dict)
        else:
            return render_template(request, response_dict, 'gall/site/error.html')


    ambassador = ambassador_api.get_ambassador_by_code(code)
    if not ambassador:
        response_dict = error_dict()
        response_dict['error_code'] = 400
        response_dict['error_msg'] = 'Invalid code'
        if not origin:
            return render_json(request, response_dict)
        else:
            return render_template(request, response_dict, 'gall/site/error.html')

    activations = activation_api.get_activations_by_code(code)
    #for activation in activations:
    #    if email.lower() == activation.email.lower():
    #        response_dict = error_dict()
    #        response_dict['error_code'] = 500
    #        response_dict['error_msg'] = 'Already redeemed'
    #        if not origin:
    #            return render_json(request, response_dict)
    #        else:
    #            return render_template(request, response_dict, 'gall/site/error.html')

    last_activation = activation_api.get_last_activation_by_code(code)
    activation = activation_api.create_activation(name, email, code)

    if last_activation:
        _send_coupon(ambassador, last_activation, activation)

    # return response
    response_dict = success_dict()
    response_dict['ambassador'] = ambassador
    response_dict['last_activation'] = last_activation
    response_dict['activation'] = activation
    response_dict['activations'] = activations
    if not origin:
        return render_json(request, response_dict)
    else:
        return render_template(request, response_dict, 'gall/site/received_a_card_success.html')

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
        mail_api.send_test_mail()
    except:
        logging.exception('mail test failed')

    response_dict = success_dict()
    return render_json(request, response_dict)

###
### PRIVATE
###

def _send_coupon(ambassador, last_activation, activation):
    coupon = coupon_api.get_unsent_coupon()
    mail_api.send_coupon_mail(ambassador, last_activation, activation, coupon)
    last_activation.coupon_id = coupon.id
    activation_api.update_activation(last_activation)
    coupon.activation_id = activation.id
    coupon.sent = True
    coupon_api.update_coupon(coupon)