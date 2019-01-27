import argparse

from ..client import client
from ..server import server

def handle_command():
    parser = argparse.ArgumentParser(
                prog='todo',
                description='Todo server and client tool',)

    subparsers = parser.add_subparsers(
        dest='mode',
        help='server or client mode'
    )

    server_parser = subparsers.add_parser(
        'server',
        help='server sub command'
    )

    client_parser = subparsers.add_parser(
        'client',
        help='client sub command'
    )

    handle_server_subcommand(server_parser)

    return parser.parse_args()

def handle_server_subcommand(parser):
    parser.add_argument(
        'path',
        help='json file path to store data'
    )

    parser.add_argument(
        '-w'
        '--worker',
        nargs='?',
        default=5,
        dest='worker',
        help='Maximum workers for thread pool'
    )

    parser.add_argument(
        '-a',
        '--address',
        nargs='?',
        dest='address',
        default='[::]:50051',
        help='Bind address (host and port)'
    )


def main():
    args = handle_command()

    if getattr(args, 'mode') == 'server':
        server.serve(
            db_path=args.path,
            max_workers=args.worker,
            address=args.address
        )
    else:
        client.main()