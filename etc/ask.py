CONFIG = {
  'environment': {
    'PYTHON_PATH': '/home/box/web/ask/'
  },
  'mode': 'django',
  'args': (
    '--bind=0.0.0.0:8000',
    '--workers=16',
    '--timeout=60',
    'ask.wsgi',
  ),
}
