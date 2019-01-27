import grpc
import json
import time
from concurrent import futures

from ..proto import todo_pb2
from ..proto import todo_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


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
            yield todo_pb2.ListTaskResponse(task=task)

    def GetTaskById(self, request, context):
        task = self._get_task(key='id', value=request.id)
        return todo_pb2.GetTaskByIdResponse(task=task)

    def GetTaskByName(self, request, context):
        task = self._get_task(key='name', value=request.name)
        return todo_pb2.GetTaskByNameResponse(task=task)


def read_todo_from_db(db_path):
    """
    Reads todo list from database.

    Returns all task in database.
    """

    with open(db_path) as db:
        todo_list = json.load(db)

    return todo_list


def serve(db_path, max_workers=5, address='[::]:50051'):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    todo_pb2_grpc.add_TodoServicer_to_server(Todo(db_path), server)
    server.add_insecure_port(address)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(None)
