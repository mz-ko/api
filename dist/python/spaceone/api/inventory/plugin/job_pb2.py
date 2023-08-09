# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory/plugin/job.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'spaceone/api/inventory/plugin/job.proto\x12\x1dspaceone.api.inventory.plugin\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x83\x01\n\nTaskFilter\x12\x11\n\tproviders\x18\x01 \x03(\t\x12\x1c\n\x14\x63loud_service_groups\x18\x02 \x03(\t\x12\x1b\n\x13\x63loud_service_types\x18\x03 \x03(\t\x12\x14\n\x0cregion_codes\x18\x04 \x03(\t\x12\x11\n\tresources\x18\x05 \x03(\t\"\xa8\x01\n\x0eGetTaskRequest\x12,\n\x0bsecret_data\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12(\n\x07options\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12>\n\x0btask_filter\x18\x03 \x01(\x0b\x32).spaceone.api.inventory.plugin.TaskFilter\"9\n\x08TaskInfo\x12-\n\x0ctask_options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"C\n\tTasksInfo\x12\x36\n\x05tasks\x18\x01 \x03(\x0b\x32\'.spaceone.api.inventory.plugin.TaskInfo2m\n\x03Job\x12\x66\n\tget_tasks\x12-.spaceone.api.inventory.plugin.GetTaskRequest\x1a(.spaceone.api.inventory.plugin.TasksInfo\"\x00\x42\x44ZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/inventory/pluginb\x06proto3')



_TASKFILTER = DESCRIPTOR.message_types_by_name['TaskFilter']
_GETTASKREQUEST = DESCRIPTOR.message_types_by_name['GetTaskRequest']
_TASKINFO = DESCRIPTOR.message_types_by_name['TaskInfo']
_TASKSINFO = DESCRIPTOR.message_types_by_name['TasksInfo']
TaskFilter = _reflection.GeneratedProtocolMessageType('TaskFilter', (_message.Message,), {
  'DESCRIPTOR' : _TASKFILTER,
  '__module__' : 'spaceone.api.inventory.plugin.job_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.plugin.TaskFilter)
  })
_sym_db.RegisterMessage(TaskFilter)

GetTaskRequest = _reflection.GeneratedProtocolMessageType('GetTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKREQUEST,
  '__module__' : 'spaceone.api.inventory.plugin.job_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.plugin.GetTaskRequest)
  })
_sym_db.RegisterMessage(GetTaskRequest)

TaskInfo = _reflection.GeneratedProtocolMessageType('TaskInfo', (_message.Message,), {
  'DESCRIPTOR' : _TASKINFO,
  '__module__' : 'spaceone.api.inventory.plugin.job_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.plugin.TaskInfo)
  })
_sym_db.RegisterMessage(TaskInfo)

TasksInfo = _reflection.GeneratedProtocolMessageType('TasksInfo', (_message.Message,), {
  'DESCRIPTOR' : _TASKSINFO,
  '__module__' : 'spaceone.api.inventory.plugin.job_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.plugin.TasksInfo)
  })
_sym_db.RegisterMessage(TasksInfo)

_JOB = DESCRIPTOR.services_by_name['Job']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/inventory/plugin'
  _TASKFILTER._serialized_start=134
  _TASKFILTER._serialized_end=265
  _GETTASKREQUEST._serialized_start=268
  _GETTASKREQUEST._serialized_end=436
  _TASKINFO._serialized_start=438
  _TASKINFO._serialized_end=495
  _TASKSINFO._serialized_start=497
  _TASKSINFO._serialized_end=564
  _JOB._serialized_start=566
  _JOB._serialized_end=675
# @@protoc_insertion_point(module_scope)
