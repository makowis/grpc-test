import grpc
from api import hello_pb2 
from api import hello_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = hello_pb2_grpc.GreetingServiceStub(channel)
        response = stub.Hello(hello_pb2.HelloRequest(name='YamadaSan'))
    print("RECV: %s" % response.message)

if __name__ == '__main__':
    run()