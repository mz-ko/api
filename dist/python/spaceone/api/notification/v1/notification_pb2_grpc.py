# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.notification.v1 import notification_pb2 as spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2

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
        + f' but the generated code in spaceone/api/notification/v1/notification_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NotificationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.notification.v1.Notification/create',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.CreateNotificationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.push = channel.unary_unary(
                '/spaceone.api.notification.v1.Notification/push',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.PushNotificationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.notification.v1.Notification/delete',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.set_read = channel.unary_unary(
                '/spaceone.api.notification.v1.Notification/set_read',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.notification.v1.Notification/get',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.GetNotificationRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.notification.v1.Notification/list',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationsInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.notification.v1.Notification/stat',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class NotificationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Creates a new Notification. When a Notification is created, it is delivered to a UserChannel or a ProjectChannel depending on the parameter `resource_type`. If a Notification is delivered to a UserChannel, the `resource_type` is `identity.User`, and if a Notification is delivered to a ProjectChannel, the `resource_type` is `identity.Project`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def push(self, request, context):
        """Manually raises a Notification. A Notification is raised with a message to be sent using a valid specific Protocol, and data used for a specific Protocol such as a phone number.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Deletes multiple Notifications. You must specify `notifications` of the list of Notifications to delete.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_read(self, request, context):
        """Marks a Notification as read. When a Notification is raised and if the Notification has been acknowledged, it can be marked as read with the method.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Gets a specific Notification. Prints detailed information about the Notification, including not only the message contents(`title`, `description`) but also related data such as created time and urgency.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Gets a list of all Notifications. You can use a query to get a filtered list of Notifications.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotificationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.CreateNotificationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'push': grpc.unary_unary_rpc_method_handler(
                    servicer.push,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.PushNotificationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'set_read': grpc.unary_unary_rpc_method_handler(
                    servicer.set_read,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.GetNotificationRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.notification.v1.Notification', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.notification.v1.Notification', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Notification(object):
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
            '/spaceone.api.notification.v1.Notification/create',
            spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.CreateNotificationRequest.SerializeToString,
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
    def push(request,
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
            '/spaceone.api.notification.v1.Notification/push',
            spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.PushNotificationRequest.SerializeToString,
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
            '/spaceone.api.notification.v1.Notification/delete',
            spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationsRequest.SerializeToString,
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
    def set_read(request,
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
            '/spaceone.api.notification.v1.Notification/set_read',
            spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationsRequest.SerializeToString,
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
            '/spaceone.api.notification.v1.Notification/get',
            spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.GetNotificationRequest.SerializeToString,
            spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationInfo.FromString,
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
            '/spaceone.api.notification.v1.Notification/list',
            spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationQuery.SerializeToString,
            spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationsInfo.FromString,
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
            '/spaceone.api.notification.v1.Notification/stat',
            spaceone_dot_api_dot_notification_dot_v1_dot_notification__pb2.NotificationStatQuery.SerializeToString,
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
