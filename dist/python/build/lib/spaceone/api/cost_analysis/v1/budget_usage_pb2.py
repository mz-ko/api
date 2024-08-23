# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: spaceone/api/cost_analysis/v1/budget_usage.proto
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
    'spaceone/api/cost_analysis/v1/budget_usage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v2 import query_pb2 as spaceone_dot_api_dot_core_dot_v2_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0spaceone/api/cost_analysis/v1/budget_usage.proto\x12\x1dspaceone.api.cost_analysis.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"\xb1\x01\n\x19\x42udgetUsageProviderFilter\x12M\n\x05state\x18\x01 \x01(\x0e\x32>.spaceone.api.cost_analysis.v1.BudgetUsageProviderFilter.State\x12\x11\n\tproviders\x18\x02 \x03(\t\"2\n\x05State\x12\x0e\n\nSTATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\xaf\x01\n\x10\x42udgetUsageQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\x12\x12\n\nproject_id\x18\x16 \x01(\t\x12\x11\n\tbudget_id\x18\x17 \x01(\t\x12\x16\n\x0e\x64\x61ta_source_id\x18\x18 \x01(\t\"\xc7\x03\n\x0f\x42udgetUsageInfo\x12\x11\n\tbudget_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x0c\n\x04\x63ost\x18\x05 \x01(\x02\x12\r\n\x05limit\x18\x06 \x01(\x02\x12\x10\n\x08\x63urrency\x18\x07 \x01(\t\x12Q\n\x0fprovider_filter\x18\x08 \x01(\x0b\x32\x38.spaceone.api.cost_analysis.v1.BudgetUsageProviderFilter\x12T\n\x0eresource_group\x18\t \x01(\x0e\x32<.spaceone.api.cost_analysis.v1.BudgetUsageInfo.ResourceGroup\x12\x16\n\x0e\x64\x61ta_source_id\x18\r \x01(\t\x12\x12\n\nproject_id\x18\x13 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x14 \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x12\n\nupdated_at\x18\x1f \x01(\t\"D\n\rResourceGroup\x12\x17\n\x13RESOURCE_GROUP_NONE\x10\x00\x12\r\n\tWORKSPACE\x10\x01\x12\x0b\n\x07PROJECT\x10\x02\"h\n\x10\x42udgetUsagesInfo\x12?\n\x07results\x18\x01 \x03(\x0b\x32..spaceone.api.cost_analysis.v1.BudgetUsageInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"\x81\x01\n\x17\x42udgetUsageAnalyzeQuery\x12;\n\x05query\x18\x01 \x01(\x0b\x32,.spaceone.api.core.v2.TimeSeriesAnalyzeQuery\x12\x11\n\tbudget_id\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x61ta_source_id\x18\x03 \x01(\t\"w\n\x14\x42udgetUsageStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery\x12\x11\n\tbudget_id\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x61ta_source_id\x18\x03 \x01(\t2\xbf\x03\n\x0b\x42udgetUsage\x12\x98\x01\n\x04list\x12/.spaceone.api.cost_analysis.v1.BudgetUsageQuery\x1a/.spaceone.api.cost_analysis.v1.BudgetUsagesInfo\".\x82\xd3\xe4\x93\x02(\"#/cost-analysis/v1/budget-usage/list:\x01*\x12\x8d\x01\n\x07\x61nalyze\x12\x36.spaceone.api.cost_analysis.v1.BudgetUsageAnalyzeQuery\x1a\x17.google.protobuf.Struct\"1\x82\xd3\xe4\x93\x02+\"&/cost-analysis/v1/budget-usage/analyze:\x01*\x12\x84\x01\n\x04stat\x12\x33.spaceone.api.cost_analysis.v1.BudgetUsageStatQuery\x1a\x17.google.protobuf.Struct\".\x82\xd3\xe4\x93\x02(\"#/cost-analysis/v1/budget-usage/stat:\x01*BDZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/cost_analysis/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.cost_analysis.v1.budget_usage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/cost_analysis/v1'
  _globals['_BUDGETUSAGE'].methods_by_name['list']._loaded_options = None
  _globals['_BUDGETUSAGE'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002(\"#/cost-analysis/v1/budget-usage/list:\001*'
  _globals['_BUDGETUSAGE'].methods_by_name['analyze']._loaded_options = None
  _globals['_BUDGETUSAGE'].methods_by_name['analyze']._serialized_options = b'\202\323\344\223\002+\"&/cost-analysis/v1/budget-usage/analyze:\001*'
  _globals['_BUDGETUSAGE'].methods_by_name['stat']._loaded_options = None
  _globals['_BUDGETUSAGE'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002(\"#/cost-analysis/v1/budget-usage/stat:\001*'
  _globals['_BUDGETUSAGEPROVIDERFILTER']._serialized_start=178
  _globals['_BUDGETUSAGEPROVIDERFILTER']._serialized_end=355
  _globals['_BUDGETUSAGEPROVIDERFILTER_STATE']._serialized_start=305
  _globals['_BUDGETUSAGEPROVIDERFILTER_STATE']._serialized_end=355
  _globals['_BUDGETUSAGEQUERY']._serialized_start=358
  _globals['_BUDGETUSAGEQUERY']._serialized_end=533
  _globals['_BUDGETUSAGEINFO']._serialized_start=536
  _globals['_BUDGETUSAGEINFO']._serialized_end=991
  _globals['_BUDGETUSAGEINFO_RESOURCEGROUP']._serialized_start=923
  _globals['_BUDGETUSAGEINFO_RESOURCEGROUP']._serialized_end=991
  _globals['_BUDGETUSAGESINFO']._serialized_start=993
  _globals['_BUDGETUSAGESINFO']._serialized_end=1097
  _globals['_BUDGETUSAGEANALYZEQUERY']._serialized_start=1100
  _globals['_BUDGETUSAGEANALYZEQUERY']._serialized_end=1229
  _globals['_BUDGETUSAGESTATQUERY']._serialized_start=1231
  _globals['_BUDGETUSAGESTATQUERY']._serialized_end=1350
  _globals['_BUDGETUSAGE']._serialized_start=1353
  _globals['_BUDGETUSAGE']._serialized_end=1800
# @@protoc_insertion_point(module_scope)
