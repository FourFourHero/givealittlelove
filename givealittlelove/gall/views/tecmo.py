import logging
import random

from django.contrib.admin.views.decorators import staff_member_required
import givealittlelove.gall.api.activation as activation_api

from givealittlelove.gall.views.response import *

logger = logging.getLogger(__name__)

import random

def roll_team(not_team=-1):
    roll = random.randint(1,28)

    while roll == not_team:
        roll = random.randint(1,28)

    return roll

#@staff_member_required
def vs(request, template_name):
    response_dict = success_dict()
    return render_template(request, response_dict, 'gall/site/' + template_name)

def home(request):
    team1 = roll_team()
    team2 = roll_team(not_team=team1)
    response_dict = success_dict()
    response_dict['team1'] = team1
    response_dict['team2'] = team2
    return render_template(request, response_dict, 'gall/site/tecmo.html')

