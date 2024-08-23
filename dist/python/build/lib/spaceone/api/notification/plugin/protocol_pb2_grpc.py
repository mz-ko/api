# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.notification.plugin import protocol_pb2 as spaceone_dot_api_dot_notification_dot_plugin_dot_protocol__pb2

GRPC_GENERATED_VERSION = '1.66.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in spaceone/api/notification/plugin/protocol_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ProtocolStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.init = channel.unary_unary(
                '/spaceone.api.notification.plugin.Protocol/init',
                request_serializer=spaceone_dot_api_dot_notification_dot_plugin_dot_protocol__pb2.InitRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_plugin_dot_protocol__pb2.PluginInfo.FromString,
                _registered_method=True)
        self.verify = channel.unary_unary(
                '/spaceone.api.notification.plugin.Protocol/verify',
                request_serializer=spaceone_dot_api_dot_notification_dot_plugin_dot_protocol__pb2.PluginVerifyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class ProtocolServicer(object):
    """Missing associated documentation comment in .proto file."""

    def init(self, request, context):
        """Initializes a specific Protocol. During initialization, the Protocol information to be passed to the Protocol user is delivered as `metadata`. Protocol information includes its name and version.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def verify(self, request, context):
        """Verifies if a specific Protocol is a valid plugin instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProtocolServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'init': grpc.unary_unary_rpc_method_handler(
                    servicer.init,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_plugin_dot_protocol__pb2.InitRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_plugin_dot_protocol__pb2.PluginInfo.SerializeToString,
            ),
            'verify': grpc.unary_unary_rpc_method_handler(
                    servicer.verify,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_plugin_dot_protocol__pb2.PluginVerifyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.notification.plugin.Protocol', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.notification.plugin.Protocol', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Protocol(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def init(request,
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
            '/spaceone.api.notification.plugin.Protocol/init',
            spaceone_dot_api_dot_notification_dot_plugin_dot_protocol__pb2.InitRequest.SerializeToString,
            spaceone_dot_api_dot_notification_dot_plugin_dot_protocol__pb2.PluginInfo.FromString,
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
    def verify(request,
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
            '/spaceone.api.notification.plugin.Protocol/verify',
            spaceone_dot_api_dot_notification_dot_plugin_dot_protocol__pb2.PluginVerifyRequest.SerializeToString,
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
