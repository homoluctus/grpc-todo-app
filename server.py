import grpc
import json
from concurrent import futures


import todo_pb2
import todo_pb2_grpc


class Todo(todo_pb2_grpc.TodoServicer):
    def ListTask(self, request, context):
        yield task

    def GetTaskById(self, request, context):
        return task

    def GetTaskByName(self, request, context):
        return task


def read_todo_from_db(path='todo_list.json'):
    """
    Reads todo list from database.

    Returns all task in database as a sequence of todo_pb2.Task.
    """

    todo_list = []

    with open(path) as todo_list_file:
        for item in json.load(todo_list_file):
            task = todo_pb2.Task(id=item['id'],
                                 name=item['name'],
                                 is_complete=item['is_complete'],
                                 priority=item['priority'])
            todo_list.append(task)
    return todo_list


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    todo_pb2_grpc.add_TodoServicer_to_server(Todo(), server)
    server.add_insecure_port('[::]:50051')
    server.start()


if __name__ == '__main__':
    serve()
