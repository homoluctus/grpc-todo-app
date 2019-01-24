import grpc
from todo import todo_pb2
from todo import todo_pb2_grpc


def get_todo_list(stub):
    response = stub.ListTask(todo_pb2.ListTaskRequest())
    print(response)


def get_task_by_name(stub, name):
    response = stub.GetTaskByName(todo_pb2.GetTaskByNameRequest(name=name))
    print(response.task)


def run(target='localhost:50051', callback=None, args=(), kwargs={}):
    with grpc.insecure_channel(target) as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        callback(stub, *args, **kwargs)


if __name__ == '__main__':
    run(callback=get_task_by_name, args=('task2',))
