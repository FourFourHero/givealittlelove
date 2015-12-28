import logging
import random

from givealittlelove.gall.views.response import *

logger = logging.getLogger(__name__)

class Team(object):
    name = None
    id = -1
    tiers = []

    def __init__(self, name, img_id, tiers):
        self.name = name
        self.img_id = img_id
        self.tiers = tiers

# http://tecmotourney.blogspot.com/p/team-tiers.html
def setup_teams_tomczak():
    logging.info('setup_teams_tomczak')
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

    return teams

def setup_teams_rook():
    logging.info('setup_teams_rook')
    teams = []

    team = Team('Bills', 25, [1]) # bills
    teams.append(team)
    team = Team('49ers', 28, [1]) # 49ers
    teams.append(team)
    team = Team('Oilers', 10, [1]) # oilers
    teams.append(team)

    team = Team('Giants', 13, [2]) # giants
    teams.append(team)
    team = Team('Raiders', 7, [2]) # raiders
    teams.append(team)
    team = Team('Dolphins', 16, [2]) # dolphins
    teams.append(team)
    team = Team('Eagles', 15, [2]) # eagles
    teams.append(team)
    team = Team('Chiefs', 19, [2]) # chiefs
    teams.append(team)
    team = Team('Bears', 27, [2]) # bears
    teams.append(team)

    team = Team('Vikings', 1, [3]) # vikings
    teams.append(team)
    team = Team('Rams', 6, [2, 3]) # rams
    teams.append(team)
    team = Team('Redskins', 5, [3]) # redskins
    teams.append(team)
    team = Team('Lions', 11, [3]) # lions
    teams.append(team)
    team = Team('Falcons', 14, [3]) # falcons
    teams.append(team)
    team = Team('Buccaneers', 22, [3]) # buccaneers
    teams.append(team)

    team = Team('Cowboys', 17, [4]) # cowboys
    teams.append(team)
    team = Team('Bengals', 26, [4]) # bengals
    teams.append(team)
    team = Team('Saints', 4, [4]) # saints
    teams.append(team)
    team = Team('Broncos', 24, [4]) # broncos
    teams.append(team)
    team = Team('Chargers', 20, [4]) # chargers
    teams.append(team)
    team = Team('Cardinals', 21, [4]) # cardinals
    teams.append(team)

    team = Team('Jets', 12, [5]) # jets
    teams.append(team)
    team = Team('Steelers', 2, [5]) # steelers
    teams.append(team)
    team = Team('Browns', 23, [5]) # browns
    teams.append(team)
    team = Team('Packers', 9, [5]) # packers
    teams.append(team)
    team = Team('Seahawks', 3, [5]) # seahawks
    teams.append(team)
    team = Team('Colts', 18, [5]) # colts
    teams.append(team)

    return teams
def roll_tier():
    logging.info('roll_tier')
    roll = random.randint(1,5)
    logging.info('tier roll: ' + str(roll))
    return roll

def roll_team(teams, tier, not_team=-1):
    logging.info('roll_team tier: ' + str(tier) + ' not_team: ' + str(not_team))
    roll = random.randint(1,28)
    logging.info('team roll: ' + str(roll))

    team = teams[roll-1]
    logging.info('team: ' + team.name)

    while tier not in team.tiers or team.img_id == not_team:
        roll = random.randint(1,28)
        logging.info('backup team roll: ' + str(roll))
        team = teams[roll-1]
        logging.info('backup team: ' + team.name)

    return team

def vs_tomczak(request):
    logging.warn('vs_tomczak')

    teams = setup_teams_tomczak()
    tier = roll_tier()

    team1 = roll_team(teams, tier)
    team2 = roll_team(teams, tier, not_team=team1.img_id)
    response_dict = success_dict()
    response_dict['tier'] = tier
    response_dict['tier_ranking'] = 'Tomczak'
    response_dict['form_action'] = '/tecmo/vs/tomczak'
    response_dict['team1'] = team1
    response_dict['team2'] = team2
    return render_template(request, response_dict, 'gall/site/tecmo_vs.html')

def vs_rook(request):
    logging.warn('vs_rook')

    teams = setup_teams_rook()
    tier = roll_tier()

    team1 = roll_team(teams, tier)
    team2 = roll_team(teams, tier, not_team=team1.img_id)
    response_dict = success_dict()
    response_dict['tier'] = tier
    response_dict['tier_ranking'] = 'Rook'
    response_dict['form_action'] = '/tecmo/vs/rook'
    response_dict['team1'] = team1
    response_dict['team2'] = team2
    return render_template(request, response_dict, 'gall/site/tecmo_vs.html')

def home(request):
    logging.warn('home')
    response_dict = success_dict()
    return render_template(request, response_dict, 'gall/site/tecmo.html')