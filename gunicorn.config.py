import os

# Bind to the port provided by the environment
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"

# Workers configuration
workers = 4
threads = 4

# Logging
accesslog = '-'  # Output to stdout
errorlog = '-'   # Output to stderr