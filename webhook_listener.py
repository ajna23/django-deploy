from http.server import BaseHTTPRequestHandler, HTTPServer
   import subprocess

   PORT = 8000
   SCRIPT_PATH = "./setup_and_run.sh"

   class WebhookHandler(BaseHTTPRequestHandler):
       def do_POST(self):
           self.send_response(200)
           self.end_headers()
           subprocess.call(SCRIPT_PATH, shell=True)

   if _name_ == "_main_":
       server_address = ('', PORT)
       httpd = HTTPServer(server_address, WebhookHandler)
       print(f"Webhook listener started on port {PORT}")
       httpd.serve_forever()
