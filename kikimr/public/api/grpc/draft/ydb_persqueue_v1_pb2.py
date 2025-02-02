# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/draft/ydb_persqueue_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_persqueue_v1_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/draft/ydb_persqueue_v1.proto',
  package='Ydb.PersQueue.V1',
  syntax='proto3',
  serialized_pb=_b('\n3kikimr/public/api/grpc/draft/ydb_persqueue_v1.proto\x12\x10Ydb.PersQueue.V1\x1a/kikimr/public/api/protos/ydb_persqueue_v1.proto2\xad\x02\n\x10PersQueueService\x12\x61\n\x12\x43reateWriteSession\x12\".Ydb.PersQueue.WriteSessionRequest\x1a#.Ydb.PersQueue.WriteSessionResponse(\x01\x30\x01\x12^\n\x11\x43reateReadSession\x12!.Ydb.PersQueue.ReadSessionRequest\x1a\".Ydb.PersQueue.ReadSessionResponse(\x01\x30\x01\x12V\n\x13GetReadSessionsInfo\x12\x1e.Ydb.PersQueue.ReadInfoRequest\x1a\x1f.Ydb.PersQueue.ReadInfoResponseB\x1d\n\x1b\x63om.yandex.ydb.persqueue.v1b\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033com.yandex.ydb.persqueue.v1'))

_PERSQUEUESERVICE = _descriptor.ServiceDescriptor(
  name='PersQueueService',
  full_name='Ydb.PersQueue.V1.PersQueueService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=123,
  serialized_end=424,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateWriteSession',
    full_name='Ydb.PersQueue.V1.PersQueueService.CreateWriteSession',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2._WRITESESSIONREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2._WRITESESSIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateReadSession',
    full_name='Ydb.PersQueue.V1.PersQueueService.CreateReadSession',
    index=1,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2._READSESSIONREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2._READSESSIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetReadSessionsInfo',
    full_name='Ydb.PersQueue.V1.PersQueueService.GetReadSessionsInfo',
    index=2,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2._READINFOREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2._READINFORESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PERSQUEUESERVICE)

DESCRIPTOR.services_by_name['PersQueueService'] = _PERSQUEUESERVICE

# @@protoc_insertion_point(module_scope)
