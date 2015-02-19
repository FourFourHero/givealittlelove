import logging

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from givealittlelove.gall.views.response import *
import givealittlelove.gall.api.ambassador as ambassador_api
import givealittlelove.gall.api.activation as activation_api

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

    # return response
    response_dict = success_dict()
    response_dict['ambassador'] = ambassador
    response_dict['activation'] = activation
    return render_json(request, response_dict)