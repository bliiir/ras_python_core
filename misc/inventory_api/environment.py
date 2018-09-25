# Python's bundled WSGI server
from wsgiref.simple_server import make_server

ip_address = "localhost" # = 127.0.0.1
port = 8000

def application (environ, start_response):

    # Sorting and stringifying the environment key, value pairs
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body.encode('utf-8')]

# Instantiate the server
httpd = make_server (
    ip_address, # The host name
    port, # A port number where to wait for the request
    application # The application object name, in this case a function
)

print(f"serving application on {port}...")

# Wait for a single request, serve it and quit
#httpd.handle_request()
httpd.serve_forever()
