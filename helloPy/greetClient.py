from __future__ import print_function

import logging

import grpc
import greet_pb2
import greet_pb2_grpc


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greet_pb2.HelloRequest(name="Client Python"))
        print("Greeter server replyed: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()

#python -m grpc_tools.protoc -Iprotos --python_out=. --pyi_out=. --grpc_python_out=. protos/greet.proto