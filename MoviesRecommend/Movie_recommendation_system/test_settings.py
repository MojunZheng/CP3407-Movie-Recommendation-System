from .settings import *

# Test settings for Practical 7 automated tests.
# The original project uses MySQL. These test settings use SQLite memory database
# so automated tests can run without changing the local MySQL data.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
