# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.inventory.plugin import collector_pb2 as spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2


class CollectorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.init = channel.unary_unary(
                '/spaceone.api.inventory.plugin.Collector/init',
                request_serializer=spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.InitRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.PluginInfo.FromString,
                )
        self.verify = channel.unary_unary(
                '/spaceone.api.inventory.plugin.Collector/verify',
                request_serializer=spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.VerifyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.collect = channel.unary_stream(
                '/spaceone.api.inventory.plugin.Collector/collect',
                request_serializer=spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.CollectRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.ResourceInfo.FromString,
                )


class CollectorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def init(self, request, context):
        """Initializes a specific Collector. During initialization, the Collector information to be passed to the Collector user is delivered as `metadata`. Collector information includes its name and version.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def verify(self, request, context):
        """Verifies a specific Collector. You must specify the parameter `secret_data`, encrypted account data of the Collector to validate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def collect(self, request, context):
        """Collects data of external infrastructure resources by a specific Collector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CollectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'init': grpc.unary_unary_rpc_method_handler(
                    servicer.init,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.InitRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.PluginInfo.SerializeToString,
            ),
            'verify': grpc.unary_unary_rpc_method_handler(
                    servicer.verify,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.VerifyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'collect': grpc.unary_stream_rpc_method_handler(
                    servicer.collect,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.CollectRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.ResourceInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.inventory.plugin.Collector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Collector(object):
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.plugin.Collector/init',
            spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.InitRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.PluginInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.plugin.Collector/verify',
            spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.VerifyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def collect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spaceone.api.inventory.plugin.Collector/collect',
            spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.CollectRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_plugin_dot_collector__pb2.ResourceInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)