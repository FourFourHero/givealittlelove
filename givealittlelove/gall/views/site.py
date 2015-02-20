import logging

from django.contrib.admin.views.decorators import staff_member_required

from givealittlelove.gall.views.response import *

logger = logging.getLogger(__name__)

#@staff_member_required
def show(request, template_name):
    response_dict = success_dict()
    return render_template(request, response_dict, 'gall/site/' + template_name)

