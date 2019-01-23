import argparse
from .server import serve


def handle_args():
    parser = argparse.ArgumentParser(
                prog='Todo app'
                description='This app use gRPC',)

    parser.add_argument(
        'path',
        description='json file path to store data')

    parser.add_argument(
        '-w'
        '--worker',
        default=5,
        description='Maximum workers for thread pool')

    parser.add_argument(
        '-p',
        '--port',
        default='[::]:50051',
        description='Bind port number')

    return parser.parse_args()


def start_server():
    args = handle_args()
    serve(db_path=args.path,
          max_workers=args.worker,
          port=args.port)
