# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import upper_controller_pb2 as upper__controller__pb2

GRPC_GENERATED_VERSION = '1.70.0'
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
        + f' but the generated code in upper_controller_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class UpperControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendEndAction = channel.unary_unary(
                '/upper_controller.UpperController/sendEndAction',
                request_serializer=upper__controller__pb2.EndPayload.SerializeToString,
                response_deserializer=upper__controller__pb2.Response.FromString,
                _registered_method=True)
        self.recvEndState = channel.unary_unary(
                '/upper_controller.UpperController/recvEndState',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=upper__controller__pb2.EndPayload.FromString,
                _registered_method=True)
        self.sendArmAction = channel.unary_unary(
                '/upper_controller.UpperController/sendArmAction',
                request_serializer=upper__controller__pb2.ArmPayload.SerializeToString,
                response_deserializer=upper__controller__pb2.Response.FromString,
                _registered_method=True)
        self.recvArmState = channel.unary_unary(
                '/upper_controller.UpperController/recvArmState',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=upper__controller__pb2.ArmPayload.FromString,
                _registered_method=True)
        self.setConfig = channel.unary_unary(
                '/upper_controller.UpperController/setConfig',
                request_serializer=upper__controller__pb2.Config.SerializeToString,
                response_deserializer=upper__controller__pb2.Response.FromString,
                _registered_method=True)
        self.getConfig = channel.unary_unary(
                '/upper_controller.UpperController/getConfig',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=upper__controller__pb2.Config.FromString,
                _registered_method=True)
        self.setNeckPose = channel.unary_unary(
                '/upper_controller.UpperController/setNeckPose',
                request_serializer=upper__controller__pb2.NeckPose.SerializeToString,
                response_deserializer=upper__controller__pb2.Response.FromString,
                _registered_method=True)
        self.getNeckPose = channel.unary_unary(
                '/upper_controller.UpperController/getNeckPose',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=upper__controller__pb2.NeckPose.FromString,
                _registered_method=True)
        self.setWaistPose = channel.unary_unary(
                '/upper_controller.UpperController/setWaistPose',
                request_serializer=upper__controller__pb2.WaistPose.SerializeToString,
                response_deserializer=upper__controller__pb2.Response.FromString,
                _registered_method=True)
        self.getWaistPose = channel.unary_unary(
                '/upper_controller.UpperController/getWaistPose',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=upper__controller__pb2.WaistPose.FromString,
                _registered_method=True)


class UpperControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sendEndAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recvEndState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendArmAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recvArmState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setNeckPose(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getNeckPose(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setWaistPose(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getWaistPose(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UpperControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendEndAction': grpc.unary_unary_rpc_method_handler(
                    servicer.sendEndAction,
                    request_deserializer=upper__controller__pb2.EndPayload.FromString,
                    response_serializer=upper__controller__pb2.Response.SerializeToString,
            ),
            'recvEndState': grpc.unary_unary_rpc_method_handler(
                    servicer.recvEndState,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=upper__controller__pb2.EndPayload.SerializeToString,
            ),
            'sendArmAction': grpc.unary_unary_rpc_method_handler(
                    servicer.sendArmAction,
                    request_deserializer=upper__controller__pb2.ArmPayload.FromString,
                    response_serializer=upper__controller__pb2.Response.SerializeToString,
            ),
            'recvArmState': grpc.unary_unary_rpc_method_handler(
                    servicer.recvArmState,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=upper__controller__pb2.ArmPayload.SerializeToString,
            ),
            'setConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.setConfig,
                    request_deserializer=upper__controller__pb2.Config.FromString,
                    response_serializer=upper__controller__pb2.Response.SerializeToString,
            ),
            'getConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.getConfig,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=upper__controller__pb2.Config.SerializeToString,
            ),
            'setNeckPose': grpc.unary_unary_rpc_method_handler(
                    servicer.setNeckPose,
                    request_deserializer=upper__controller__pb2.NeckPose.FromString,
                    response_serializer=upper__controller__pb2.Response.SerializeToString,
            ),
            'getNeckPose': grpc.unary_unary_rpc_method_handler(
                    servicer.getNeckPose,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=upper__controller__pb2.NeckPose.SerializeToString,
            ),
            'setWaistPose': grpc.unary_unary_rpc_method_handler(
                    servicer.setWaistPose,
                    request_deserializer=upper__controller__pb2.WaistPose.FromString,
                    response_serializer=upper__controller__pb2.Response.SerializeToString,
            ),
            'getWaistPose': grpc.unary_unary_rpc_method_handler(
                    servicer.getWaistPose,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=upper__controller__pb2.WaistPose.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'upper_controller.UpperController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('upper_controller.UpperController', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UpperController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sendEndAction(request,
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
            '/upper_controller.UpperController/sendEndAction',
            upper__controller__pb2.EndPayload.SerializeToString,
            upper__controller__pb2.Response.FromString,
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
    def recvEndState(request,
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
            '/upper_controller.UpperController/recvEndState',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            upper__controller__pb2.EndPayload.FromString,
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
    def sendArmAction(request,
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
            '/upper_controller.UpperController/sendArmAction',
            upper__controller__pb2.ArmPayload.SerializeToString,
            upper__controller__pb2.Response.FromString,
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
    def recvArmState(request,
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
            '/upper_controller.UpperController/recvArmState',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            upper__controller__pb2.ArmPayload.FromString,
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
    def setConfig(request,
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
            '/upper_controller.UpperController/setConfig',
            upper__controller__pb2.Config.SerializeToString,
            upper__controller__pb2.Response.FromString,
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
    def getConfig(request,
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
            '/upper_controller.UpperController/getConfig',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            upper__controller__pb2.Config.FromString,
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
    def setNeckPose(request,
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
            '/upper_controller.UpperController/setNeckPose',
            upper__controller__pb2.NeckPose.SerializeToString,
            upper__controller__pb2.Response.FromString,
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
    def getNeckPose(request,
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
            '/upper_controller.UpperController/getNeckPose',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            upper__controller__pb2.NeckPose.FromString,
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
    def setWaistPose(request,
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
            '/upper_controller.UpperController/setWaistPose',
            upper__controller__pb2.WaistPose.SerializeToString,
            upper__controller__pb2.Response.FromString,
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
    def getWaistPose(request,
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
            '/upper_controller.UpperController/getWaistPose',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            upper__controller__pb2.WaistPose.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
