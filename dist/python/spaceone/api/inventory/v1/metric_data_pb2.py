# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: spaceone/api/inventory/v1/metric_data.proto
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
    'spaceone/api/inventory/v1/metric_data.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v2 import query_pb2 as spaceone_dot_api_dot_core_dot_v2_dot_query__pb2
from spaceone.api.inventory.v1 import metric_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_metric__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+spaceone/api/inventory/v1/metric_data.proto\x12\x19spaceone.api.inventory.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\x1a&spaceone/api/inventory/v1/metric.proto\"z\n\x0fMetricDataQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x11\n\tmetric_id\x18\x02 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\x12\x12\n\nproject_id\x18\x16 \x01(\t\"\x9b\x02\n\x0eMetricDataInfo\x12\x11\n\tmetric_id\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\'\n\x06labels\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x12\n\nproject_id\x18\x17 \x01(\t\x12\x1a\n\x12service_account_id\x18\x18 \x01(\t\x12\x14\n\x0cnamespace_id\x18\x19 \x01(\t\x12\x14\n\x0c\x63reated_year\x18\x1f \x01(\t\x12\x15\n\rcreated_month\x18  \x01(\t\x12\x14\n\x0c\x63reated_date\x18! \x01(\t\"b\n\x0fMetricDatasInfo\x12:\n\x07results\x18\x01 \x03(\x0b\x32).spaceone.api.inventory.v1.MetricDataInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"h\n\x16MetricDataAnalyzeQuery\x12;\n\x05query\x18\x01 \x01(\x0b\x32,.spaceone.api.core.v2.TimeSeriesAnalyzeQuery\x12\x11\n\tmetric_id\x18\x02 \x01(\t\"^\n\x13MetricDataStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery\x12\x11\n\tmetric_id\x18\x02 \x01(\t2\x9a\x03\n\nMetricData\x12\x89\x01\n\x04list\x12*.spaceone.api.inventory.v1.MetricDataQuery\x1a*.spaceone.api.inventory.v1.MetricDatasInfo\")\x82\xd3\xe4\x93\x02#\"\x1e/inventory/v1/metric-data/list:\x01*\x12z\n\x04stat\x12..spaceone.api.inventory.v1.MetricDataStatQuery\x1a\x17.google.protobuf.Struct\")\x82\xd3\xe4\x93\x02#\"\x1e/inventory/v1/metric-data/stat:\x01*\x12\x83\x01\n\x07\x61nalyze\x12\x31.spaceone.api.inventory.v1.MetricDataAnalyzeQuery\x1a\x17.google.protobuf.Struct\",\x82\xd3\xe4\x93\x02&\"!/inventory/v1/metric-data/analyze:\x01*B@Z>github.com/cloudforet-io/api/dist/go/spaceone/api/inventory/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.inventory.v1.metric_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z>github.com/cloudforet-io/api/dist/go/spaceone/api/inventory/v1'
  _globals['_METRICDATA'].methods_by_name['list']._loaded_options = None
  _globals['_METRICDATA'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002#\"\036/inventory/v1/metric-data/list:\001*'
  _globals['_METRICDATA'].methods_by_name['stat']._loaded_options = None
  _globals['_METRICDATA'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002#\"\036/inventory/v1/metric-data/stat:\001*'
  _globals['_METRICDATA'].methods_by_name['analyze']._loaded_options = None
  _globals['_METRICDATA'].methods_by_name['analyze']._serialized_options = b'\202\323\344\223\002&\"!/inventory/v1/metric-data/analyze:\001*'
  _globals['_METRICDATAQUERY']._serialized_start=237
  _globals['_METRICDATAQUERY']._serialized_end=359
  _globals['_METRICDATAINFO']._serialized_start=362
  _globals['_METRICDATAINFO']._serialized_end=645
  _globals['_METRICDATASINFO']._serialized_start=647
  _globals['_METRICDATASINFO']._serialized_end=745
  _globals['_METRICDATAANALYZEQUERY']._serialized_start=747
  _globals['_METRICDATAANALYZEQUERY']._serialized_end=851
  _globals['_METRICDATASTATQUERY']._serialized_start=853
  _globals['_METRICDATASTATQUERY']._serialized_end=947
  _globals['_METRICDATA']._serialized_start=950
  _globals['_METRICDATA']._serialized_end=1360
# @@protoc_insertion_point(module_scope)
