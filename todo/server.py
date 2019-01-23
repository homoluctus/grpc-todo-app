import grpc
import json
from concurrent import futures

from . import todo_pb2
from . import todo_pb2_grpc


class Todo(todo_pb2_grpc.TodoServicer):
    def __init__(self, db_path):
        self.todo_list = read_todo_from_db(db_path)

    def _get_task(self, key, value):
        """
        Find value by key

        :params key: sequence key of todo_list
        :params value: value of request sent by a user
        """

        for task in self.todo_list:
            if task[key] == value:
                return task
        return None

    def ListTask(self, request, context):
        for task in self.todo_list:
            yield task

    def GetTaskById(self, request, context):
        task = self._get_task(key='id', value=request)

        if task is None:
            return todo_pb2.GetTaskByIdResponse(task=None)
        return task

    def GetTaskByName(self, request, context):
        task = self._get_task(key='name', value=request)
        if task is None:
            return todo_pb2.GetTaskByNameResponse(task=None)
        return task


def read_todo_from_db(db_path):
    """
    Reads todo list from database.

    Returns all task in database as a sequence of todo_pb2.Task.
    """

    todo_list = []

    with open(db_path) as db:
        for item in json.load(db):
            task = todo_pb2.Task(
                        id=item['id'],
                        name=item['name'],
                        is_complete=item['is_complete'],
                        priority=item['priority'])
            todo_list.append(task)

    return todo_list


def serve(db_path, max_workers=5, port='[::]:50051'):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    todo_pb2_grpc.add_TodoServicer_to_server(Todo(db_path), server)
    server.add_insecure_port(port)
    server.start()
