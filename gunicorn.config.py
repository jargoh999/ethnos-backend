import os
import multiprocessing

# Bind to the port provided by the environment
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"

# Workers configuration
workers = multiprocessing.cpu_count() * 2 + 1
threads = 4

# Logging
accesslog = '-'  # Output to stdout
errorlog = '-'   # Output to stderr
loglevel = 'info'

# Keepalive
keepalive = 120

# Timeout
timeout = 120