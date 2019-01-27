import grpc
from ..proto import todo_pb2
from ..proto import todo_pb2_grpc


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


def post_task(stub, name, priority):
    if not isinstance(name, str):
        raise TypeError

    if not isinstance(priority, int):
        raise TypeError

    response = stub.PostTask(
            todo_pb2.PostTaskRequest(name=name, priority=priority))

    if response:
        print('SUCCESS')
    else:
        print('FAILURE')


def run(target='localhost:50051', callback=None, args=(), kwargs={}):
    with grpc.insecure_channel(target) as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        callback(stub, *args, **kwargs)

def main():
    print('============ get_todo_list() ================')
    run(callback=get_todo_list)
    print('============ get_task_by_id() ================')
    run(callback=get_task_by_id, args=(1,))
    print('============ get_task_by_name() ================')
    run(callback=get_task_by_name, args=('task2',))
    #print('============ post_task() ================')
    #run(callback=post_task, args=('test2', 2))