#!/usr/bin/env python3
"""
Simple HTTP server that runs commands
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
import logging
from sys import argv
import subprocess

class S(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"GET request,\nPath: {self.path}\nHeaders:\n{self.headers}\n")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        url = unquote(self.path[1:])
        command = url.split("?")[0]
        query = {q.split("=")[0]: q.split("=")[1] for q in url.split("?")[1].split("&")} if len(url.split("?")) > 1 else {}
        logging.info(f"-> Running: {command}")
        output = subprocess.run(command.split(' '), stdout=subprocess.PIPE, shell=True, **query).stdout
        logging.info(f"<- Output: {output}")

        self.wfile.write(output)


def run(server_class=HTTPServer, handler_class=S, port=8585):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
