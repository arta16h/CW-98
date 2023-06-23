import json
from http.server import BaseHTTPRequestHandler, HTTPServer

to_do_list = []

class ToDoRequestHandler(BaseHTTPRequestHandler) :
    def _set_headers(self, status_code = 200, content_type = "text/plain") :
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()


    def do_get(self) :
        if self.path == "/" :
            self._set_headers(200, "application/json")
            self.wfile.write(json.dumps(to_do_list).encode())
        else:
            self._set_headers(404)
            self.wfile.write("Not Found".encode())


    def do_post(self) :
        if self.path == "/" :
            content_length = int(self.headers["Content-length"])
            payload = self.rfile.read(content_length).decode()
            try :
                to_do_item = json.loads(payload)
                to_do_list.append(to_do_item)
                self._set_headers(201, "text/plain")
                self.wfile.write("To-do Item Created".encode())
            except json.JSONDecodeError :
                self. _set_headers(400)
                self.wfile.write("Inavalid Json payload".encode())
        else :
            self._set_headers(404)
            self.wfile.write("Not Found".encode())




def run_server() :
    server_address = {"localhost,8000"}

    httpd = HTTPServer(server_address, ToDoRequestHandler)
    print("Server started on http://localhost:8000")

if __name__ == "__main__" :
    run_server()