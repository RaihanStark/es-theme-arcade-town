#!/usr/bin/env python3
"""
Launch a live 640x480 interactive preview of es-theme-arcade-town on Arch Linux.
"""
import http.server
import os
import socketserver
import webbrowser
from pathlib import Path

ROOT = Path(__file__).parent
PORT = 8765


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    os.chdir(ROOT)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler) as httpd:
        url = f"http://127.0.0.1:{PORT}/preview.html"
        print(f"Serving es-theme-arcade-town preview at {url}")
        print("Controls: Left/Right = switch shops | Enter = open gamelist | Esc = back | M = menu")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nPreview stopped.")
