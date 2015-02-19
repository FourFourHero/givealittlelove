import logging

import uuid
from givealittlelove.gall.models import Ambassador

logger = logging.getLogger(__name__)

def create_ambassador(name, email):
    ambassador = Ambassador()
    ambassador.name = name
    ambassador.email = email
    ambassador.code = __create_code()
    logging.info('code: ' + str(ambassador.code))
    ambassador.save()
    return ambassador

def update_ambassador(ambassador):
    ambassador.save()
    return ambassador

def get_ambassador(ambassador_id):
    ambassador = None
    try:
        ambassador = Ambassador.objects.get(pk=ambassador_id)
    except:
        pass
    return ambassador

def __create_code():
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace('-','')
    return random[0:6]