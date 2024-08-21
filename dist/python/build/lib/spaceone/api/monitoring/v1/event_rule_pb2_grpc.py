# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.monitoring.v1 import event_rule_pb2 as spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2

GRPC_GENERATED_VERSION = '1.65.5'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in spaceone/api/monitoring/v1/event_rule_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class EventRuleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EventRule/create',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.CreateEventRuleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EventRule/update',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.UpdateEventRuleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.FromString,
                _registered_method=True)
        self.change_order = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EventRule/change_order',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.ChangeEventRuleOrderRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EventRule/delete',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EventRule/get',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EventRule/list',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRulesInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EventRule/stat',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class EventRuleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Creates a new EventRule. You can filter the Events to apply the EventRule by setting the input parameter `Conditions`. The method can change the Events' assignee or Project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Changes a priority order between EventRules to apply. EventRules are filtered by the order configured.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def change_order(self, request, context):
        """Updates a specific EventRule. You can make changes in EventRule settings.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Deletes a specific EventRule. You must assign an EventRule resource to delete by specifying `event_rule_id`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Gets a specific EventRule. Prints detailed information about the EventRule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Gets a list of all EventRules. You can use a query to get a filtered list of EventRules. For example, you can adjust the scope of the list to a certain Project or Domain.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventRuleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.CreateEventRuleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.UpdateEventRuleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.SerializeToString,
            ),
            'change_order': grpc.unary_unary_rpc_method_handler(
                    servicer.change_order,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.ChangeEventRuleOrderRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRulesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.monitoring.v1.EventRule', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.monitoring.v1.EventRule', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EventRule(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.EventRule/create',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.CreateEventRuleRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.EventRule/update',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.UpdateEventRuleRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def change_order(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.EventRule/change_order',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.ChangeEventRuleOrderRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.EventRule/delete',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.EventRule/get',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.EventRule/list',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleQuery.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRulesInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def stat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.monitoring.v1.EventRule/stat',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__rule__pb2.EventRuleStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
