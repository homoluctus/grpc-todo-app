import grpc
from todo import todo_pb2
from todo import todo_pb2_grpc


def get_todo_list(stub):
    todo_list = []
    for response in stub.ListTask(todo_pb2.ListTaskRequest()):
        todo_list.append(response)

    print(todo_list)


def get_task_by_id(stub, id_number):
    response = stub.GetTaskById(todo_pb2.GetTaskByIdRequest(id=id_number))
    print(response.task)


def get_task_by_name(stub, name):
    response = stub.GetTaskByName(todo_pb2.GetTaskByNameRequest(name=name))
    print(response.task)


def run(target='localhost:50051', callback=None, args=(), kwargs={}):
    with grpc.insecure_channel(target) as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        callback(stub, *args, **kwargs)
