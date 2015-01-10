"""A version-independent HTTP server."""

from __future__ import print_function

import sys
import argparse

def run_server(handler, server, port):
    server_address = ('', port)
    handler.protocol_version = 'HTTP/1.0'
    httpd = server(server_address, handler)

    sa = httpd.socket.getsockname()
    print('Serving HTTP on', sa[0], 'port', sa[1], '...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nKeyboard interrupt received, exiting.')
        httpd.server_close()
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description='Start a simple HTTP server.')
    parser.add_argument('-p', '--port', action='store', default=8000, type=int,
                        help='specify alternate port [default: 8000]')
    args = parser.parse_args()

    if sys.version_info.major == 2:
        from SimpleHTTPServer import SimpleHTTPRequestHandler
        from BaseHTTPServer import HTTPServer
    else:
        from http.server import SimpleHTTPRequestHandler, HTTPServer
    run_server(SimpleHTTPRequestHandler, HTTPServer, args.port)

if __name__ == '__main__':
    main()
