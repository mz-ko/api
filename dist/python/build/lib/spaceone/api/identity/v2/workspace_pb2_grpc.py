# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.identity.v2 import workspace_pb2 as spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2

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
        + f' but the generated code in spaceone/api/identity/v2/workspace_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class WorkspaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.identity.v2.Workspace/create',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.CreateWorkSpaceRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.identity.v2.Workspace/update',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.UpdateWorkSpaceRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.identity.v2.Workspace/delete',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceDeleteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.enable = channel.unary_unary(
                '/spaceone.api.identity.v2.Workspace/enable',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.FromString,
                _registered_method=True)
        self.disable = channel.unary_unary(
                '/spaceone.api.identity.v2.Workspace/disable',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.identity.v2.Workspace/get',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.FromString,
                _registered_method=True)
        self.check = channel.unary_unary(
                '/spaceone.api.identity.v2.Workspace/check',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceCheckRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.identity.v2.Workspace/list',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceSearchQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspacesInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.identity.v2.Workspace/stat',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class WorkspaceServicer(object):
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

    def enable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def check(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkspaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.CreateWorkSpaceRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.UpdateWorkSpaceRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceDeleteRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'enable': grpc.unary_unary_rpc_method_handler(
                    servicer.enable,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.SerializeToString,
            ),
            'disable': grpc.unary_unary_rpc_method_handler(
                    servicer.disable,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.SerializeToString,
            ),
            'check': grpc.unary_unary_rpc_method_handler(
                    servicer.check,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceCheckRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceSearchQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspacesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.identity.v2.Workspace', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.identity.v2.Workspace', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Workspace(object):
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
            '/spaceone.api.identity.v2.Workspace/create',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.CreateWorkSpaceRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.FromString,
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
            '/spaceone.api.identity.v2.Workspace/update',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.UpdateWorkSpaceRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.FromString,
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
            '/spaceone.api.identity.v2.Workspace/delete',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceDeleteRequest.SerializeToString,
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
    def enable(request,
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
            '/spaceone.api.identity.v2.Workspace/enable',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.FromString,
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
    def disable(request,
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
            '/spaceone.api.identity.v2.Workspace/disable',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.FromString,
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
            '/spaceone.api.identity.v2.Workspace/get',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceInfo.FromString,
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
    def check(request,
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
            '/spaceone.api.identity.v2.Workspace/check',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceCheckRequest.SerializeToString,
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
            '/spaceone.api.identity.v2.Workspace/list',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceSearchQuery.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspacesInfo.FromString,
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
            '/spaceone.api.identity.v2.Workspace/stat',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__pb2.WorkspaceStatQuery.SerializeToString,
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
