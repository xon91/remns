import os
from wsgiref import simple_server
import main

httpd = simple_server.make_server('', 3000, main.app)

httpd.serve_forever()


