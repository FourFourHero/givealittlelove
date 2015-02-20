import logging

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from givealittlelove.gall.views.response import *
import givealittlelove.gall.api.ambassador as ambassador_api
import givealittlelove.gall.api.mail as mail_api

logger = logging.getLogger(__name__)

@require_POST
@csrf_exempt
def create(request):
    name = get_request_var(request, 'name')
    email = get_request_var(request, 'email')
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

    ambassador = ambassador_api.create_ambassador(name, email)

    mail_api.send_ambassador_welcome_mail(ambassador)

    # return response
    response_dict = success_dict()
    response_dict['ambassador'] = ambassador
    if not origin:
        return render_json(request, response_dict)
    else:
        return render_template(request, response_dict, 'gall/site/ambassador_success.html')

@require_POST
@csrf_exempt
def passthru(request):
    password = get_request_var(request, 'password')

    if not password:
        response_dict = error_dict()
        response_dict['error_code'] = 100
        response_dict['error_msg'] = 'Missing password param'
        return render_template(request, response_dict, 'gall/site/error.html')

    if password != 'iloveteambanzai':
        response_dict = error_dict()
        response_dict['error_code'] = 200
        response_dict['error_msg'] = 'Incorrect password'
        return render_template(request, response_dict, 'gall/site/error.html')

    # return response
    response_dict = success_dict()
    return render_template(request, response_dict, 'gall/site/ambassador_signup.html')