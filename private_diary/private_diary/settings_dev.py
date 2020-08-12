from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギング設定
LOGING = {
    'version': 1, # '1' const
    'disable_existing_loggers': False,

    # logger の設定
    'loggers': {
        # Django が利用するlogger
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diary app が利用するlogger
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # handler の設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        },
    },

    # formatter の設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'