# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos import ydb_persqueue_v1_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2


class PersQueueServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateWriteSession = channel.stream_stream(
        '/Ydb.PersQueue.V1.PersQueueService/CreateWriteSession',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.WriteSessionRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.WriteSessionResponse.FromString,
        )
    self.CreateReadSession = channel.stream_stream(
        '/Ydb.PersQueue.V1.PersQueueService/CreateReadSession',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.ReadSessionRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.ReadSessionResponse.FromString,
        )
    self.GetReadSessionsInfo = channel.unary_unary(
        '/Ydb.PersQueue.V1.PersQueueService/GetReadSessionsInfo',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.ReadInfoRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.ReadInfoResponse.FromString,
        )


class PersQueueServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateWriteSession(self, request_iterator, context):
    """*
    Creates Write Session
    Pipeline:
    client                  server
    Init(Topic, SourceId, ...)
    ---------------->
    Init(Partition, MaxSeqNo, ...)
    <----------------
    write(data1, seqNo1)
    ---------------->
    write(data2, seqNo2)
    ---------------->
    ack(seqNo1, offset1, ...)
    <----------------
    write(data3, seqNo3)
    ---------------->
    ack(seqNo2, offset2, ...)
    <----------------
    issue(description, ...)
    <----------------

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateReadSession(self, request_iterator, context):
    """*
    Creates Read Session
    Pipeline:
    client                  server
    Init(Topics, ClientId, ...)
    ---------------->
    Init(SessionId)
    <----------------
    read1
    ---------------->
    read2
    ---------------->
    assign(Topic1, Cluster, Partition1, ...) - assigns and releases are optional
    <----------------
    assign(Topic2, Clutster, Partition2, ...)
    <----------------
    start_read(Topic1, Partition1, ...) - client must respond to assign request with this message. Only after this client will start recieving messages from this partition
    ---------------->
    release(Topic1, Partition1, ...)
    <----------------
    released(Topic1, Partition1, ...) - only after released server will give this parittion to other session.
    ---------------->
    start_read(Topic2, Partition2, ...) - client must respond to assign request with this message. Only after this client will start recieving messages from this partition
    ---------------->
    read data(data, ...)
    <----------------
    commit(cookie1)
    ---------------->
    committed(cookie1)
    <----------------
    issue(description, ...)
    <----------------

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetReadSessionsInfo(self, request, context):
    """Get information about reading
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PersQueueServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateWriteSession': grpc.stream_stream_rpc_method_handler(
          servicer.CreateWriteSession,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.WriteSessionRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.WriteSessionResponse.SerializeToString,
      ),
      'CreateReadSession': grpc.stream_stream_rpc_method_handler(
          servicer.CreateReadSession,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.ReadSessionRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.ReadSessionResponse.SerializeToString,
      ),
      'GetReadSessionsInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetReadSessionsInfo,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.ReadInfoRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__persqueue__v1__pb2.ReadInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Ydb.PersQueue.V1.PersQueueService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
