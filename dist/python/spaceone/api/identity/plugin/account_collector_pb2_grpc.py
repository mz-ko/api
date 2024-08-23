# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from spaceone.api.identity.plugin import account_collector_pb2 as spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2

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
        + f' but the generated code in spaceone/api/identity/plugin/account_collector_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AccountCollectorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.init = channel.unary_unary(
                '/spaceone.api.identity.plugin.AccountCollector/init',
                request_serializer=spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.InitRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.PluginInfo.FromString,
                _registered_method=True)
        self.sync = channel.unary_unary(
                '/spaceone.api.identity.plugin.AccountCollector/sync',
                request_serializer=spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.SyncRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.AccountsInfo.FromString,
                _registered_method=True)


class AccountCollectorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def init(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountCollectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'init': grpc.unary_unary_rpc_method_handler(
                    servicer.init,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.InitRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.PluginInfo.SerializeToString,
            ),
            'sync': grpc.unary_unary_rpc_method_handler(
                    servicer.sync,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.SyncRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.AccountsInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.identity.plugin.AccountCollector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.identity.plugin.AccountCollector', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AccountCollector(object):
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
            '/spaceone.api.identity.plugin.AccountCollector/init',
            spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.InitRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.PluginInfo.FromString,
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
    def sync(request,
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
            '/spaceone.api.identity.plugin.AccountCollector/sync',
            spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.SyncRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_plugin_dot_account__collector__pb2.AccountsInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
