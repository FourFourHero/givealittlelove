import logging

import uuid
from givealittlelove.gall.models import Activation

logger = logging.getLogger(__name__)

def create_activation(name, email, code):
    activation = Activation()
    activation.name = name
    activation.email = email
    activation.code = code
    activation.save()
    return activation

def update_activation(activation):
    activation.save()
    return activation

def get_activation(activation_id):
    activation = None
    try:
        activation = Activation.objects.get(pk=activation_id)
    except:
        pass
    return activation

def get_last_activation_by_code(code):
    activations = list(Activation.objects.filter(code=code, coupon_id=-1).order_by('created'))
    if activations:
        return activations[0]
    else:
        return None

def get_activations_by_code(code):
    return list(Activation.objects.filter(code=code).order_by('created'))
