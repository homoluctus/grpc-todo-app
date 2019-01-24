import argparse
from .server import serve


def handle_args():
    parser = argparse.ArgumentParser(
                prog='Todo app',
                description='This app use gRPC',)

    parser.add_argument(
        'path',
        help='json file path to store data')

    parser.add_argument(
        '-w'
        '--worker',
        nargs='?',
        default=5,
        dest='worker',
        help='Maximum workers for thread pool')

    parser.add_argument(
        '-a',
        '--address',
        nargs='?',
        dest='address',
        default='[::]:50051',
        help='Bind address (host and port)')

    return parser.parse_args()


def start_server():
    args = handle_args()
    serve(db_path=args.path,
          max_workers=args.worker,
          address=args.address)
