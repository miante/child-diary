import logging.config


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)-6s]  %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
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
