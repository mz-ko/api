# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.monitoring.v1 import escalation_policy_pb2 as spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2


class EscalationPolicyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EscalationPolicy/create',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.CreateEscalationPolicyRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.FromString,
                )
        self.update = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EscalationPolicy/update',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.UpdateEscalationPolicyRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.FromString,
                )
        self.set_default = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EscalationPolicy/set_default',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.FromString,
                )
        self.delete = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EscalationPolicy/delete',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EscalationPolicy/get',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.GetEscalationPolicyRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EscalationPolicy/list',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPoliciesInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.monitoring.v1.EscalationPolicy/stat',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class EscalationPolicyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Creates a new EscalationPolicy. When creating an EscalationPolicy, if the project_id is assigned, the EscalationPolicy is applied to the Project with the same project_id. If an EscalationPolicy is set as a global policy, all Projects in the same domain can apply the policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Updates a specific EscalationPolicy. You can make changes in EscalationPolicy settings, including the name, the escalation process, and the number of iterations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_default(self, request, context):
        """Sets a specific EscalationPolicy as default. Only policies configured as global can be set as default. When a Project is created, even if you did not configure any policy to the Project, the default policy set by this api method is applied.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Deletes a specific EscalationPolicy. Deletes the EscalationPolicy with the escalation_policy_id from the deletion request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Gets a specific EscalationPolicy. Prints detailed information about the EscalationPolicy, including the name, rules, and termination conditions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Gets a list of all EscalationPolicies. You can use a query to get a filtered list of EscalationPolicies.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EscalationPolicyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.CreateEscalationPolicyRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.UpdateEscalationPolicyRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.SerializeToString,
            ),
            'set_default': grpc.unary_unary_rpc_method_handler(
                    servicer.set_default,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.GetEscalationPolicyRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPoliciesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.monitoring.v1.EscalationPolicy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EscalationPolicy(object):
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.EscalationPolicy/create',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.CreateEscalationPolicyRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.EscalationPolicy/update',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.UpdateEscalationPolicyRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def set_default(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.EscalationPolicy/set_default',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.EscalationPolicy/delete',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.EscalationPolicy/get',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.GetEscalationPolicyRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.EscalationPolicy/list',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyQuery.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPoliciesInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.monitoring.v1.EscalationPolicy/stat',
            spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2.EscalationPolicyStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)