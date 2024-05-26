# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.dashboard.v1 import public_data_table_pb2 as spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in spaceone/api/dashboard/v1/public_data_table_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class PublicDataTableStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.data_table.v1.PublicDataTable/create',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.CreatePublicDataTableRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.data_table.v1.PublicDataTable/update',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.UpdatePublicDataTableRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.data_table.v1.PublicDataTable/delete',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.load = channel.unary_unary(
                '/spaceone.api.data_table.v1.PublicDataTable/load',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.LoadPublicDataTableRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.data_table.v1.PublicDataTable/get',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.data_table.v1.PublicDataTable/list',
                request_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTablesInfo.FromString,
                _registered_method=True)


class PublicDataTableServicer(object):
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


def add_PublicDataTableServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.CreatePublicDataTableRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.UpdatePublicDataTableRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'load': grpc.unary_unary_rpc_method_handler(
                    servicer.load,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.LoadPublicDataTableRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTablesInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.data_table.v1.PublicDataTable', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.data_table.v1.PublicDataTable', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PublicDataTable(object):
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
            '/spaceone.api.data_table.v1.PublicDataTable/create',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.CreatePublicDataTableRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.FromString,
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
            '/spaceone.api.data_table.v1.PublicDataTable/update',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.UpdatePublicDataTableRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.FromString,
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
            '/spaceone.api.data_table.v1.PublicDataTable/delete',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableRequest.SerializeToString,
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
            '/spaceone.api.data_table.v1.PublicDataTable/load',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.LoadPublicDataTableRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.FromString,
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
            '/spaceone.api.data_table.v1.PublicDataTable/get',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableRequest.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableInfo.FromString,
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
            '/spaceone.api.data_table.v1.PublicDataTable/list',
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTableQuery.SerializeToString,
            spaceone_dot_api_dot_dashboard_dot_v1_dot_public__data__table__pb2.PublicDataTablesInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
