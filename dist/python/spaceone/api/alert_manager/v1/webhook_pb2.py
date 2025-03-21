# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/alert_manager/v1/webhook.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v2 import query_pb2 as spaceone_dot_api_dot_core_dot_v2_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+spaceone/api/alert_manager/v1/webhook.proto\x12\x1dspaceone.api.alert_manager.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"0\n\x14WebhookMessageFormat\x12\x0c\n\x04\x66rom\x18\x01 \x01(\t\x12\n\n\x02to\x18\x02 \x01(\t\"/\n\x0fWebhookRequests\x12\r\n\x05total\x18\x01 \x01(\x03\x12\r\n\x05\x65rror\x18\x02 \x01(\x03\"\xaa\x02\n\x11WebhookPluginInfo\x12\x11\n\tplugin_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12(\n\x07options\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12Y\n\x0cupgrade_mode\x18\x05 \x01(\x0e\x32\x43.spaceone.api.alert_manager.v1.WebhookPluginInfo.WebhookUpgradeMode\"A\n\x12WebhookUpgradeMode\x12\x15\n\x11UPGRADE_MODE_NONE\x10\x00\x12\x08\n\x04\x41UTO\x10\x01\x12\n\n\x06MANUAL\x10\x02\"\xf4\x01\n\x14WebhookCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x45\n\x0bplugin_info\x18\x02 \x01(\x0b\x32\x30.spaceone.api.alert_manager.v1.WebhookPluginInfo\x12L\n\x0fmessage_formats\x18\x03 \x03(\x0b\x32\x33.spaceone.api.alert_manager.v1.WebhookMessageFormat\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nservice_id\x18\x15 \x01(\t\"_\n\x14WebhookUpdateRequest\x12\x12\n\nwebhook_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\"\x85\x01\n!WebhookMessageFormatUpdateRequest\x12\x12\n\nwebhook_id\x18\x01 \x01(\t\x12L\n\x0fmessage_formats\x18\x02 \x03(\x0b\x32\x33.spaceone.api.alert_manager.v1.WebhookMessageFormat\"\x92\x02\n\x1aWebhookUpdatePluginRequest\x12\x12\n\nwebhook_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12(\n\x07options\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x62\n\x0cupgrade_mode\x18\x04 \x01(\x0e\x32L.spaceone.api.alert_manager.v1.WebhookUpdatePluginRequest.WebhookUpgradeMode\"A\n\x12WebhookUpgradeMode\x12\x15\n\x11UPGRADE_MODE_NONE\x10\x00\x12\x08\n\x04\x41UTO\x10\x01\x12\n\n\x06MANUAL\x10\x02\"$\n\x0eWebhookRequest\x12\x12\n\nwebhook_id\x18\x01 \x01(\t\"\xb2\x02\n\x12WebhookSearchQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x12\n\nwebhook_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12M\n\x05state\x18\x04 \x01(\x0e\x32>.spaceone.api.alert_manager.v1.WebhookSearchQuery.WebhookState\x12\x12\n\naccess_key\x18\x05 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\x12\x12\n\nservice_id\x18\x16 \x01(\t\"A\n\x0cWebhookState\x12\x16\n\x12WEBHOOK_STATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"H\n\x10WebhookStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery\"\xb2\x04\n\x0bWebhookInfo\x12\x12\n\nwebhook_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x46\n\x05state\x18\x03 \x01(\x0e\x32\x37.spaceone.api.alert_manager.v1.WebhookInfo.WebhookState\x12\x12\n\naccess_key\x18\x04 \x01(\t\x12\x13\n\x0bwebhook_url\x18\x05 \x01(\t\x12\x45\n\x0bplugin_info\x18\x06 \x01(\x0b\x32\x30.spaceone.api.alert_manager.v1.WebhookPluginInfo\x12@\n\x08requests\x18\x07 \x01(\x0b\x32..spaceone.api.alert_manager.v1.WebhookRequests\x12L\n\x0fmessage_formats\x18\x08 \x03(\x0b\x32\x33.spaceone.api.alert_manager.v1.WebhookMessageFormat\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x12\n\nservice_id\x18\x17 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\"A\n\x0cWebhookState\x12\x16\n\x12WEBHOOK_STATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"`\n\x0cWebhooksInfo\x12;\n\x07results\x18\x01 \x03(\x0b\x32*.spaceone.api.alert_manager.v1.WebhookInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"k\n\x17WebhookErrorSearchQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x12\n\nwebhook_id\x18\x02 \x01(\t\x12\x10\n\x08\x65rror_id\x18\x03 \x01(\t\"\xc5\x01\n\x10WebhookErrorInfo\x12\x10\n\x08\x65rror_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12)\n\x08raw_data\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x12\n\nservice_id\x18\x17 \x01(\t\x12\x12\n\nwebhook_id\x18\x18 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\"j\n\x11WebhookErrorsInfo\x12@\n\x07results\x18\x01 \x03(\x0b\x32/.spaceone.api.alert_manager.v1.WebhookErrorInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\x9c\r\n\x07Webhook\x12\x96\x01\n\x06\x63reate\x12\x33.spaceone.api.alert_manager.v1.WebhookCreateRequest\x1a*.spaceone.api.alert_manager.v1.WebhookInfo\"+\x82\xd3\xe4\x93\x02%\" /alert-manager/v1/webhook/create:\x01*\x12\x96\x01\n\x06update\x12\x33.spaceone.api.alert_manager.v1.WebhookUpdateRequest\x1a*.spaceone.api.alert_manager.v1.WebhookInfo\"+\x82\xd3\xe4\x93\x02%\" /alert-manager/v1/webhook/update:\x01*\x12\xc1\x01\n\x15update_message_format\x12@.spaceone.api.alert_manager.v1.WebhookMessageFormatUpdateRequest\x1a*.spaceone.api.alert_manager.v1.WebhookInfo\":\x82\xd3\xe4\x93\x02\x34\"//alert-manager/v1/webhook/update-message-format:\x01*\x12\xaa\x01\n\rupdate_plugin\x12\x39.spaceone.api.alert_manager.v1.WebhookUpdatePluginRequest\x1a*.spaceone.api.alert_manager.v1.WebhookInfo\"2\x82\xd3\xe4\x93\x02,\"\'/alert-manager/v1/webhook/update-plugin:\x01*\x12\x90\x01\n\x06\x65nable\x12-.spaceone.api.alert_manager.v1.WebhookRequest\x1a*.spaceone.api.alert_manager.v1.WebhookInfo\"+\x82\xd3\xe4\x93\x02%\" /alert-manager/v1/webhook/enable:\x01*\x12\x92\x01\n\x07\x64isable\x12-.spaceone.api.alert_manager.v1.WebhookRequest\x1a*.spaceone.api.alert_manager.v1.WebhookInfo\",\x82\xd3\xe4\x93\x02&\"!/alert-manager/v1/webhook/disable:\x01*\x12|\n\x06\x64\x65lete\x12-.spaceone.api.alert_manager.v1.WebhookRequest\x1a\x16.google.protobuf.Empty\"+\x82\xd3\xe4\x93\x02%\" /alert-manager/v1/webhook/delete:\x01*\x12\x8a\x01\n\x03get\x12-.spaceone.api.alert_manager.v1.WebhookRequest\x1a*.spaceone.api.alert_manager.v1.WebhookInfo\"(\x82\xd3\xe4\x93\x02\"\"\x1d/alert-manager/v1/webhook/get:\x01*\x12\x91\x01\n\x04list\x12\x31.spaceone.api.alert_manager.v1.WebhookSearchQuery\x1a+.spaceone.api.alert_manager.v1.WebhooksInfo\")\x82\xd3\xe4\x93\x02#\"\x1e/alert-manager/v1/webhook/list:\x01*\x12\xa9\x01\n\x0blist_errors\x12\x36.spaceone.api.alert_manager.v1.WebhookErrorSearchQuery\x1a\x30.spaceone.api.alert_manager.v1.WebhookErrorsInfo\"0\x82\xd3\xe4\x93\x02*\"%/alert-manager/v1/webhook/list-errors:\x01*\x12{\n\x04stat\x12/.spaceone.api.alert_manager.v1.WebhookStatQuery\x1a\x17.google.protobuf.Struct\")\x82\xd3\xe4\x93\x02#\"\x1e/alert-manager/v1/webhook/stat:\x01*BDZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/alert-manager/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.alert_manager.v1.webhook_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/alert-manager/v1'
  _globals['_WEBHOOK'].methods_by_name['create']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['create']._serialized_options = b'\202\323\344\223\002%\" /alert-manager/v1/webhook/create:\001*'
  _globals['_WEBHOOK'].methods_by_name['update']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['update']._serialized_options = b'\202\323\344\223\002%\" /alert-manager/v1/webhook/update:\001*'
  _globals['_WEBHOOK'].methods_by_name['update_message_format']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['update_message_format']._serialized_options = b'\202\323\344\223\0024\"//alert-manager/v1/webhook/update-message-format:\001*'
  _globals['_WEBHOOK'].methods_by_name['update_plugin']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['update_plugin']._serialized_options = b'\202\323\344\223\002,\"\'/alert-manager/v1/webhook/update-plugin:\001*'
  _globals['_WEBHOOK'].methods_by_name['enable']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['enable']._serialized_options = b'\202\323\344\223\002%\" /alert-manager/v1/webhook/enable:\001*'
  _globals['_WEBHOOK'].methods_by_name['disable']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['disable']._serialized_options = b'\202\323\344\223\002&\"!/alert-manager/v1/webhook/disable:\001*'
  _globals['_WEBHOOK'].methods_by_name['delete']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002%\" /alert-manager/v1/webhook/delete:\001*'
  _globals['_WEBHOOK'].methods_by_name['get']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002\"\"\035/alert-manager/v1/webhook/get:\001*'
  _globals['_WEBHOOK'].methods_by_name['list']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002#\"\036/alert-manager/v1/webhook/list:\001*'
  _globals['_WEBHOOK'].methods_by_name['list_errors']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['list_errors']._serialized_options = b'\202\323\344\223\002*\"%/alert-manager/v1/webhook/list-errors:\001*'
  _globals['_WEBHOOK'].methods_by_name['stat']._loaded_options = None
  _globals['_WEBHOOK'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002#\"\036/alert-manager/v1/webhook/stat:\001*'
  _globals['_WEBHOOKMESSAGEFORMAT']._serialized_start=201
  _globals['_WEBHOOKMESSAGEFORMAT']._serialized_end=249
  _globals['_WEBHOOKREQUESTS']._serialized_start=251
  _globals['_WEBHOOKREQUESTS']._serialized_end=298
  _globals['_WEBHOOKPLUGININFO']._serialized_start=301
  _globals['_WEBHOOKPLUGININFO']._serialized_end=599
  _globals['_WEBHOOKPLUGININFO_WEBHOOKUPGRADEMODE']._serialized_start=534
  _globals['_WEBHOOKPLUGININFO_WEBHOOKUPGRADEMODE']._serialized_end=599
  _globals['_WEBHOOKCREATEREQUEST']._serialized_start=602
  _globals['_WEBHOOKCREATEREQUEST']._serialized_end=846
  _globals['_WEBHOOKUPDATEREQUEST']._serialized_start=848
  _globals['_WEBHOOKUPDATEREQUEST']._serialized_end=943
  _globals['_WEBHOOKMESSAGEFORMATUPDATEREQUEST']._serialized_start=946
  _globals['_WEBHOOKMESSAGEFORMATUPDATEREQUEST']._serialized_end=1079
  _globals['_WEBHOOKUPDATEPLUGINREQUEST']._serialized_start=1082
  _globals['_WEBHOOKUPDATEPLUGINREQUEST']._serialized_end=1356
  _globals['_WEBHOOKUPDATEPLUGINREQUEST_WEBHOOKUPGRADEMODE']._serialized_start=534
  _globals['_WEBHOOKUPDATEPLUGINREQUEST_WEBHOOKUPGRADEMODE']._serialized_end=599
  _globals['_WEBHOOKREQUEST']._serialized_start=1358
  _globals['_WEBHOOKREQUEST']._serialized_end=1394
  _globals['_WEBHOOKSEARCHQUERY']._serialized_start=1397
  _globals['_WEBHOOKSEARCHQUERY']._serialized_end=1703
  _globals['_WEBHOOKSEARCHQUERY_WEBHOOKSTATE']._serialized_start=1638
  _globals['_WEBHOOKSEARCHQUERY_WEBHOOKSTATE']._serialized_end=1703
  _globals['_WEBHOOKSTATQUERY']._serialized_start=1705
  _globals['_WEBHOOKSTATQUERY']._serialized_end=1777
  _globals['_WEBHOOKINFO']._serialized_start=1780
  _globals['_WEBHOOKINFO']._serialized_end=2342
  _globals['_WEBHOOKINFO_WEBHOOKSTATE']._serialized_start=1638
  _globals['_WEBHOOKINFO_WEBHOOKSTATE']._serialized_end=1703
  _globals['_WEBHOOKSINFO']._serialized_start=2344
  _globals['_WEBHOOKSINFO']._serialized_end=2440
  _globals['_WEBHOOKERRORSEARCHQUERY']._serialized_start=2442
  _globals['_WEBHOOKERRORSEARCHQUERY']._serialized_end=2549
  _globals['_WEBHOOKERRORINFO']._serialized_start=2552
  _globals['_WEBHOOKERRORINFO']._serialized_end=2749
  _globals['_WEBHOOKERRORSINFO']._serialized_start=2751
  _globals['_WEBHOOKERRORSINFO']._serialized_end=2857
  _globals['_WEBHOOK']._serialized_start=2860
  _globals['_WEBHOOK']._serialized_end=4552
# @@protoc_insertion_point(module_scope)
