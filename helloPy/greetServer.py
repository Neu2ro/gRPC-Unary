from concurrent import futures
import logging

import grpc
import greet_pb2
import greet_pb2_grpc


class Greeter(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greet_pb2.HelloReply(message="Hello from python Server, %s!" % request.name)
    

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Python Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
