# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: spaceone/api/identity/v1/authorization.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'spaceone/api/identity/v1/authorization.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import handler_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_handler__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,spaceone/api/identity/v1/authorization.proto\x12\x18spaceone.api.identity.v1\x1a\x1cgoogle/api/annotations.proto\x1a\"spaceone/api/core/v1/handler.proto2t\n\rAuthorization\x12\x63\n\x06verify\x12*.spaceone.api.core.v1.AuthorizationRequest\x1a+.spaceone.api.core.v1.AuthorizationResponse\"\x00\x42?Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.identity.v1.authorization_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v1'
  _globals['_AUTHORIZATION']._serialized_start=140
  _globals['_AUTHORIZATION']._serialized_end=256
# @@protoc_insertion_point(module_scope)
