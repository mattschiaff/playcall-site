#!/usr/bin/env python3
"""Build and serve only dist on loopback. Ctrl-C stops the server."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import subprocess,sys,argparse
r=Path(__file__).resolve().parents[1];p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8873);a=p.parse_args()
subprocess.run([sys.executable,str(r/'scripts/build.py')],check=True)
with ThreadingHTTPServer(('127.0.0.1',a.port),partial(SimpleHTTPRequestHandler,directory=str(r/'dist'))) as server:
 print(f'PlayCall preview: http://127.0.0.1:{a.port}/ (dist only). Stop with Ctrl-C.',flush=True)
 try:server.serve_forever()
 except KeyboardInterrupt:print('\nPreview stopped.')
