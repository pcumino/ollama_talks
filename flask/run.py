import argparse
from flask import Flask
from app.routes import setup_routes

app = Flask(__name__)
setup_routes(app)

def main(argv):
    parser = argparse.ArgumentParser(description='Flask server')

    parser.add_argument('server', help='Host server address.', nargs='?', default='127.0.0.1')
    parser.add_argument('port', help='Host port number.', nargs='?', default='9100')
    parser.add_argument('-d', '--debug', help='Debug mode.', nargs='?', type=bool, const=True, default=False)

    args = parser.parse_args(argv)

    app.run(port=args.port, host=args.server, debug=args.debug)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
    