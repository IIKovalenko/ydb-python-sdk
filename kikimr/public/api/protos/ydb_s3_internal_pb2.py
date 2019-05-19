# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/protos/ydb_s3_internal.proto

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
  name='kikimr/public/api/protos/ydb_s3_internal.proto',
  package='Ydb.S3Internal',
  syntax='proto3',
  serialized_pb=_b('\n.kikimr/public/api/protos/ydb_s3_internal.proto\x12\x0eYdb.S3Internal\x1a,kikimr/public/api/protos/ydb_operation.proto\x1a(kikimr/public/api/protos/ydb_value.proto\"\x9f\x02\n\x10S3ListingRequest\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12#\n\nkey_prefix\x18\x02 \x01(\x0b\x32\x0f.Ydb.TypedValue\x12\x1a\n\x12path_column_prefix\x18\x03 \x01(\t\x12\x1d\n\x15path_column_delimiter\x18\x04 \x01(\t\x12/\n\x16start_after_key_suffix\x18\x05 \x01(\x0b\x32\x0f.Ydb.TypedValue\x12\x10\n\x08max_keys\x18\x06 \x01(\r\x12\x19\n\x11\x63olumns_to_return\x18\x07 \x03(\t\x12\x39\n\x10operation_params\x18\x08 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\"A\n\x11S3ListingResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"u\n\x0fS3ListingResult\x12\'\n\x0f\x63ommon_prefixes\x18\x01 \x01(\x0b\x32\x0e.Ydb.ResultSet\x12 \n\x08\x63ontents\x18\x02 \x01(\x0b\x32\x0e.Ydb.ResultSet\x12\x17\n\x0fkey_suffix_size\x18\x03 \x01(\rB1\n\x1a\x63om.yandex.ydb.s3_internalB\x10S3InternalProtos\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2.DESCRIPTOR,])




_S3LISTINGREQUEST = _descriptor.Descriptor(
  name='S3ListingRequest',
  full_name='Ydb.S3Internal.S3ListingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='Ydb.S3Internal.S3ListingRequest.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_prefix', full_name='Ydb.S3Internal.S3ListingRequest.key_prefix', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_column_prefix', full_name='Ydb.S3Internal.S3ListingRequest.path_column_prefix', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_column_delimiter', full_name='Ydb.S3Internal.S3ListingRequest.path_column_delimiter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_after_key_suffix', full_name='Ydb.S3Internal.S3ListingRequest.start_after_key_suffix', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_keys', full_name='Ydb.S3Internal.S3ListingRequest.max_keys', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='columns_to_return', full_name='Ydb.S3Internal.S3ListingRequest.columns_to_return', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.S3Internal.S3ListingRequest.operation_params', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=155,
  serialized_end=442,
)


_S3LISTINGRESPONSE = _descriptor.Descriptor(
  name='S3ListingResponse',
  full_name='Ydb.S3Internal.S3ListingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.S3Internal.S3ListingResponse.operation', index=0,
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
  serialized_start=444,
  serialized_end=509,
)


_S3LISTINGRESULT = _descriptor.Descriptor(
  name='S3ListingResult',
  full_name='Ydb.S3Internal.S3ListingResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_prefixes', full_name='Ydb.S3Internal.S3ListingResult.common_prefixes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contents', full_name='Ydb.S3Internal.S3ListingResult.contents', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_suffix_size', full_name='Ydb.S3Internal.S3ListingResult.key_suffix_size', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=511,
  serialized_end=628,
)

_S3LISTINGREQUEST.fields_by_name['key_prefix'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2._TYPEDVALUE
_S3LISTINGREQUEST.fields_by_name['start_after_key_suffix'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2._TYPEDVALUE
_S3LISTINGREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_S3LISTINGRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_S3LISTINGRESULT.fields_by_name['common_prefixes'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2._RESULTSET
_S3LISTINGRESULT.fields_by_name['contents'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2._RESULTSET
DESCRIPTOR.message_types_by_name['S3ListingRequest'] = _S3LISTINGREQUEST
DESCRIPTOR.message_types_by_name['S3ListingResponse'] = _S3LISTINGRESPONSE
DESCRIPTOR.message_types_by_name['S3ListingResult'] = _S3LISTINGRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

S3ListingRequest = _reflection.GeneratedProtocolMessageType('S3ListingRequest', (_message.Message,), dict(
  DESCRIPTOR = _S3LISTINGREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_s3_internal_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.S3Internal.S3ListingRequest)
  ))
_sym_db.RegisterMessage(S3ListingRequest)

S3ListingResponse = _reflection.GeneratedProtocolMessageType('S3ListingResponse', (_message.Message,), dict(
  DESCRIPTOR = _S3LISTINGRESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_s3_internal_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.S3Internal.S3ListingResponse)
  ))
_sym_db.RegisterMessage(S3ListingResponse)

S3ListingResult = _reflection.GeneratedProtocolMessageType('S3ListingResult', (_message.Message,), dict(
  DESCRIPTOR = _S3LISTINGRESULT,
  __module__ = 'kikimr.public.api.protos.ydb_s3_internal_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.S3Internal.S3ListingResult)
  ))
_sym_db.RegisterMessage(S3ListingResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.yandex.ydb.s3_internalB\020S3InternalProtos\370\001\001'))
# @@protoc_insertion_point(module_scope)
