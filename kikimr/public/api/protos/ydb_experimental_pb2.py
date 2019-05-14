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


from kikimr.public.api.protos import ydb_issue_message_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__issue__message__pb2
from kikimr.public.api.protos import ydb_operation_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2
from kikimr.public.api.protos import ydb_status_codes_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__status__codes__pb2
from kikimr.public.api.protos import ydb_value_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/protos/ydb_experimental.proto',
  package='Ydb.Experimental',
  syntax='proto3',
  serialized_pb=_b('\n/kikimr/public/api/protos/ydb_experimental.proto\x12\x10Ydb.Experimental\x1a\x30kikimr/public/api/protos/ydb_issue_message.proto\x1a,kikimr/public/api/protos/ydb_operation.proto\x1a/kikimr/public/api/protos/ydb_status_codes.proto\x1a(kikimr/public/api/protos/ydb_value.proto\"|\n\x11UploadRowsRequest\x12\r\n\x05table\x18\x01 \x01(\t\x12\x1d\n\x04rows\x18\x02 \x01(\x0b\x32\x0f.Ydb.TypedValue\x12\x39\n\x10operation_params\x18\x03 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\"B\n\x12UploadRowsResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\x12\n\x10UploadRowsResult\"\xec\x01\n\x12ReadColumnsRequest\x12\r\n\x05table\x18\x01 \x01(\t\x12\x0f\n\x07\x63olumns\x18\x02 \x03(\t\x12\x10\n\x08\x66rom_key\x18\x03 \x01(\x0c\x12\x1a\n\x12\x66rom_key_inclusive\x18\x04 \x01(\x08\x12\x0e\n\x06to_key\x18\x05 \x01(\x0c\x12\x18\n\x10to_key_inclusive\x18\x06 \x01(\x08\x12\x10\n\x08max_rows\x18\x07 \x01(\x04\x12\x11\n\tmax_bytes\x18\x08 \x01(\x04\x12\x39\n\x10operation_params\x18\t \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\"C\n\x13ReadColumnsResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"^\n\x11ReadColumnsResult\x12\x0e\n\x06\x62locks\x18\x01 \x03(\x0c\x12\x0b\n\x03\x65of\x18\x02 \x01(\x08\x12\x10\n\x08last_key\x18\x03 \x01(\x0c\x12\x1a\n\x12last_key_inclusive\x18\x04 \x01(\x08\"i\n\x18GetShardLocationsRequest\x12\x12\n\ntablet_ids\x18\x01 \x03(\x04\x12\x39\n\x10operation_params\x18\t \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\"I\n\x19GetShardLocationsResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"-\n\nTabletInfo\x12\x11\n\ttablet_id\x18\x01 \x01(\x04\x12\x0c\n\x04host\x18\x02 \x01(\t\"H\n\x17GetShardLocationsResult\x12-\n\x07tablets\x18\x01 \x03(\x0b\x32\x1c.Ydb.Experimental.TabletInfo\"\xc2\x01\n\x19\x45xecuteStreamQueryRequest\x12\x10\n\x08yql_text\x18\x01 \x01(\t\x12O\n\nparameters\x18\x02 \x03(\x0b\x32;.Ydb.Experimental.ExecuteStreamQueryRequest.ParametersEntry\x1a\x42\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.Ydb.TypedValue:\x02\x38\x01\"\xac\x01\n\x1a\x45xecuteStreamQueryResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.Ydb.StatusIds.StatusCode\x12\'\n\x06issues\x18\x02 \x03(\x0b\x32\x17.Ydb.Issue.IssueMessage\x12:\n\x06result\x18\x03 \x01(\x0b\x32*.Ydb.Experimental.ExecuteStreamQueryResult\">\n\x18\x45xecuteStreamQueryResult\x12\"\n\nresult_set\x18\x01 \x01(\x0b\x32\x0e.Ydb.ResultSetB3\n\x1aru.yandex.ydb.experimentalB\x12\x45xperimentalProtos\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__issue__message__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_ydb__status__codes__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2.DESCRIPTOR,])




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
  serialized_start=256,
  serialized_end=380,
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
  serialized_start=382,
  serialized_end=448,
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
  serialized_start=450,
  serialized_end=468,
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
  serialized_start=471,
  serialized_end=707,
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
  serialized_start=709,
  serialized_end=776,
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
  serialized_start=778,
  serialized_end=872,
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
  serialized_start=874,
  serialized_end=979,
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
  serialized_start=981,
  serialized_end=1054,
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
  serialized_start=1056,
  serialized_end=1101,
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
  serialized_start=1103,
  serialized_end=1175,
)


_EXECUTESTREAMQUERYREQUEST_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='Ydb.Experimental.ExecuteStreamQueryRequest.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Ydb.Experimental.ExecuteStreamQueryRequest.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Ydb.Experimental.ExecuteStreamQueryRequest.ParametersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1306,
  serialized_end=1372,
)

_EXECUTESTREAMQUERYREQUEST = _descriptor.Descriptor(
  name='ExecuteStreamQueryRequest',
  full_name='Ydb.Experimental.ExecuteStreamQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='yql_text', full_name='Ydb.Experimental.ExecuteStreamQueryRequest.yql_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='Ydb.Experimental.ExecuteStreamQueryRequest.parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_EXECUTESTREAMQUERYREQUEST_PARAMETERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1178,
  serialized_end=1372,
)


_EXECUTESTREAMQUERYRESPONSE = _descriptor.Descriptor(
  name='ExecuteStreamQueryResponse',
  full_name='Ydb.Experimental.ExecuteStreamQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Ydb.Experimental.ExecuteStreamQueryResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='issues', full_name='Ydb.Experimental.ExecuteStreamQueryResponse.issues', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='Ydb.Experimental.ExecuteStreamQueryResponse.result', index=2,
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
  serialized_start=1375,
  serialized_end=1547,
)


_EXECUTESTREAMQUERYRESULT = _descriptor.Descriptor(
  name='ExecuteStreamQueryResult',
  full_name='Ydb.Experimental.ExecuteStreamQueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_set', full_name='Ydb.Experimental.ExecuteStreamQueryResult.result_set', index=0,
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
  serialized_start=1549,
  serialized_end=1611,
)

_UPLOADROWSREQUEST.fields_by_name['rows'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2._TYPEDVALUE
_UPLOADROWSREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_UPLOADROWSRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_READCOLUMNSREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_READCOLUMNSRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_GETSHARDLOCATIONSREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_GETSHARDLOCATIONSRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_GETSHARDLOCATIONSRESULT.fields_by_name['tablets'].message_type = _TABLETINFO
_EXECUTESTREAMQUERYREQUEST_PARAMETERSENTRY.fields_by_name['value'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2._TYPEDVALUE
_EXECUTESTREAMQUERYREQUEST_PARAMETERSENTRY.containing_type = _EXECUTESTREAMQUERYREQUEST
_EXECUTESTREAMQUERYREQUEST.fields_by_name['parameters'].message_type = _EXECUTESTREAMQUERYREQUEST_PARAMETERSENTRY
_EXECUTESTREAMQUERYRESPONSE.fields_by_name['status'].enum_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__status__codes__pb2._STATUSIDS_STATUSCODE
_EXECUTESTREAMQUERYRESPONSE.fields_by_name['issues'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__issue__message__pb2._ISSUEMESSAGE
_EXECUTESTREAMQUERYRESPONSE.fields_by_name['result'].message_type = _EXECUTESTREAMQUERYRESULT
_EXECUTESTREAMQUERYRESULT.fields_by_name['result_set'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2._RESULTSET
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
DESCRIPTOR.message_types_by_name['ExecuteStreamQueryRequest'] = _EXECUTESTREAMQUERYREQUEST
DESCRIPTOR.message_types_by_name['ExecuteStreamQueryResponse'] = _EXECUTESTREAMQUERYRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteStreamQueryResult'] = _EXECUTESTREAMQUERYRESULT
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

ExecuteStreamQueryRequest = _reflection.GeneratedProtocolMessageType('ExecuteStreamQueryRequest', (_message.Message,), dict(

  ParametersEntry = _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _EXECUTESTREAMQUERYREQUEST_PARAMETERSENTRY,
    __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
    # @@protoc_insertion_point(class_scope:Ydb.Experimental.ExecuteStreamQueryRequest.ParametersEntry)
    ))
  ,
  DESCRIPTOR = _EXECUTESTREAMQUERYREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.ExecuteStreamQueryRequest)
  ))
_sym_db.RegisterMessage(ExecuteStreamQueryRequest)
_sym_db.RegisterMessage(ExecuteStreamQueryRequest.ParametersEntry)

ExecuteStreamQueryResponse = _reflection.GeneratedProtocolMessageType('ExecuteStreamQueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTESTREAMQUERYRESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.ExecuteStreamQueryResponse)
  ))
_sym_db.RegisterMessage(ExecuteStreamQueryResponse)

ExecuteStreamQueryResult = _reflection.GeneratedProtocolMessageType('ExecuteStreamQueryResult', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTESTREAMQUERYRESULT,
  __module__ = 'kikimr.public.api.protos.ydb_experimental_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Experimental.ExecuteStreamQueryResult)
  ))
_sym_db.RegisterMessage(ExecuteStreamQueryResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032ru.yandex.ydb.experimentalB\022ExperimentalProtos\370\001\001'))
_EXECUTESTREAMQUERYREQUEST_PARAMETERSENTRY.has_options = True
_EXECUTESTREAMQUERYREQUEST_PARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
