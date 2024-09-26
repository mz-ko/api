# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/cost_analysis/v1/unified_cost.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.core.v2 import query_pb2 as spaceone_dot_api_dot_core_dot_v2_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0spaceone/api/cost_analysis/v1/unified_cost.proto\x12\x1dspaceone.api.cost_analysis.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a spaceone/api/core/v2/query.proto\"-\n\x12UnifiedCostRequest\x12\x17\n\x0funified_cost_id\x18\x01 \x01(\t\"W\n\x10UnifiedCostQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x17\n\x0funified_cost_id\x18\x02 \x01(\t\"l\n\x17UnifiedCostAnalyzeQuery\x12;\n\x05query\x18\x01 \x01(\x0b\x32,.spaceone.api.core.v2.TimeSeriesAnalyzeQuery\x12\x14\n\x0cis_confirmed\x18\x02 \x01(\x08\"\xcd\x04\n\x0fUnifiedCostInfo\x12\x17\n\x0funified_cost_id\x18\x01 \x01(\t\x12%\n\x04\x63ost\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x14\n\x0c\x62illed_month\x18\x03 \x01(\t\x12\x13\n\x0b\x62illed_year\x18\x04 \x01(\t\x12\x18\n\x10\x61ggregation_date\x18\x05 \x01(\t\x12\x15\n\rexchange_date\x18\x06 \x01(\t\x12\x17\n\x0f\x65xchange_source\x18\x07 \x01(\t\x12\x10\n\x08\x63urrency\x18\x08 \x01(\t\x12\x14\n\x0cis_confirmed\x18\t \x01(\x08\x12\x10\n\x08provider\x18\n \x01(\t\x12\x13\n\x0bregion_code\x18\x0b \x01(\t\x12\x12\n\nregion_key\x18\x0c \x01(\t\x12\x0f\n\x07product\x18\r \x01(\t\x12\x12\n\nusage_type\x18\x0e \x01(\t\x12\x12\n\nusage_unit\x18\x0f \x01(\t\x12\x1c\n\x14service_account_name\x18\x10 \x01(\t\x12\x18\n\x10\x64\x61ta_source_name\x18\x11 \x01(\t\x12\x14\n\x0cproject_name\x18\x12 \x01(\t\x12\x16\n\x0eworkspace_name\x18\x13 \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x12\n\nproject_id\x18\x17 \x01(\t\x12\x16\n\x0e\x64\x61ta_source_id\x18\x1a \x01(\t\x12\x1a\n\x12service_account_id\x18\x1b \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\"h\n\x10UnifiedCostsInfo\x12?\n\x07results\x18\x01 \x03(\x0b\x32..spaceone.api.cost_analysis.v1.UnifiedCostInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"L\n\x14UnifiedCostStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery2\xd9\x04\n\x0bUnifiedCost\x12\x97\x01\n\x03get\x12\x31.spaceone.api.cost_analysis.v1.UnifiedCostRequest\x1a..spaceone.api.cost_analysis.v1.UnifiedCostInfo\"-\x82\xd3\xe4\x93\x02\'\"\"/cost-analysis/v1/unified-cost/get:\x01*\x12\x98\x01\n\x04list\x12/.spaceone.api.cost_analysis.v1.UnifiedCostQuery\x1a/.spaceone.api.cost_analysis.v1.UnifiedCostsInfo\".\x82\xd3\xe4\x93\x02(\"#/cost-analysis/v1/unified-cost/list:\x01*\x12\x8d\x01\n\x07\x61nalyze\x12\x36.spaceone.api.cost_analysis.v1.UnifiedCostAnalyzeQuery\x1a\x17.google.protobuf.Struct\"1\x82\xd3\xe4\x93\x02+\"&/cost-analysis/v1/unified-cost/analyze:\x01*\x12\x84\x01\n\x04stat\x12\x33.spaceone.api.cost_analysis.v1.UnifiedCostStatQuery\x1a\x17.google.protobuf.Struct\".\x82\xd3\xe4\x93\x02(\"#/cost-analysis/v1/unified-cost/stat:\x01*BDZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/cost_analysis/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.cost_analysis.v1.unified_cost_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/cost_analysis/v1'
  _globals['_UNIFIEDCOST'].methods_by_name['get']._loaded_options = None
  _globals['_UNIFIEDCOST'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002\'\"\"/cost-analysis/v1/unified-cost/get:\001*'
  _globals['_UNIFIEDCOST'].methods_by_name['list']._loaded_options = None
  _globals['_UNIFIEDCOST'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002(\"#/cost-analysis/v1/unified-cost/list:\001*'
  _globals['_UNIFIEDCOST'].methods_by_name['analyze']._loaded_options = None
  _globals['_UNIFIEDCOST'].methods_by_name['analyze']._serialized_options = b'\202\323\344\223\002+\"&/cost-analysis/v1/unified-cost/analyze:\001*'
  _globals['_UNIFIEDCOST'].methods_by_name['stat']._loaded_options = None
  _globals['_UNIFIEDCOST'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002(\"#/cost-analysis/v1/unified-cost/stat:\001*'
  _globals['_UNIFIEDCOSTREQUEST']._serialized_start=206
  _globals['_UNIFIEDCOSTREQUEST']._serialized_end=251
  _globals['_UNIFIEDCOSTQUERY']._serialized_start=253
  _globals['_UNIFIEDCOSTQUERY']._serialized_end=340
  _globals['_UNIFIEDCOSTANALYZEQUERY']._serialized_start=342
  _globals['_UNIFIEDCOSTANALYZEQUERY']._serialized_end=450
  _globals['_UNIFIEDCOSTINFO']._serialized_start=453
  _globals['_UNIFIEDCOSTINFO']._serialized_end=1042
  _globals['_UNIFIEDCOSTSINFO']._serialized_start=1044
  _globals['_UNIFIEDCOSTSINFO']._serialized_end=1148
  _globals['_UNIFIEDCOSTSTATQUERY']._serialized_start=1150
  _globals['_UNIFIEDCOSTSTATQUERY']._serialized_end=1226
  _globals['_UNIFIEDCOST']._serialized_start=1229
  _globals['_UNIFIEDCOST']._serialized_end=1830
# @@protoc_insertion_point(module_scope)