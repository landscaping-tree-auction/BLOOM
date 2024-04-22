"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config

def main():
    """Run administrative tasks."""

    environment = config('ENVIRONMENT', default='development')  # 기본값으로 'development' 지정

    if environment == 'production':
        os.environ.setdefault(
            'DJANGO_SETTINGS_MODULE',
            'config.settings.production',
        )
        print(f'--> Running manage.py with production environment: {sys.argv}')
    else:
        os.environ.setdefault(
            'DJANGO_SETTINGS_MODULE',
            'config.settings.development',
        )
        print(f'--> Running manage.py with \
            development environment: {sys.argv}')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()