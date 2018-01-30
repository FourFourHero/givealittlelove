import logging
import random

from django.http import JsonResponse
from givealittlelove.gall.views.response import *

logger = logging.getLogger(__name__)

###
### CONTROLLER
###

def vs_tomczak(request):
    logger.warn('vs_tomczak')
    teams, tiers = _setup_teams_tomczak()
    return _vs(request, teams, tiers, 'Tomczak', '/vs/tomczak')

def vs_agi(request):
    logger.warn('vs_agi')
    teams, tiers = _setup_teams_agi()
    return _vs(request, teams, tiers, 'AGI', '/vs/agi')

def vs_random(request):
    logger.warn('vs_random')
    teams, tiers = _setup_teams_agi()
    return _vs_random(request, teams)

def _get_alexa_teams(request, teams):
    logger.info('_get_alexa_teams')
    team1 = _roll_team(teams)
    logger.info('t1 ' + str(team1.name))
    tiers = team1.tiers
    logger.info('team tiers ' + str(tiers))
    idx = random.randint(0,len(tiers)-1)
    logger.info('idx ' + str(idx))
    tier = team1.tiers[idx]
    logger.info('NEW tier: ' + str(tier))
    team2 = _roll_team(teams, tier=tier, not_team=team1.img_id)
    return tier, team1, team2

# called via Alexa skill
def vs_agi_json(request):
    logger.warn('vs_agi_json')

    min_tier = get_request_var(request, 'min_tier')
    logger.warn('min_tier: ' + str(min_tier))

    teams, tiers = _setup_teams_agi()

    tier, team1, team2 = _get_alexa_teams(request, teams)
    
    if min_tier:
        min_tier = int(min_tier)
        while tier > min_tier:
            tier, team1, team2 = _get_alexa_teams(request, teams)
            
    response_dict = success_dict()
    response_dict['tier'] = tier
    response_dict['team1'] = team1.name
    response_dict['team2'] = team2.name
    return JsonResponse(response_dict)

def home(request):
    logger.warn('home')
    response_dict = success_dict()
    return render_template(request, response_dict, 'gall/site/tecmo.html')

###
### PRIVATE
###

class Team(object):
    name = None
    id = -1
    tiers = []

    def __init__(self, name, img_id, tiers):
        self.name = name
        self.img_id = img_id
        self.tiers = tiers

# http://tecmotourney.blogspot.com/p/team-tiers.html
def _setup_teams_tomczak():
    logger.info('setup_teams_tomczak')
    teams = []

    team = Team('Oilers', 10, [1]) # oilers
    teams.append(team)
    team = Team('Giants', 13, [1]) # giants
    teams.append(team)
    team = Team('Bills', 25, [1]) # bills
    teams.append(team)
    team = Team('49ers', 28, [1]) # 49ers
    teams.append(team)

    team = Team('Raiders', 7, [1, 2]) # raiders
    teams.append(team)

    team = Team('Vikings', 1, [2]) # vikings
    teams.append(team)
    team = Team('Eagles', 15, [2]) # eagles
    teams.append(team)
    team = Team('Dolphins', 16, [2]) # dolphins
    teams.append(team)
    team = Team('Chiefs', 19, [2]) # chiefs
    teams.append(team)

    team = Team('Rams', 6, [2, 3]) # rams
    teams.append(team)
    team = Team('Bears', 27, [2, 3]) # bears
    teams.append(team)

    team = Team('Redskins', 5, [3]) # redskins
    teams.append(team)
    team = Team('Chargers', 20, [3]) # chargers
    teams.append(team)
    team = Team('Broncos', 24, [3]) # broncos
    teams.append(team)
    team = Team('Bengals', 26, [3]) # bengals
    teams.append(team)

    team = Team('Lions', 11, [3, 4]) # lions
    teams.append(team)
    team = Team('Falcons', 14, [3, 4]) # falcons
    teams.append(team)

    team = Team('Saints', 4, [4]) # saints
    teams.append(team)
    team = Team('Cowboys', 17, [4]) # cowboys
    teams.append(team)
    team = Team('Cardinals', 21, [4]) # cardinals
    teams.append(team)
    team = Team('Buccaneers', 22, [4]) # buccaneers
    teams.append(team)

    team = Team('Steelers', 2, [4, 5]) # steelers
    teams.append(team)
    team = Team('Jets', 12, [4, 5]) # jets
    teams.append(team)

    team = Team('Seahawks', 3, [5]) # seahawks
    teams.append(team)
    team = Team('Patriots', 8, [5]) # patriots
    teams.append(team)
    team = Team('Packers', 9, [5]) # packers
    teams.append(team)
    team = Team('Colts', 18, [5]) # colts
    teams.append(team)
    team = Team('Browns', 23, [5]) # browns
    teams.append(team)

    logger.info('teams size: ' + str(len(teams)))
    return teams, 5

# experimental AGI rankings
def _setup_teams_agi():
    logger.info('setup_teams_agi')
    teams = []

    # tier 1
    team = Team('49ers', 28, [1]) # 49ers
    teams.append(team)
    team = Team('Oilers', 10, [1]) # oilers
    teams.append(team)
    team = Team('Bills', 25, [1]) # bills
    teams.append(team)
    team = Team('Giants', 13, [1]) # giants
    teams.append(team)

    # tiers 1 & 2
    team = Team('Raiders', 7, [1, 2]) # raiders
    teams.append(team)

    # tier 2
    team = Team('Dolphins', 16, [2]) # dolphins
    teams.append(team)
    team = Team('Eagles', 15, [2]) # eagles
    teams.append(team)
    team = Team('Chiefs', 19, [2]) # chiefs
    teams.append(team)
    team = Team('Bears', 27, [2]) # bears
    teams.append(team)

    # tiers 2 & 3
    team = Team('Lions', 11, [2, 3]) # lions
    teams.append(team)

    # tier 3
    team = Team('Vikings', 1, [3]) # vikings
    teams.append(team)
    team = Team('Rams', 6, [3]) # rams
    teams.append(team)
    team = Team('Redskins', 5, [3]) # redskins
    teams.append(team)

    # tiers 3 & 4
    team = Team('Falcons', 14, [3, 4]) # falcons
    teams.append(team)
    team = Team('Cowboys', 17, [3, 4]) # cowboys
    teams.append(team)

    # tier 4
    team = Team('Broncos', 24, [4]) # broncos
    teams.append(team)
    team = Team('Bengals', 26, [4]) # bengals
    teams.append(team)
    team = Team('Chargers', 20, [4]) # chargers
    teams.append(team)

    # tiers 4 & 5
    team = Team('Buccaneers', 22, [4, 5]) # buccaneers
    teams.append(team)

    # tier 5
    team = Team('Saints', 4, [5]) # saints
    teams.append(team)
    team = Team('Cardinals', 21, [5]) # cardinals
    teams.append(team)
    team = Team('Jets', 12, [5]) # jets
    teams.append(team)
    team = Team('Steelers', 2, [5]) # steelers
    teams.append(team)

    # tiers 5 & 6
    team = Team('Browns', 23, [5, 6]) # browns
    teams.append(team)

    # tier 6
    team = Team('Packers', 9, [6]) # packers
    teams.append(team)
    team = Team('Seahawks', 3, [6]) # seahawks
    teams.append(team)
    team = Team('Colts', 18, [6]) # colts
    teams.append(team)
    team = Team('Patriots', 8, [6]) # patriots
    teams.append(team)

    logger.info('teams size: ' + str(len(teams)))
    return teams, 6

def _roll_team(teams, tier=-1, not_team=-1):
    logger.info('roll_team tier: ' + str(tier) + ' not_team: ' + str(not_team))
    roll = random.randint(1,28)
    logger.info('team roll: ' + str(roll))

    team = teams[roll-1]
    logger.info('team: ' + team.name)

    # if the team is not in the same tier, or is the same team already picked, find another
    while (tier != -1 and tier not in team.tiers) or team.img_id == not_team:
        roll = random.randint(1,28)
        logger.info('backup team roll: ' + str(roll))
        team = teams[roll-1]
        logger.info('backup team: ' + team.name)

    return team 

def _vs(request, teams, tiers, tier_ranking, form_action, format=None):
    logger.warn('_vs')
    team1 = _roll_team(teams)
    tiers = team1.tiers
    idx = random.randint(0,len(tiers))
    tier = team1.tiers[idx]
    logger.info('NEW tier: ' + str(tier))
    team2 = _roll_team(teams, tier=tier, not_team=team1.img_id)
    response_dict = success_dict()
    response_dict['tier'] = tier
    response_dict['tier_ranking'] = tier_ranking
    response_dict['form_action'] = form_action
    response_dict['team1'] = team1
    response_dict['team2'] = team2
    return render_template(request, response_dict, 'gall/site/tecmo_vs.html')

def _vs_random(request, teams):
    logger.warn('_vs_random')
    team1 = _roll_team(teams)
    team2 = _roll_team(teams, not_team=team1.img_id)
    response_dict = success_dict()
    response_dict['team1'] = team1
    response_dict['team2'] = team2
    return render_template(request, response_dict, 'gall/site/tecmo_vs_random.html')

###
### GRAVEYARD
###

def _roll_tier(max_tier=5):
    logger.info('roll_tier')
    roll = random.randint(1,max_tier)
    logger.info('tier roll: ' + str(roll))
    return roll

def _roll_tier_new(min_tier=None, num_tiers=5):
    logger.info('roll_tier')

    tier = None
    while not tier:
        roll = random.randint(1, num_tiers)
        logger.info('tier roll: ' + str(roll))
        if min_tier:
            logger.info('there is a min_tier')
            if roll <= min_tier:
                logger.info('roll is less than min_tier')
                tier = roll
                break

    logger.info('got tier: ' + str(tier))
    return tier