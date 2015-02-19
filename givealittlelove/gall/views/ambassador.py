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

    ambassador = ambassador_api.create_ambassador(name, email)

    mail_api.send_ambassador_welcome_mail(ambassador)

    # return response
    response_dict = success_dict()
    response_dict['ambassador'] = ambassador
    return render_json(request, response_dict)