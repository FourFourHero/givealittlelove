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

def get_activation_by_code(code):
    activation = None
    try:
        activation = Activation.objects.get(code=code)
    except:
        pass
    return activation

def get_activations_by_code(code):
    return Activation.objects.filter(code=code).order_by('created')
