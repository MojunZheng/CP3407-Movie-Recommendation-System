import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Movie_recommendation_system.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Project environment configuration is abnormal. Please check!"
        ) from exc
    execute_from_command_line(sys.argv)
