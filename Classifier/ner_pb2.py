# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ner.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ner.proto',
  package='ner',
  syntax='proto3',
  serialized_pb=_b('\n\tner.proto\x12\x03ner\"\x1e\n\nNerRequest\x12\x10\n\x08sentence\x18\x01 \x01(\t\"j\n\x06\x45ntity\x12\x13\n\x0b\x65ntity_type\x18\x01 \x01(\t\x12\x14\n\x0c\x65ntity_value\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x13\n\x0bstart_index\x18\x04 \x01(\x05\x12\x11\n\tend_index\x18\x05 \x01(\x05\")\n\x08NerReply\x12\x1d\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x0b.ner.Entity22\n\x03Ner\x12+\n\x07process\x12\x0f.ner.NerRequest\x1a\r.ner.NerReply\"\x00\x42*\xaa\x02\'Microsoft.AI.NLU.NamedEntityRecognitionb\x06proto3')
)




_NERREQUEST = _descriptor.Descriptor(
  name='NerRequest',
  full_name='ner.NerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sentence', full_name='ner.NerRequest.sentence', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=18,
  serialized_end=48,
)


_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='ner.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='ner.Entity.entity_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_value', full_name='ner.Entity.entity_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='ner.Entity.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_index', full_name='ner.Entity.start_index', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_index', full_name='ner.Entity.end_index', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=50,
  serialized_end=156,
)


_NERREPLY = _descriptor.Descriptor(
  name='NerReply',
  full_name='ner.NerReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='ner.NerReply.entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=158,
  serialized_end=199,
)

_NERREPLY.fields_by_name['entities'].message_type = _ENTITY
DESCRIPTOR.message_types_by_name['NerRequest'] = _NERREQUEST
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['NerReply'] = _NERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NerRequest = _reflection.GeneratedProtocolMessageType('NerRequest', (_message.Message,), dict(
  DESCRIPTOR = _NERREQUEST,
  __module__ = 'ner_pb2'
  # @@protoc_insertion_point(class_scope:ner.NerRequest)
  ))
_sym_db.RegisterMessage(NerRequest)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), dict(
  DESCRIPTOR = _ENTITY,
  __module__ = 'ner_pb2'
  # @@protoc_insertion_point(class_scope:ner.Entity)
  ))
_sym_db.RegisterMessage(Entity)

NerReply = _reflection.GeneratedProtocolMessageType('NerReply', (_message.Message,), dict(
  DESCRIPTOR = _NERREPLY,
  __module__ = 'ner_pb2'
  # @@protoc_insertion_point(class_scope:ner.NerReply)
  ))
_sym_db.RegisterMessage(NerReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\'Microsoft.AI.NLU.NamedEntityRecognition'))

_NER = _descriptor.ServiceDescriptor(
  name='Ner',
  full_name='ner.Ner',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=201,
  serialized_end=251,
  methods=[
  _descriptor.MethodDescriptor(
    name='process',
    full_name='ner.Ner.process',
    index=0,
    containing_service=None,
    input_type=_NERREQUEST,
    output_type=_NERREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NER)

DESCRIPTOR.services_by_name['Ner'] = _NER

# @@protoc_insertion_point(module_scope)
