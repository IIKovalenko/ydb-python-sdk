# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/protos/ydb_experimental.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_operation_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2
from kikimr.public.api.protos import ydb_value_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/protos/ydb_experimental.proto',
  package='Ydb.Experimental',
  syntax='proto3',
  serialized_pb=_b('\n/kikimr/public/api/protos/ydb_experimental.proto\x12\x10Ydb.Experimental\x1a,kikimr/public/api/protos/ydb_operation.proto\x1a(kikimr/public/api/protos/ydb_value.proto\"|\n\x11UploadRowsRequest\x12\r\n\x05table\x18\x01 \x01(\t\x12\x1d\n\x04rows\x18\x02 \x01(\x0b\x32\x0f.Ydb.TypedValue\x12\x39\n\x10operation_params\x18\x03 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\"B\n\x12UploadRowsResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\x12\n\x10UploadRowsResult\"\xec\x01\n\x12ReadColumnsRequest\x12\r\n\x05table\x18\x01 \x01(\t\x12\x0f\n\x07\x63olumns\x18\x02 \x03(\t\x12\x10\n\x08\x66rom_key\x18\x03 \x01(\x0c\x12\x1a\n\x12\x66rom_key_inclusive\x18\x04 \x01(\x08\x12\x0e\n\x06to_key\x18\x05 \x01(\x0c\x12\x18\n\x10to_key_inclusive\x18\x06 \x01(\x08\x12\x10\n\x08max_rows\x18\x07 \x01(\x04\x12\x11\n\tmax_bytes\x18\x08 \x01(\x04\x12\x39\n\x10operation_params\x18\t \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\"C\n\x13ReadColumnsResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"^\n\x11ReadColumnsResult\x12\x0e\n\x06\x62locks\x18\x01 \x03(\x0c\x12\x0b\n\x03\x65of\x18\x02 \x01(\x08\x12\x10\n\x08last_key\x18\x03 \x01(\x0c\x12\x1a\n\x12last_key_inclusive\x18\x04 \x01(\x08\"i\n\x18GetShardLocationsRequest\x12\x12\n\ntablet_ids\x18\x01 \x03(\x04\x12\x39\n\x10operation_params\x18\t \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\"I\n\x19GetShardLocationsResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"-\n\nTabletInfo\x12\x11\n\ttablet_id\x18\x01 \x01(\x04\x12\x0c\n\x04host\x18\x02 \x01(\t\"H\n\x17GetShardLocationsResult\x12-\n\x07tablets\x18\x01 \x03(\x0b\x32\x1c.Ydb.Experimental.TabletInfoB3\n\x1aru.yandex.ydb.experimentalB\x12\x45xperimentalProtos\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2.DESCRIPTOR,])




_UPLOADROWSREQUEST = _descriptor.Descriptor(
  name='UploadRowsRequest',
  full_name='Ydb.Experimental.UploadRowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='Ydb.Experimental.UploadRowsRequest.table', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='Ydb.Experimental.UploadRowsRequest.rows', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.Experimental.UploadRowsRequest.operation_params', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=281,
)


_UPLOADROWSRESPONSE = _descriptor.Descriptor(
  name='UploadRowsResponse',
  full_name='Ydb.Experimental.UploadRowsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.Experimental.UploadRowsResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=349,
)


_UPLOADROWSRESULT = _descriptor.Descriptor(
  name='UploadRowsResult',
  full_name='Ydb.Experimental.UploadRowsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=369,
)


_READCOLUMNSREQUEST = _descriptor.Descriptor(
  name='ReadColumnsRequest',
  full_name='Ydb.Experimental.ReadColumnsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='Ydb.Experimental.ReadColumnsRequest.table', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='columns', full_name='Ydb.Experimental.ReadColumnsRequest.columns', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_key', full_name='Ydb.Experimental.ReadColumnsRequest.from_key', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_key_inclusive', full_name='Ydb.Experimental.ReadColumnsRequest.from_key_inclusive', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_key', full_name='Ydb.Experimental.ReadColumnsRequest.to_key', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_key_inclusive', full_name='Ydb.Experimental.ReadColumnsRequest.to_key_inclusive', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_rows', full_name='Ydb.Experimental.ReadColumnsRequest.max_rows', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_bytes', full_name='Ydb.Experimental.ReadColumnsRequest.max_bytes', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.Experimental.ReadColumnsRequest.operation_params', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=608,
)


_READCOLUMNSRESPONSE = _descriptor.Descriptor(
  name='ReadColumnsResponse',
  full_name='Ydb.Experimental.ReadColumnsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.Experimental.ReadColumnsResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=677,
)


_READCOLUMNSRESULT = _descriptor.Descriptor(
  name='ReadColumnsResult',
  full_name='Ydb.Experimental.ReadColumnsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocks', full_name='Ydb.Experimental.ReadColumnsResult.blocks', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eof', full_name='Ydb.Experimental.ReadColumnsResult.eof', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_key', full_name='Ydb.Experimental.ReadColumnsResult.last_key', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_key_inclusive', full_name='Ydb.Experimental.ReadColumnsResult.last_key_inclusive', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=679,
  serialized_end=773,
)


_GETSHARDLOCATIONSREQUEST = _descriptor.Descriptor(
  name='GetShardLocationsRequest',
  full_name='Ydb.Experimental.GetShardLocationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tablet_ids', full_name='Ydb.Experimental.GetShardLocationsRequest.tablet_ids', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.Experimental.GetShardLocationsRequest.operation_params', index=1,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=775,
  serialized_end=880,
)


_GETSHARDLOCATIONSRESPONSE = _descriptor.Descriptor(
  name='GetShardLocationsResponse',
  full_name='Ydb.Experimental.GetShardLocationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.Experimental.GetShardLocationsResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=882,
  serialized_end=955,
)


_TABLETINFO = _descriptor.Descriptor(
  name='TabletInfo',
  full_name='Ydb.Experimental.TabletInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tablet_id', full_name='Ydb.Experimental.TabletInfo.tablet_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='Ydb.Experimental.TabletInfo.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=957,
  serialized_end=1002,
)


_GETSHARDLOCATIONSRESULT = _descriptor.Descriptor(
  name='GetShardLocationsResult',
  full_name='Ydb.Experimental.GetShardLocationsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tablets', full_name='Ydb.Experimental.GetShardLocationsResult.tablets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1004,
  serialized_end=1076,
)

_UPLOADROWSREQUEST.fields_by_name['rows'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2._TYPEDVALUE
_UPLOADROWSREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_UPLOADROWSRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_READCOLUMNSREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_READCOLUMNSRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_GETSHARDLOCATIONSREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_GETSHARDLOCATIONSRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_GETSHARDLOCATIONSRESULT.fields_by_name['tablets'].message_type = _TABLETINFO
DESCRIPTOR.message_types_by_name['UploadRowsRequest'] = _UPLOADROWSREQUEST
DESCRIPTOR.message_types_by_name['UploadRowsResponse'] = _UPLOADROWSRESPONSE
DESCRIPTOR.message_types_by_name['UploadRowsResult'] = _UPLOADROWSRESULT
DESCRIPTOR.message_types_by_name['ReadColumnsRequest'] = _READCOLUMNSREQUEST
DESCRIPTOR.message_types_by_name['ReadColumnsResponse'] = _READCOLUMNSRESPONSE
DESCRIPTOR.message_types_by_name['ReadColumnsResult'] = _READCOLUMNSRESULT
DESCRIPTOR.message_types_by_name['GetShardLocationsRequest'] = _GETSHARDLOCATIONSREQUEST
DESCRIPTOR.message_types_by_name['GetShardLocationsResponse'] = _GETSHARDLOCATIONSRESPONSE
DESCRIPTOR.message_types_by_name['TabletInfo'] = _TABLETINFO
DESCRIPTOR.message_types_by_name['GetShardLocationsResult'] = _GETSHARDLOCATIONSRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadRowsRequest = _reflection.GeneratedProtocolMessageType('UploadRowsRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADROWSREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.UploadRowsRequest)
  ))
_sym_db.RegisterMessage(UploadRowsRequest)

UploadRowsResponse = _reflection.GeneratedProtocolMessageType('UploadRowsResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADROWSRESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.UploadRowsResponse)
  ))
_sym_db.RegisterMessage(UploadRowsResponse)

UploadRowsResult = _reflection.GeneratedProtocolMessageType('UploadRowsResult', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADROWSRESULT,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.UploadRowsResult)
  ))
_sym_db.RegisterMessage(UploadRowsResult)

ReadColumnsRequest = _reflection.GeneratedProtocolMessageType('ReadColumnsRequest', (_message.Message,), dict(
  DESCRIPTOR = _READCOLUMNSREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.ReadColumnsRequest)
  ))
_sym_db.RegisterMessage(ReadColumnsRequest)

ReadColumnsResponse = _reflection.GeneratedProtocolMessageType('ReadColumnsResponse', (_message.Message,), dict(
  DESCRIPTOR = _READCOLUMNSRESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.ReadColumnsResponse)
  ))
_sym_db.RegisterMessage(ReadColumnsResponse)

ReadColumnsResult = _reflection.GeneratedProtocolMessageType('ReadColumnsResult', (_message.Message,), dict(
  DESCRIPTOR = _READCOLUMNSRESULT,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.ReadColumnsResult)
  ))
_sym_db.RegisterMessage(ReadColumnsResult)

GetShardLocationsRequest = _reflection.GeneratedProtocolMessageType('GetShardLocationsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSHARDLOCATIONSREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.GetShardLocationsRequest)
  ))
_sym_db.RegisterMessage(GetShardLocationsRequest)

GetShardLocationsResponse = _reflection.GeneratedProtocolMessageType('GetShardLocationsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSHARDLOCATIONSRESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.GetShardLocationsResponse)
  ))
_sym_db.RegisterMessage(GetShardLocationsResponse)

TabletInfo = _reflection.GeneratedProtocolMessageType('TabletInfo', (_message.Message,), dict(
  DESCRIPTOR = _TABLETINFO,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.TabletInfo)
  ))
_sym_db.RegisterMessage(TabletInfo)

GetShardLocationsResult = _reflection.GeneratedProtocolMessageType('GetShardLocationsResult', (_message.Message,), dict(
  DESCRIPTOR = _GETSHARDLOCATIONSRESULT,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.GetShardLocationsResult)
  ))
_sym_db.RegisterMessage(GetShardLocationsResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032ru.yandex.ydb.experimentalB\022ExperimentalProtos\370\001\001'))
# @@protoc_insertion_point(module_scope)
