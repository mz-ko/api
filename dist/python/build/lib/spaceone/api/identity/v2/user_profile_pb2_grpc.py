# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.identity.v2 import user_pb2 as spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2
from spaceone.api.identity.v2 import user_profile_pb2 as spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2

GRPC_GENERATED_VERSION = '1.64.1'
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
        + f' but the generated code in spaceone/api/identity/v2/user_profile_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class UserProfileStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.update = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/update',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UpdateUserProfileRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
                _registered_method=True)
        self.set_refresh_timeout = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/set_refresh_timeout',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.SetRefreshTimeout.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
                _registered_method=True)
        self.verify_email = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/verify_email',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.VerifyEmailRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.confirm_email = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/confirm_email',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.ConfirmEmailRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
                _registered_method=True)
        self.reset_password = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/reset_password',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UserPasswordResetRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.enable_mfa = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/enable_mfa',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.EnableMFARequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
                _registered_method=True)
        self.disable_mfa = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/disable_mfa',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.DisableMFARequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
                _registered_method=True)
        self.confirm_mfa = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/confirm_mfa',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.ConfirmMFARequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/get',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UserProfileRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
                _registered_method=True)
        self.get_workspaces = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/get_workspaces',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UserProfileRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.MyWorkspacesInfo.FromString,
                _registered_method=True)
        self.get_workspace_groups = channel.unary_unary(
                '/spaceone.api.identity.v2.UserProfile/get_workspace_groups',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.WorkspaceGroupUserProfileRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.MyWorkspaceGroupsInfo.FromString,
                _registered_method=True)


class UserProfileServicer(object):
    """Missing associated documentation comment in .proto file."""

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_refresh_timeout(self, request, context):
        """Sets the user's refresh token timeout. This API can only be used by users with the `DOMAIN_ADMIN` role.
        Min value is `1800` seconds and max value is `2592000` seconds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def verify_email(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def confirm_email(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def reset_password(self, request, context):
        """+noauth
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def enable_mfa(self, request, context):
        """Enable MFA for user. If this api is called, send email to user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disable_mfa(self, request, context):
        """Disable MFA for user. If this api is called, send email to user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def confirm_mfa(self, request, context):
        """Confirm MFA for user by given verify_code which is sent by your authentication method.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_workspaces(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_workspace_groups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserProfileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UpdateUserProfileRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.SerializeToString,
            ),
            'set_refresh_timeout': grpc.unary_unary_rpc_method_handler(
                    servicer.set_refresh_timeout,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.SetRefreshTimeout.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.SerializeToString,
            ),
            'verify_email': grpc.unary_unary_rpc_method_handler(
                    servicer.verify_email,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.VerifyEmailRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'confirm_email': grpc.unary_unary_rpc_method_handler(
                    servicer.confirm_email,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.ConfirmEmailRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.SerializeToString,
            ),
            'reset_password': grpc.unary_unary_rpc_method_handler(
                    servicer.reset_password,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UserPasswordResetRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'enable_mfa': grpc.unary_unary_rpc_method_handler(
                    servicer.enable_mfa,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.EnableMFARequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.SerializeToString,
            ),
            'disable_mfa': grpc.unary_unary_rpc_method_handler(
                    servicer.disable_mfa,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.DisableMFARequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.SerializeToString,
            ),
            'confirm_mfa': grpc.unary_unary_rpc_method_handler(
                    servicer.confirm_mfa,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.ConfirmMFARequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UserProfileRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.SerializeToString,
            ),
            'get_workspaces': grpc.unary_unary_rpc_method_handler(
                    servicer.get_workspaces,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UserProfileRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.MyWorkspacesInfo.SerializeToString,
            ),
            'get_workspace_groups': grpc.unary_unary_rpc_method_handler(
                    servicer.get_workspace_groups,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.WorkspaceGroupUserProfileRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.MyWorkspaceGroupsInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.identity.v2.UserProfile', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.identity.v2.UserProfile', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserProfile(object):
    """Missing associated documentation comment in .proto file."""

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
            '/spaceone.api.identity.v2.UserProfile/update',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UpdateUserProfileRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
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
    def set_refresh_timeout(request,
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
            '/spaceone.api.identity.v2.UserProfile/set_refresh_timeout',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.SetRefreshTimeout.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
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
    def verify_email(request,
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
            '/spaceone.api.identity.v2.UserProfile/verify_email',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.VerifyEmailRequest.SerializeToString,
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
    def confirm_email(request,
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
            '/spaceone.api.identity.v2.UserProfile/confirm_email',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.ConfirmEmailRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
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
    def reset_password(request,
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
            '/spaceone.api.identity.v2.UserProfile/reset_password',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UserPasswordResetRequest.SerializeToString,
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
    def enable_mfa(request,
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
            '/spaceone.api.identity.v2.UserProfile/enable_mfa',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.EnableMFARequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
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
    def disable_mfa(request,
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
            '/spaceone.api.identity.v2.UserProfile/disable_mfa',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.DisableMFARequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
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
    def confirm_mfa(request,
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
            '/spaceone.api.identity.v2.UserProfile/confirm_mfa',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.ConfirmMFARequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
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
            '/spaceone.api.identity.v2.UserProfile/get',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UserProfileRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_user__pb2.UserInfo.FromString,
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
    def get_workspaces(request,
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
            '/spaceone.api.identity.v2.UserProfile/get_workspaces',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.UserProfileRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.MyWorkspacesInfo.FromString,
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
    def get_workspace_groups(request,
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
            '/spaceone.api.identity.v2.UserProfile/get_workspace_groups',
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.WorkspaceGroupUserProfileRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_user__profile__pb2.MyWorkspaceGroupsInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
