# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api import hello_pb2 as api_dot_hello__pb2


class GreetingServiceStub(object):
    """サービスの定義
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Hello = channel.unary_unary(
                '/myapp.GreetingService/Hello',
                request_serializer=api_dot_hello__pb2.HelloRequest.SerializeToString,
                response_deserializer=api_dot_hello__pb2.HelloResponse.FromString,
                )


class GreetingServiceServicer(object):
    """サービスの定義
    """

    def Hello(self, request, context):
        """サービスが持つメソッドの定義
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreetingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Hello': grpc.unary_unary_rpc_method_handler(
                    servicer.Hello,
                    request_deserializer=api_dot_hello__pb2.HelloRequest.FromString,
                    response_serializer=api_dot_hello__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'myapp.GreetingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GreetingService(object):
    """サービスの定義
    """

    @staticmethod
    def Hello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/myapp.GreetingService/Hello',
            api_dot_hello__pb2.HelloRequest.SerializeToString,
            api_dot_hello__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
