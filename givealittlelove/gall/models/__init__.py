import logging
from ambassador import Ambassador
from activation import Activation
from coupon import Coupon

def model_encode(obj):
    enc = None
    try:
        enc = obj.__json__()
    except:
        logging.exception('error encoding')
        enc = None

    if enc:
        return enc

    raise TypeError(repr(obj) + " is not JSON serializable")

def model_encode_verbose(obj):
    enc = None
    try:
        enc = obj.__json_verbose__()
    except Exception, e:
        logging.error(e)
        enc = None

    if enc:
        return enc

    raise TypeError(repr(obj) + " is not JSON serializable")