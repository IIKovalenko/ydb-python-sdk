# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/protos/ydb_value.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/protos/ydb_value.proto',
  package='Ydb',
  syntax='proto3',
  serialized_pb=_b('\n(kikimr/public/api/protos/ydb_value.proto\x12\x03Ydb\x1a\x1cgoogle/protobuf/struct.proto\"/\n\x0b\x44\x65\x63imalType\x12\x11\n\tprecision\x18\x01 \x01(\r\x12\r\n\x05scale\x18\x02 \x01(\r\"\'\n\x0cOptionalType\x12\x17\n\x04item\x18\x01 \x01(\x0b\x32\t.Ydb.Type\"#\n\x08ListType\x12\x17\n\x04item\x18\x01 \x01(\x0b\x32\t.Ydb.Type\"e\n\x0bVariantType\x12%\n\x0btuple_items\x18\x01 \x01(\x0b\x32\x0e.Ydb.TupleTypeH\x00\x12\'\n\x0cstruct_items\x18\x02 \x01(\x0b\x32\x0f.Ydb.StructTypeH\x00\x42\x06\n\x04type\"(\n\tTupleType\x12\x1b\n\x08\x65lements\x18\x01 \x03(\x0b\x32\t.Ydb.Type\"5\n\x0cStructMember\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x04type\x18\x02 \x01(\x0b\x32\t.Ydb.Type\"0\n\nStructType\x12\"\n\x07members\x18\x01 \x03(\x0b\x32\x11.Ydb.StructMember\">\n\x08\x44ictType\x12\x16\n\x03key\x18\x01 \x01(\x0b\x32\t.Ydb.Type\x12\x1a\n\x07payload\x18\x02 \x01(\x0b\x32\t.Ydb.Type\"\xd4\x05\n\x04Type\x12,\n\x07type_id\x18\x01 \x01(\x0e\x32\x19.Ydb.Type.PrimitiveTypeIdH\x00\x12(\n\x0c\x64\x65\x63imal_type\x18\x02 \x01(\x0b\x32\x10.Ydb.DecimalTypeH\x00\x12*\n\roptional_type\x18\x65 \x01(\x0b\x32\x11.Ydb.OptionalTypeH\x00\x12\"\n\tlist_type\x18\x66 \x01(\x0b\x32\r.Ydb.ListTypeH\x00\x12$\n\ntuple_type\x18g \x01(\x0b\x32\x0e.Ydb.TupleTypeH\x00\x12&\n\x0bstruct_type\x18h \x01(\x0b\x32\x0f.Ydb.StructTypeH\x00\x12\"\n\tdict_type\x18i \x01(\x0b\x32\r.Ydb.DictTypeH\x00\x12(\n\x0cvariant_type\x18j \x01(\x0b\x32\x10.Ydb.VariantTypeH\x00\x12\x30\n\tvoid_type\x18\xc9\x01 \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00\"\xcd\x02\n\x0fPrimitiveTypeId\x12!\n\x1dPRIMITIVE_TYPE_ID_UNSPECIFIED\x10\x00\x12\x08\n\x04\x42OOL\x10\x06\x12\x08\n\x04INT8\x10\x07\x12\t\n\x05UINT8\x10\x05\x12\t\n\x05INT16\x10\x08\x12\n\n\x06UINT16\x10\t\x12\t\n\x05INT32\x10\x01\x12\n\n\x06UINT32\x10\x02\x12\t\n\x05INT64\x10\x03\x12\n\n\x06UINT64\x10\x04\x12\t\n\x05\x46LOAT\x10!\x12\n\n\x06\x44OUBLE\x10 \x12\x08\n\x04\x44\x41TE\x10\x30\x12\x0c\n\x08\x44\x41TETIME\x10\x31\x12\r\n\tTIMESTAMP\x10\x32\x12\x0c\n\x08INTERVAL\x10\x33\x12\x0b\n\x07TZ_DATE\x10\x34\x12\x0f\n\x0bTZ_DATETIME\x10\x35\x12\x10\n\x0cTZ_TIMESTAMP\x10\x36\x12\x0b\n\x06STRING\x10\x81 \x12\t\n\x04UTF8\x10\x80$\x12\t\n\x04YSON\x10\x81$\x12\t\n\x04JSON\x10\x82$\x12\t\n\x04UUID\x10\x83$B\x06\n\x04type\"A\n\tValuePair\x12\x17\n\x03key\x18\x01 \x01(\x0b\x32\n.Ydb.Value\x12\x1b\n\x07payload\x18\x02 \x01(\x0b\x32\n.Ydb.Value\"\xb1\x03\n\x05Value\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x15\n\x0bint32_value\x18\x02 \x01(\x0fH\x00\x12\x16\n\x0cuint32_value\x18\x03 \x01(\x07H\x00\x12\x15\n\x0bint64_value\x18\x04 \x01(\x10H\x00\x12\x16\n\x0cuint64_value\x18\x05 \x01(\x06H\x00\x12\x15\n\x0b\x66loat_value\x18\x06 \x01(\x02H\x00\x12\x16\n\x0c\x64ouble_value\x18\x07 \x01(\x01H\x00\x12\x15\n\x0b\x62ytes_value\x18\x08 \x01(\x0cH\x00\x12\x14\n\ntext_value\x18\t \x01(\tH\x00\x12\x35\n\x0fnull_flag_value\x18\n \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00\x12\"\n\x0cnested_value\x18\x0b \x01(\x0b\x32\n.Ydb.ValueH\x00\x12\x11\n\x07low_128\x18\x0f \x01(\x06H\x00\x12\x19\n\x05items\x18\x0c \x03(\x0b\x32\n.Ydb.Value\x12\x1d\n\x05pairs\x18\r \x03(\x0b\x32\x0e.Ydb.ValuePair\x12\x15\n\rvariant_index\x18\x0e \x01(\r\x12\x10\n\x08high_128\x18\x10 \x01(\x06\x42\x07\n\x05value\"@\n\nTypedValue\x12\x17\n\x04type\x18\x01 \x01(\x0b\x32\t.Ydb.Type\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.Ydb.Value\"/\n\x06\x43olumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x04type\x18\x02 \x01(\x0b\x32\t.Ydb.Type\"V\n\tResultSet\x12\x1c\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x0b.Ydb.Column\x12\x18\n\x04rows\x18\x02 \x03(\x0b\x32\n.Ydb.Value\x12\x11\n\ttruncated\x18\x03 \x01(\x08\x42 \n\x0e\x63om.yandex.ydbB\x0bValueProtos\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])



_TYPE_PRIMITIVETYPEID = _descriptor.EnumDescriptor(
  name='PrimitiveTypeId',
  full_name='Ydb.Type.PrimitiveTypeId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRIMITIVE_TYPE_ID_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=1, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT8', index=2, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT8', index=3, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT16', index=4, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT16', index=5, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=6, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT32', index=7, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=8, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT64', index=9, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=10, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=11, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE', index=12, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATETIME', index=13, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=14, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERVAL', index=15, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TZ_DATE', index=16, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TZ_DATETIME', index=17, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TZ_TIMESTAMP', index=18, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=19, number=4097,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UTF8', index=20, number=4608,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YSON', index=21, number=4609,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JSON', index=22, number=4610,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UUID', index=23, number=4611,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=904,
  serialized_end=1237,
)
_sym_db.RegisterEnumDescriptor(_TYPE_PRIMITIVETYPEID)


_DECIMALTYPE = _descriptor.Descriptor(
  name='DecimalType',
  full_name='Ydb.DecimalType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='precision', full_name='Ydb.DecimalType.precision', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='Ydb.DecimalType.scale', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=79,
  serialized_end=126,
)


_OPTIONALTYPE = _descriptor.Descriptor(
  name='OptionalType',
  full_name='Ydb.OptionalType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='Ydb.OptionalType.item', index=0,
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
  serialized_start=128,
  serialized_end=167,
)


_LISTTYPE = _descriptor.Descriptor(
  name='ListType',
  full_name='Ydb.ListType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='Ydb.ListType.item', index=0,
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
  serialized_start=169,
  serialized_end=204,
)


_VARIANTTYPE = _descriptor.Descriptor(
  name='VariantType',
  full_name='Ydb.VariantType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tuple_items', full_name='Ydb.VariantType.tuple_items', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='struct_items', full_name='Ydb.VariantType.struct_items', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='Ydb.VariantType.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=206,
  serialized_end=307,
)


_TUPLETYPE = _descriptor.Descriptor(
  name='TupleType',
  full_name='Ydb.TupleType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='elements', full_name='Ydb.TupleType.elements', index=0,
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
  serialized_start=309,
  serialized_end=349,
)


_STRUCTMEMBER = _descriptor.Descriptor(
  name='StructMember',
  full_name='Ydb.StructMember',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Ydb.StructMember.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Ydb.StructMember.type', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=404,
)


_STRUCTTYPE = _descriptor.Descriptor(
  name='StructType',
  full_name='Ydb.StructType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='members', full_name='Ydb.StructType.members', index=0,
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
  serialized_start=406,
  serialized_end=454,
)


_DICTTYPE = _descriptor.Descriptor(
  name='DictType',
  full_name='Ydb.DictType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Ydb.DictType.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='Ydb.DictType.payload', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=456,
  serialized_end=518,
)


_TYPE = _descriptor.Descriptor(
  name='Type',
  full_name='Ydb.Type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_id', full_name='Ydb.Type.type_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decimal_type', full_name='Ydb.Type.decimal_type', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optional_type', full_name='Ydb.Type.optional_type', index=2,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list_type', full_name='Ydb.Type.list_type', index=3,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tuple_type', full_name='Ydb.Type.tuple_type', index=4,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='struct_type', full_name='Ydb.Type.struct_type', index=5,
      number=104, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dict_type', full_name='Ydb.Type.dict_type', index=6,
      number=105, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_type', full_name='Ydb.Type.variant_type', index=7,
      number=106, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='void_type', full_name='Ydb.Type.void_type', index=8,
      number=201, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TYPE_PRIMITIVETYPEID,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='Ydb.Type.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=521,
  serialized_end=1245,
)


_VALUEPAIR = _descriptor.Descriptor(
  name='ValuePair',
  full_name='Ydb.ValuePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Ydb.ValuePair.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='Ydb.ValuePair.payload', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1247,
  serialized_end=1312,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='Ydb.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='Ydb.Value.bool_value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int32_value', full_name='Ydb.Value.int32_value', index=1,
      number=2, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint32_value', full_name='Ydb.Value.uint32_value', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='Ydb.Value.int64_value', index=3,
      number=4, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint64_value', full_name='Ydb.Value.uint64_value', index=4,
      number=5, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='Ydb.Value.float_value', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='Ydb.Value.double_value', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='Ydb.Value.bytes_value', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text_value', full_name='Ydb.Value.text_value', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='null_flag_value', full_name='Ydb.Value.null_flag_value', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nested_value', full_name='Ydb.Value.nested_value', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low_128', full_name='Ydb.Value.low_128', index=11,
      number=15, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='Ydb.Value.items', index=12,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pairs', full_name='Ydb.Value.pairs', index=13,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_index', full_name='Ydb.Value.variant_index', index=14,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high_128', full_name='Ydb.Value.high_128', index=15,
      number=16, type=6, cpp_type=4, label=1,
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
    _descriptor.OneofDescriptor(
      name='value', full_name='Ydb.Value.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1315,
  serialized_end=1748,
)


_TYPEDVALUE = _descriptor.Descriptor(
  name='TypedValue',
  full_name='Ydb.TypedValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Ydb.TypedValue.type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Ydb.TypedValue.value', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1750,
  serialized_end=1814,
)


_COLUMN = _descriptor.Descriptor(
  name='Column',
  full_name='Ydb.Column',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Ydb.Column.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Ydb.Column.type', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1816,
  serialized_end=1863,
)


_RESULTSET = _descriptor.Descriptor(
  name='ResultSet',
  full_name='Ydb.ResultSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='Ydb.ResultSet.columns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='Ydb.ResultSet.rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truncated', full_name='Ydb.ResultSet.truncated', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=1865,
  serialized_end=1951,
)

_OPTIONALTYPE.fields_by_name['item'].message_type = _TYPE
_LISTTYPE.fields_by_name['item'].message_type = _TYPE
_VARIANTTYPE.fields_by_name['tuple_items'].message_type = _TUPLETYPE
_VARIANTTYPE.fields_by_name['struct_items'].message_type = _STRUCTTYPE
_VARIANTTYPE.oneofs_by_name['type'].fields.append(
  _VARIANTTYPE.fields_by_name['tuple_items'])
_VARIANTTYPE.fields_by_name['tuple_items'].containing_oneof = _VARIANTTYPE.oneofs_by_name['type']
_VARIANTTYPE.oneofs_by_name['type'].fields.append(
  _VARIANTTYPE.fields_by_name['struct_items'])
_VARIANTTYPE.fields_by_name['struct_items'].containing_oneof = _VARIANTTYPE.oneofs_by_name['type']
_TUPLETYPE.fields_by_name['elements'].message_type = _TYPE
_STRUCTMEMBER.fields_by_name['type'].message_type = _TYPE
_STRUCTTYPE.fields_by_name['members'].message_type = _STRUCTMEMBER
_DICTTYPE.fields_by_name['key'].message_type = _TYPE
_DICTTYPE.fields_by_name['payload'].message_type = _TYPE
_TYPE.fields_by_name['type_id'].enum_type = _TYPE_PRIMITIVETYPEID
_TYPE.fields_by_name['decimal_type'].message_type = _DECIMALTYPE
_TYPE.fields_by_name['optional_type'].message_type = _OPTIONALTYPE
_TYPE.fields_by_name['list_type'].message_type = _LISTTYPE
_TYPE.fields_by_name['tuple_type'].message_type = _TUPLETYPE
_TYPE.fields_by_name['struct_type'].message_type = _STRUCTTYPE
_TYPE.fields_by_name['dict_type'].message_type = _DICTTYPE
_TYPE.fields_by_name['variant_type'].message_type = _VARIANTTYPE
_TYPE.fields_by_name['void_type'].enum_type = google_dot_protobuf_dot_struct__pb2._NULLVALUE
_TYPE_PRIMITIVETYPEID.containing_type = _TYPE
_TYPE.oneofs_by_name['type'].fields.append(
  _TYPE.fields_by_name['type_id'])
_TYPE.fields_by_name['type_id'].containing_oneof = _TYPE.oneofs_by_name['type']
_TYPE.oneofs_by_name['type'].fields.append(
  _TYPE.fields_by_name['decimal_type'])
_TYPE.fields_by_name['decimal_type'].containing_oneof = _TYPE.oneofs_by_name['type']
_TYPE.oneofs_by_name['type'].fields.append(
  _TYPE.fields_by_name['optional_type'])
_TYPE.fields_by_name['optional_type'].containing_oneof = _TYPE.oneofs_by_name['type']
_TYPE.oneofs_by_name['type'].fields.append(
  _TYPE.fields_by_name['list_type'])
_TYPE.fields_by_name['list_type'].containing_oneof = _TYPE.oneofs_by_name['type']
_TYPE.oneofs_by_name['type'].fields.append(
  _TYPE.fields_by_name['tuple_type'])
_TYPE.fields_by_name['tuple_type'].containing_oneof = _TYPE.oneofs_by_name['type']
_TYPE.oneofs_by_name['type'].fields.append(
  _TYPE.fields_by_name['struct_type'])
_TYPE.fields_by_name['struct_type'].containing_oneof = _TYPE.oneofs_by_name['type']
_TYPE.oneofs_by_name['type'].fields.append(
  _TYPE.fields_by_name['dict_type'])
_TYPE.fields_by_name['dict_type'].containing_oneof = _TYPE.oneofs_by_name['type']
_TYPE.oneofs_by_name['type'].fields.append(
  _TYPE.fields_by_name['variant_type'])
_TYPE.fields_by_name['variant_type'].containing_oneof = _TYPE.oneofs_by_name['type']
_TYPE.oneofs_by_name['type'].fields.append(
  _TYPE.fields_by_name['void_type'])
_TYPE.fields_by_name['void_type'].containing_oneof = _TYPE.oneofs_by_name['type']
_VALUEPAIR.fields_by_name['key'].message_type = _VALUE
_VALUEPAIR.fields_by_name['payload'].message_type = _VALUE
_VALUE.fields_by_name['null_flag_value'].enum_type = google_dot_protobuf_dot_struct__pb2._NULLVALUE
_VALUE.fields_by_name['nested_value'].message_type = _VALUE
_VALUE.fields_by_name['items'].message_type = _VALUE
_VALUE.fields_by_name['pairs'].message_type = _VALUEPAIR
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['bool_value'])
_VALUE.fields_by_name['bool_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['int32_value'])
_VALUE.fields_by_name['int32_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['uint32_value'])
_VALUE.fields_by_name['uint32_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['int64_value'])
_VALUE.fields_by_name['int64_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['uint64_value'])
_VALUE.fields_by_name['uint64_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['float_value'])
_VALUE.fields_by_name['float_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['double_value'])
_VALUE.fields_by_name['double_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['bytes_value'])
_VALUE.fields_by_name['bytes_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['text_value'])
_VALUE.fields_by_name['text_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['null_flag_value'])
_VALUE.fields_by_name['null_flag_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['nested_value'])
_VALUE.fields_by_name['nested_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['low_128'])
_VALUE.fields_by_name['low_128'].containing_oneof = _VALUE.oneofs_by_name['value']
_TYPEDVALUE.fields_by_name['type'].message_type = _TYPE
_TYPEDVALUE.fields_by_name['value'].message_type = _VALUE
_COLUMN.fields_by_name['type'].message_type = _TYPE
_RESULTSET.fields_by_name['columns'].message_type = _COLUMN
_RESULTSET.fields_by_name['rows'].message_type = _VALUE
DESCRIPTOR.message_types_by_name['DecimalType'] = _DECIMALTYPE
DESCRIPTOR.message_types_by_name['OptionalType'] = _OPTIONALTYPE
DESCRIPTOR.message_types_by_name['ListType'] = _LISTTYPE
DESCRIPTOR.message_types_by_name['VariantType'] = _VARIANTTYPE
DESCRIPTOR.message_types_by_name['TupleType'] = _TUPLETYPE
DESCRIPTOR.message_types_by_name['StructMember'] = _STRUCTMEMBER
DESCRIPTOR.message_types_by_name['StructType'] = _STRUCTTYPE
DESCRIPTOR.message_types_by_name['DictType'] = _DICTTYPE
DESCRIPTOR.message_types_by_name['Type'] = _TYPE
DESCRIPTOR.message_types_by_name['ValuePair'] = _VALUEPAIR
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['TypedValue'] = _TYPEDVALUE
DESCRIPTOR.message_types_by_name['Column'] = _COLUMN
DESCRIPTOR.message_types_by_name['ResultSet'] = _RESULTSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DecimalType = _reflection.GeneratedProtocolMessageType('DecimalType', (_message.Message,), dict(
  DESCRIPTOR = _DECIMALTYPE,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.DecimalType)
  ))
_sym_db.RegisterMessage(DecimalType)

OptionalType = _reflection.GeneratedProtocolMessageType('OptionalType', (_message.Message,), dict(
  DESCRIPTOR = _OPTIONALTYPE,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.OptionalType)
  ))
_sym_db.RegisterMessage(OptionalType)

ListType = _reflection.GeneratedProtocolMessageType('ListType', (_message.Message,), dict(
  DESCRIPTOR = _LISTTYPE,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.ListType)
  ))
_sym_db.RegisterMessage(ListType)

VariantType = _reflection.GeneratedProtocolMessageType('VariantType', (_message.Message,), dict(
  DESCRIPTOR = _VARIANTTYPE,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.VariantType)
  ))
_sym_db.RegisterMessage(VariantType)

TupleType = _reflection.GeneratedProtocolMessageType('TupleType', (_message.Message,), dict(
  DESCRIPTOR = _TUPLETYPE,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.TupleType)
  ))
_sym_db.RegisterMessage(TupleType)

StructMember = _reflection.GeneratedProtocolMessageType('StructMember', (_message.Message,), dict(
  DESCRIPTOR = _STRUCTMEMBER,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.StructMember)
  ))
_sym_db.RegisterMessage(StructMember)

StructType = _reflection.GeneratedProtocolMessageType('StructType', (_message.Message,), dict(
  DESCRIPTOR = _STRUCTTYPE,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.StructType)
  ))
_sym_db.RegisterMessage(StructType)

DictType = _reflection.GeneratedProtocolMessageType('DictType', (_message.Message,), dict(
  DESCRIPTOR = _DICTTYPE,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.DictType)
  ))
_sym_db.RegisterMessage(DictType)

Type = _reflection.GeneratedProtocolMessageType('Type', (_message.Message,), dict(
  DESCRIPTOR = _TYPE,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Type)
  ))
_sym_db.RegisterMessage(Type)

ValuePair = _reflection.GeneratedProtocolMessageType('ValuePair', (_message.Message,), dict(
  DESCRIPTOR = _VALUEPAIR,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.ValuePair)
  ))
_sym_db.RegisterMessage(ValuePair)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Value)
  ))
_sym_db.RegisterMessage(Value)

TypedValue = _reflection.GeneratedProtocolMessageType('TypedValue', (_message.Message,), dict(
  DESCRIPTOR = _TYPEDVALUE,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.TypedValue)
  ))
_sym_db.RegisterMessage(TypedValue)

Column = _reflection.GeneratedProtocolMessageType('Column', (_message.Message,), dict(
  DESCRIPTOR = _COLUMN,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Column)
  ))
_sym_db.RegisterMessage(Column)

ResultSet = _reflection.GeneratedProtocolMessageType('ResultSet', (_message.Message,), dict(
  DESCRIPTOR = _RESULTSET,
  __module__ = 'kikimr.public.api.protos.ydb_value_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.ResultSet)
  ))
_sym_db.RegisterMessage(ResultSet)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016com.yandex.ydbB\013ValueProtos\370\001\001'))
# @@protoc_insertion_point(module_scope)
