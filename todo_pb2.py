# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='todo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntodo.proto\x12\x04todo\"W\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bis_complete\x18\x03 \x01(\x08\x12 \n\x08priority\x18\x04 \x01(\x0e\x32\x0e.todo.Priority\"\x11\n\x0fListTaskRequest\",\n\x10ListTaskResponse\x12\x18\n\x04task\x18\x01 \x01(\x0b\x32\n.todo.Task\"Y\n\x12GetTaskByIdRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bis_complete\x18\x02 \x01(\x08\x12 \n\x08priority\x18\x03 \x01(\x0e\x32\x0e.todo.Priority\"/\n\x13GetTaskByIdResponce\x12\x18\n\x04task\x18\x01 \x01(\x0b\x32\n.todo.Task\"$\n\x14GetTaskByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"Z\n\x15GetTaskByNameResponce\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bis_complete\x18\x02 \x01(\x08\x12 \n\x08priority\x18\x03 \x01(\x0e\x32\x0e.todo.Priority*/\n\x08Priority\x12\x07\n\x03URG\x10\x00\x12\x08\n\x04HIGH\x10\x01\x12\x07\n\x03MED\x10\x02\x12\x07\n\x03LOW\x10\x03\x32\xd1\x01\n\x04Todo\x12;\n\x08ListTask\x12\x15.todo.ListTaskRequest\x1a\x16.todo.ListTaskResponse0\x01\x12\x42\n\x0bGetTaskById\x12\x18.todo.GetTaskByIdRequest\x1a\x19.todo.GetTaskByIdResponce\x12H\n\rGetTaskByName\x12\x1a.todo.GetTaskByNameRequest\x1a\x1b.todo.GetTaskByNameResponceb\x06proto3')
)

_PRIORITY = _descriptor.EnumDescriptor(
  name='Priority',
  full_name='todo.Priority',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='URG', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=444,
  serialized_end=491,
)
_sym_db.RegisterEnumDescriptor(_PRIORITY)

Priority = enum_type_wrapper.EnumTypeWrapper(_PRIORITY)
URG = 0
HIGH = 1
MED = 2
LOW = 3



_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='todo.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.Task.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='todo.Task.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_complete', full_name='todo.Task.is_complete', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='todo.Task.priority', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=107,
)


_LISTTASKREQUEST = _descriptor.Descriptor(
  name='ListTaskRequest',
  full_name='todo.ListTaskRequest',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=126,
)


_LISTTASKRESPONSE = _descriptor.Descriptor(
  name='ListTaskResponse',
  full_name='todo.ListTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='todo.ListTaskResponse.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=172,
)


_GETTASKBYIDREQUEST = _descriptor.Descriptor(
  name='GetTaskByIdRequest',
  full_name='todo.GetTaskByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='todo.GetTaskByIdRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_complete', full_name='todo.GetTaskByIdRequest.is_complete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='todo.GetTaskByIdRequest.priority', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=263,
)


_GETTASKBYIDRESPONCE = _descriptor.Descriptor(
  name='GetTaskByIdResponce',
  full_name='todo.GetTaskByIdResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='todo.GetTaskByIdResponce.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=312,
)


_GETTASKBYNAMEREQUEST = _descriptor.Descriptor(
  name='GetTaskByNameRequest',
  full_name='todo.GetTaskByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='todo.GetTaskByNameRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=350,
)


_GETTASKBYNAMERESPONCE = _descriptor.Descriptor(
  name='GetTaskByNameResponce',
  full_name='todo.GetTaskByNameResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.GetTaskByNameResponce.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_complete', full_name='todo.GetTaskByNameResponce.is_complete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='todo.GetTaskByNameResponce.priority', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=442,
)

_TASK.fields_by_name['priority'].enum_type = _PRIORITY
_LISTTASKRESPONSE.fields_by_name['task'].message_type = _TASK
_GETTASKBYIDREQUEST.fields_by_name['priority'].enum_type = _PRIORITY
_GETTASKBYIDRESPONCE.fields_by_name['task'].message_type = _TASK
_GETTASKBYNAMERESPONCE.fields_by_name['priority'].enum_type = _PRIORITY
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['ListTaskRequest'] = _LISTTASKREQUEST
DESCRIPTOR.message_types_by_name['ListTaskResponse'] = _LISTTASKRESPONSE
DESCRIPTOR.message_types_by_name['GetTaskByIdRequest'] = _GETTASKBYIDREQUEST
DESCRIPTOR.message_types_by_name['GetTaskByIdResponce'] = _GETTASKBYIDRESPONCE
DESCRIPTOR.message_types_by_name['GetTaskByNameRequest'] = _GETTASKBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['GetTaskByNameResponce'] = _GETTASKBYNAMERESPONCE
DESCRIPTOR.enum_types_by_name['Priority'] = _PRIORITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
  DESCRIPTOR = _TASK,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.Task)
  ))
_sym_db.RegisterMessage(Task)

ListTaskRequest = _reflection.GeneratedProtocolMessageType('ListTaskRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTASKREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.ListTaskRequest)
  ))
_sym_db.RegisterMessage(ListTaskRequest)

ListTaskResponse = _reflection.GeneratedProtocolMessageType('ListTaskResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTTASKRESPONSE,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.ListTaskResponse)
  ))
_sym_db.RegisterMessage(ListTaskResponse)

GetTaskByIdRequest = _reflection.GeneratedProtocolMessageType('GetTaskByIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTASKBYIDREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.GetTaskByIdRequest)
  ))
_sym_db.RegisterMessage(GetTaskByIdRequest)

GetTaskByIdResponce = _reflection.GeneratedProtocolMessageType('GetTaskByIdResponce', (_message.Message,), dict(
  DESCRIPTOR = _GETTASKBYIDRESPONCE,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.GetTaskByIdResponce)
  ))
_sym_db.RegisterMessage(GetTaskByIdResponce)

GetTaskByNameRequest = _reflection.GeneratedProtocolMessageType('GetTaskByNameRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTASKBYNAMEREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.GetTaskByNameRequest)
  ))
_sym_db.RegisterMessage(GetTaskByNameRequest)

GetTaskByNameResponce = _reflection.GeneratedProtocolMessageType('GetTaskByNameResponce', (_message.Message,), dict(
  DESCRIPTOR = _GETTASKBYNAMERESPONCE,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.GetTaskByNameResponce)
  ))
_sym_db.RegisterMessage(GetTaskByNameResponce)



_TODO = _descriptor.ServiceDescriptor(
  name='Todo',
  full_name='todo.Todo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=494,
  serialized_end=703,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListTask',
    full_name='todo.Todo.ListTask',
    index=0,
    containing_service=None,
    input_type=_LISTTASKREQUEST,
    output_type=_LISTTASKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTaskById',
    full_name='todo.Todo.GetTaskById',
    index=1,
    containing_service=None,
    input_type=_GETTASKBYIDREQUEST,
    output_type=_GETTASKBYIDRESPONCE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTaskByName',
    full_name='todo.Todo.GetTaskByName',
    index=2,
    containing_service=None,
    input_type=_GETTASKBYNAMEREQUEST,
    output_type=_GETTASKBYNAMERESPONCE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODO)

DESCRIPTOR.services_by_name['Todo'] = _TODO

# @@protoc_insertion_point(module_scope)