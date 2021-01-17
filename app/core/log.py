import logging.config

from .configs import settings


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': settings.LOG_FORMAT,
        },
    },
    'handlers': {
        'console': {
            'level': logging.getLevelName(settings.LOG_LEVEL),
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': logging.getLevelName(settings.LOG_LEVEL),
            'propagate': False,
        },
    }
}


def configure_logging():
    """
    Base configure function for logging withing application
    """

    logging.config.dictConfig(LOGGING_CONFIG)


logger = logging.getLogger('app')
