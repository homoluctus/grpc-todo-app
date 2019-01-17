from concurrent import futures
import grpc


import todo_pb2
import todo_pb2_grpc


class Todo(todo_pb2_grpc.TodoServicer):
    def ListTask(self, request, context):
        yield task

    def GetTaskById(self, request, context):
        return task

    def GetTaskByName(self, request, context):
        return task


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    todo_pb2_grpc.add_TodoServicer_to_server(Todo(), server)
    server.add_insecure_port('[::]:5001')
    return


if __name__ == '__main__':
    pass
