d = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': "%(asctime)s - %(levelname)s::%(name)s: - %(message)s"
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'filelog': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'WARN',
            'formatter': 'simple',
            'filename': '/var/log/bitstampws.log',
            'when': 'D'
        }
    },
    'loggers': {
        'bitstampws': {
            'handlers': ['console', 'filelog'],
            'propagate': False
        },
        'stream': {
            'handlers': ['console'],
            'propagate': False
        }
    },
    'root': {
        'level': 'NOTSET',
        'handlers': ['console', 'filelog']
    }
}

