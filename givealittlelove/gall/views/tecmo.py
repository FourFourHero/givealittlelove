import logging
import random

from givealittlelove.gall.views.response import *

logger = logging.getLogger(__name__)

import random

def roll_team(not_team=-1):
    roll = random.randint(1,28)

    while roll == not_team:
        roll = random.randint(1,28)

    return roll

def vs(request):
    logging.warn('vs')
    team1 = roll_team()
    team2 = roll_team(not_team=team1)
    response_dict = success_dict()
    response_dict['team1'] = team1
    response_dict['team2'] = team2
    return render_template(request, response_dict, 'gall/site/tecmo_vs.html')

def home(request):
    logging.warn('home')
    response_dict = success_dict()
    return render_template(request, response_dict, 'gall/site/tecmo.html')