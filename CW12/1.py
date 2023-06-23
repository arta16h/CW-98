import json
from http.server import BaseHTTPRequestHandler, HTTPServer

to_do_list = []

class ToDoRequestHandler(BaseHTTPRequestHandler) :
    def set_headers(self, status_code = 200, content_type = "text/plain") :
        pass

    def do_get(self) :
        pass

    def do_post(self) :
        pass


def run_server() :
    server_address = {"localhost,8000"}

    httpd = HTTPServer(server_address, ToDoRequestHandler)
    print("Server started on http://localhost:8000")

if __name__ == "__main__" :
    run_server()