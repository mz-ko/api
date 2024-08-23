# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.secret.v1 import trusted_secret_pb2 as spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2

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
        + f' but the generated code in spaceone/api/secret/v1/trusted_secret_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TrustedSecretStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.secret.v1.TrustedSecret/create',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.CreateTrustedSecretRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.secret.v1.TrustedSecret/update',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.UpdateTrustedSecretRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.secret.v1.TrustedSecret/delete',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.update_data = channel.unary_unary(
                '/spaceone.api.secret.v1.TrustedSecret/update_data',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.UpdateTrustedSecretDataRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get_data = channel.unary_unary(
                '/spaceone.api.secret.v1.TrustedSecret/get_data',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.GetTrustedSecretDataRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretDataInfo.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.secret.v1.TrustedSecret/get',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.secret.v1.TrustedSecret/list',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretsInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.secret.v1.TrustedSecret/stat',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class TrustedSecretServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Create a new trusted secret.
        Created trusted secret is encrypted and stored securely.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Updates a specific trusted secret's information.
        You can only change the 'name' and 'tags', and to change the data you must use the update_data API.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Deletes a specific trusted secret.
        If a trusted secret is attached to a Secret, it cannot be deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_data(self, request, context):
        """Updates a specific trusted secret's data.
        Updated trusted secret is encrypted and stored securely.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_data(self, request, context):
        """Get a specific secret's data.
        This API is for internal system use only.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Get a specific trusted secret's information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Queries a list of trusted secrets.
        You can use a query to get a filtered list of trusted secrets.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrustedSecretServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.CreateTrustedSecretRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.UpdateTrustedSecretRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'update_data': grpc.unary_unary_rpc_method_handler(
                    servicer.update_data,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.UpdateTrustedSecretDataRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get_data': grpc.unary_unary_rpc_method_handler(
                    servicer.get_data,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.GetTrustedSecretDataRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretDataInfo.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.secret.v1.TrustedSecret', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.secret.v1.TrustedSecret', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TrustedSecret(object):
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
            '/spaceone.api.secret.v1.TrustedSecret/create',
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.CreateTrustedSecretRequest.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretInfo.FromString,
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
            '/spaceone.api.secret.v1.TrustedSecret/update',
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.UpdateTrustedSecretRequest.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretInfo.FromString,
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
            '/spaceone.api.secret.v1.TrustedSecret/delete',
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretRequest.SerializeToString,
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
    def update_data(request,
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
            '/spaceone.api.secret.v1.TrustedSecret/update_data',
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.UpdateTrustedSecretDataRequest.SerializeToString,
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
    def get_data(request,
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
            '/spaceone.api.secret.v1.TrustedSecret/get_data',
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.GetTrustedSecretDataRequest.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretDataInfo.FromString,
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
            '/spaceone.api.secret.v1.TrustedSecret/get',
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretRequest.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretInfo.FromString,
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
            '/spaceone.api.secret.v1.TrustedSecret/list',
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretQuery.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretsInfo.FromString,
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
            '/spaceone.api.secret.v1.TrustedSecret/stat',
            spaceone_dot_api_dot_secret_dot_v1_dot_trusted__secret__pb2.TrustedSecretStatQuery.SerializeToString,
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
