from grpc_tools import protoc


protoc.main((
    '',
    '-I./todo/proto',
    '--python_out=./todo/proto',
    '--grpc_python_out=./todo/proto',
    './todo/proto/todo.proto',
))