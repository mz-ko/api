# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.statistics.v1 import schedule_pb2 as spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2

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
        + f' but the generated code in spaceone/api/statistics/v1/schedule_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ScheduleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add = channel.unary_unary(
                '/spaceone.api.statistics.v1.Schedule/add',
                request_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.AddScheduleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.statistics.v1.Schedule/update',
                request_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.UpdateScheduleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.FromString,
                _registered_method=True)
        self.enable = channel.unary_unary(
                '/spaceone.api.statistics.v1.Schedule/enable',
                request_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.FromString,
                _registered_method=True)
        self.disable = channel.unary_unary(
                '/spaceone.api.statistics.v1.Schedule/disable',
                request_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.statistics.v1.Schedule/delete',
                request_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.statistics.v1.Schedule/get',
                request_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.statistics.v1.Schedule/list',
                request_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.SchedulesInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.statistics.v1.Schedule/stat',
                request_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class ScheduleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def add(self, request, context):
        """Adds a new Schedule. When creating, `topic` and queries to be used should be specified. The time interval of the Schedule should be also specified to run queries repeatedly. The run set by Schedule starts every hour on the hour.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Updates a specific Schedule. You can make changes in Schedule settings, including time intervals.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def enable(self, request, context):
        """Enables a specific Schedule. If a Schedule is enabled, the query usage will be scheduled by the time interval specified.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disable(self, request, context):
        """Disables a specific Schedule. If a Schedule is disabled, the query usage will not be scheduled.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Deletes a specific Schedule. You must specify the `schedule_id` of the Schedule to delete.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Gets a specific Schedule. Prints detailed information about the Schedule, including the schedule interval and `state`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Gets a list of all Schedules. You can use a query to get a filtered list of Schedules.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScheduleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'add': grpc.unary_unary_rpc_method_handler(
                    servicer.add,
                    request_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.AddScheduleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.UpdateScheduleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.SerializeToString,
            ),
            'enable': grpc.unary_unary_rpc_method_handler(
                    servicer.enable,
                    request_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.SerializeToString,
            ),
            'disable': grpc.unary_unary_rpc_method_handler(
                    servicer.disable,
                    request_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.SchedulesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.statistics.v1.Schedule', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.statistics.v1.Schedule', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Schedule(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def add(request,
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
            '/spaceone.api.statistics.v1.Schedule/add',
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.AddScheduleRequest.SerializeToString,
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.FromString,
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
            '/spaceone.api.statistics.v1.Schedule/update',
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.UpdateScheduleRequest.SerializeToString,
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.FromString,
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
            '/spaceone.api.statistics.v1.Schedule/enable',
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.SerializeToString,
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.FromString,
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
            '/spaceone.api.statistics.v1.Schedule/disable',
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.SerializeToString,
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.FromString,
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
            '/spaceone.api.statistics.v1.Schedule/delete',
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.SerializeToString,
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
            '/spaceone.api.statistics.v1.Schedule/get',
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleRequest.SerializeToString,
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleInfo.FromString,
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
            '/spaceone.api.statistics.v1.Schedule/list',
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleQuery.SerializeToString,
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.SchedulesInfo.FromString,
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
            '/spaceone.api.statistics.v1.Schedule/stat',
            spaceone_dot_api_dot_statistics_dot_v1_dot_schedule__pb2.ScheduleStatQuery.SerializeToString,
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
