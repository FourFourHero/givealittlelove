import logging

from django.contrib.admin.views.decorators import staff_member_required
import givealittlelove.gall.api.activation as activation_api

from givealittlelove.gall.views.response import *

logger = logging.getLogger(__name__)

#@staff_member_required
def show(request, template_name):
    response_dict = success_dict()
    return render_template(request, response_dict, 'gall/site/' + template_name)

def home(request):
    activations = activation_api.get_last_activations(amount=5)
    response_dict = success_dict()
    response_dict['activations'] = activations
    return render_template(request, response_dict, 'gall/site/home.html')

