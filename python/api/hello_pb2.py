# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61pi/hello.proto\x12\x05myapp\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\rHelloResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2E\n\x0fGreetingService\x12\x32\n\x05Hello\x12\x13.myapp.HelloRequest\x1a\x14.myapp.HelloResponseB\nZ\x08pkg/grpcb\x06proto3')



_HELLOREQUEST = DESCRIPTOR.message_types_by_name['HelloRequest']
_HELLORESPONSE = DESCRIPTOR.message_types_by_name['HelloResponse']
HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'api.hello_pb2'
  # @@protoc_insertion_point(class_scope:myapp.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), {
  'DESCRIPTOR' : _HELLORESPONSE,
  '__module__' : 'api.hello_pb2'
  # @@protoc_insertion_point(class_scope:myapp.HelloResponse)
  })
_sym_db.RegisterMessage(HelloResponse)

_GREETINGSERVICE = DESCRIPTOR.services_by_name['GreetingService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\010pkg/grpc'
  _HELLOREQUEST._serialized_start=26
  _HELLOREQUEST._serialized_end=54
  _HELLORESPONSE._serialized_start=56
  _HELLORESPONSE._serialized_end=88
  _GREETINGSERVICE._serialized_start=90
  _GREETINGSERVICE._serialized_end=159
# @@protoc_insertion_point(module_scope)
