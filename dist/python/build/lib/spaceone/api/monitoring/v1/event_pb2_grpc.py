# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.monitoring.v1 import event_pb2 as spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2


class EventStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Event/create',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.CreateEventRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Event/get',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.GetEventRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Event/list',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventsInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.monitoring.v1.Event/stat',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class EventServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Creates a new Event. The Event creation process starts with validation checking whether the input data is from a webhook or not. After the input data is validated, the data is processed and used to create the Event.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Gets a specific Event matching the input parameters, `event_id` and `domain_id`. Prints detailed information about the Event.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Gets a list of all Events. You must specify the `domain_id`. You can use a query to get a filtered list of Events.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.CreateEventRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.GetEventRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.monitoring.v1.Event', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Event(object):
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Event/create',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.CreateEventRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Event/get',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.GetEventRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Event/list',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventQuery.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventsInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.Event/stat',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_event__pb2.EventStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)