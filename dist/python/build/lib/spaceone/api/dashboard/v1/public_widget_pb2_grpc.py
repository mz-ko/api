# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.dashboard.v1 import public_widget_pb2 as spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2

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
        + f' but the generated code in spaceone/api/dashboard/v1/public_widget_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class PublicWidgetStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicWidget/create',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.CreatePublicWidgetRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicWidget/update',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.UpdatePublicWidgetRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicWidget/delete',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.load = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicWidget/load',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.LoadPublicWidgetRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicWidget/get',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.dashboard.v1.PublicWidget/list',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetsInfo.FromString,
                _registered_method=True)


class PublicWidgetServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def load(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PublicWidgetServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.CreatePublicWidgetRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.UpdatePublicWidgetRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'load': grpc.unary_unary_rpc_method_handler(
                    servicer.load,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.LoadPublicWidgetRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetsInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.dashboard.v1.PublicWidget', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.dashboard.v1.PublicWidget', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PublicWidget(object):
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
            '/spaceone.api.dashboard.v1.PublicWidget/create',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.CreatePublicWidgetRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetInfo.FromString,
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
            '/spaceone.api.dashboard.v1.PublicWidget/update',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.UpdatePublicWidgetRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetInfo.FromString,
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
            '/spaceone.api.dashboard.v1.PublicWidget/delete',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetRequest.SerializeToString,
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
    def load(request,
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
            '/spaceone.api.dashboard.v1.PublicWidget/load',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.LoadPublicWidgetRequest.SerializeToString,
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
            '/spaceone.api.dashboard.v1.PublicWidget/get',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetInfo.FromString,
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
            '/spaceone.api.dashboard.v1.PublicWidget/list',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetQuery.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__widget__pb2.PublicWidgetsInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
