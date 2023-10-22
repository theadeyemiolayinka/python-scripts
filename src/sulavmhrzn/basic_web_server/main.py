from http.server import BaseHTTPRequestHandler, HTTPServer


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handles HTTP GET request"""

        if self.path in ["/", "/index.html"]:
            # Set a 200 response status code
            self.send_response(200)

            # Set content type to text/html because we are serving an html file
            self.send_header("Content-type", "text/html")

            # end_headers should be called everytime we call send_header
            self.end_headers()

            # set path from / to /index.html
            self.path = "/index.html"

            # returns index.html
            file = self.open_file(self.path)

            # Send index.html as response to the client
            return self.wfile.write(bytes(file, "utf-8"))
        else:
            # Sends a 404 error to every other path visited
            self.send_response(404)
            return self.wfile.write(bytes("404 page not found.", "utf-8"))

    def open_file(self, file_name: str):
        """Returns a file with given file name"""

        file_name = file_name.split("/")[1]
        with open(file_name) as f:
            return f.read()


httpd = HTTPServer(("localhost", 8000), Server)
print("Serving on port 8000.")
httpd.serve_forever()
