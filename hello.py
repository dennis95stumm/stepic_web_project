from urlparse import urlparse

def wsgi_application(environment, start_response):
  status = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  qs = urlparse.parse_qs(environment['QUERY_STRING'])
  body = ''
  for key, value in qs.iteritems():
    body += key + '=' + value + '\n'

  start_response(status, headers)
  return [body]
