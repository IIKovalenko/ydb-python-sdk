# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos import ydb_coordination_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2


class CoordinationServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Session = channel.stream_stream(
        '/Ydb.Coordination.V1.CoordinationService/Session',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.SessionRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.SessionResponse.FromString,
        )
    self.CreateNode = channel.unary_unary(
        '/Ydb.Coordination.V1.CoordinationService/CreateNode',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.CreateNodeRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.CreateNodeResponse.FromString,
        )
    self.AlterNode = channel.unary_unary(
        '/Ydb.Coordination.V1.CoordinationService/AlterNode',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.AlterNodeRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.AlterNodeResponse.FromString,
        )
    self.DropNode = channel.unary_unary(
        '/Ydb.Coordination.V1.CoordinationService/DropNode',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.DropNodeRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.DropNodeResponse.FromString,
        )
    self.DescribeNode = channel.unary_unary(
        '/Ydb.Coordination.V1.CoordinationService/DescribeNode',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.DescribeNodeRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.DescribeNodeResponse.FromString,
        )


class CoordinationServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Session(self, request_iterator, context):
    """Establishes a coordination session
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateNode(self, request, context):
    """Creates a new coordination node
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AlterNode(self, request, context):
    """Modifies settings of a coordination node
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DropNode(self, request, context):
    """Drops a coordination node
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DescribeNode(self, request, context):
    """Describes a coordination node
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CoordinationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Session': grpc.stream_stream_rpc_method_handler(
          servicer.Session,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.SessionRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.SessionResponse.SerializeToString,
      ),
      'CreateNode': grpc.unary_unary_rpc_method_handler(
          servicer.CreateNode,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.CreateNodeRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.CreateNodeResponse.SerializeToString,
      ),
      'AlterNode': grpc.unary_unary_rpc_method_handler(
          servicer.AlterNode,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.AlterNodeRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.AlterNodeResponse.SerializeToString,
      ),
      'DropNode': grpc.unary_unary_rpc_method_handler(
          servicer.DropNode,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.DropNodeRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.DropNodeResponse.SerializeToString,
      ),
      'DescribeNode': grpc.unary_unary_rpc_method_handler(
          servicer.DescribeNode,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.DescribeNodeRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__coordination__pb2.DescribeNodeResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Ydb.Coordination.V1.CoordinationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
