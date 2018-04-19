import logging
from django.conf import settings

from common_interface.const import PathConst

def get_logger(name='general'):
    if not name in settings.LOGGING['loggers']:
        settings.LOGGING['handlers'][name] = {
                                'level':'DEBUG',
                                'class':'logging.handlers.RotatingFileHandler',
                                'filename': PathConst.LOG_FOLDER + name + '.log',
                                'maxBytes': 500000,
                                'backupCount': 5,
                                'formatter': 'verbose',
                                'encoding': 'utf8'
                                }
        settings.LOGGING['loggers'][name] = {
                                'handlers': ['console', name],
                                'level': settings.LOGGER_LEVEL,
                                }
        logging.config.dictConfig(settings.LOGGING)   # must set this to save config into settings
    return logging.getLogger(name)