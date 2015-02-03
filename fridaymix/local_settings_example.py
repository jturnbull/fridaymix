DEBUG = True
SERVE_MEDIA = DEBUG
TEMPLATE_DEBUG = DEBUG
EMAIL_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

DEBUG_PROPAGATE_EXCEPTIONS = False

# DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
# DATABASE_HOST = '192.168.0.2'             # Set to empty string for localhost. Not used with sqlite3.
# DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

#python -u -m smtpd -n -c DebuggingServer localhost:1025