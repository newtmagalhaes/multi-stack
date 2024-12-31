from multiprocessing import cpu_count
from os import getenv

# server config
bind = f'0.0.0.0:{getenv("APP_PORT", 8000)}'
gunicorn_workers = getenv("GUNICORN_WORKERS", cpu_count() * 2 + 1)
worker_class = 'sync'
max_requests = 500
max_requests_jitter = 50
timeout = 30
keepalive = 5
graceful_timeout = 30
