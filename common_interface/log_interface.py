import logging
from django.conf import settings

def get_logger(name='general'):
    if not settings.LOGGING['loggers'].has_key(name):
        settings.LOGGING['handlers'][name] = {
                                'level':'DEBUG',
                                'class':'logging.handlers.RotatingFileHandler',
                                'filename': '/home/anshun/TEST/log/' + name + '.log',
                                'maxBytes': 500000,
                                'backupCount': 5,
                                'formatter': 'verbose',
                                }
        settings.LOGGING['loggers'][name] = {
                                'handlers': ['console', name],
                                'level': settings.LOGGER_LEVEL,
                                }
        logging.config.dictConfig(settings.LOGGING)   # must set this to save config into settings
    return logging.getLogger(name)