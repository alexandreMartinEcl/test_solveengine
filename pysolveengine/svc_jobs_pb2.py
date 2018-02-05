# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: svc_jobs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import google.api.annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import pysolveengine.converter_pb2 as converter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='svc_jobs.proto',
  package='solver.jobs',
  syntax='proto3',
  serialized_pb=_b('\n\x0esvc_jobs.proto\x12\x0bsolver.jobs\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0f\x63onverter.proto\"\xa7\x01\n\x10\x43reateJobRequest\x12;\n\x07options\x18\x01 \x03(\x0b\x32*.solver.jobs.CreateJobRequest.OptionsEntry\x12&\n\x08problems\x18\x02 \x03(\x0b\x32\x14.solver.jobs.Problem\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"%\n\x07Problem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x18\n\nJobRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1f\n\x11\x43reateJobResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x1b\n\tJobStatus\x12\x0e\n\x06status\x18\x01 \x01(\t\"V\n\x0bListRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x1a\n\x08per_page\x18\x02 \x01(\x05R\x08per_page\x12\x0c\n\x04sort\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\x05\"N\n\x07JobList\x12%\n\x04jobs\x18\x01 \x03(\x0b\x32\x17.solver.jobs.JobMessage\x12\x0f\n\x05total\x18\x02 \x01(\x05H\x00\x42\x0b\n\ttotal_obj\"\x9a\x02\n\nJobMessage\x12\x18\n\x07user_id\x18\x01 \x01(\x05R\x07user_id\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x11\n\talgorithm\x18\x04 \x01(\t\x12-\n\tsubmitted\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07started\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x66inished\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tfilenames\x18\x08 \x01(\t\x12\x1e\n\tused_time\x18\t \x01(\x05H\x00R\tused_timeB\x06\n\x04time\"7\n\rInputResponse\x12&\n\x08problems\x18\x01 \x03(\x0b\x32\x14.solver.jobs.Problem\"R\n\x0eResultResponse\x12\x16\n\x06job_id\x18\x01 \x01(\tR\x06job_id\x12(\n\x06result\x18\x02 \x01(\x0b\x32\x18.solver.converter.Result2\xf1\x05\n\x03Job\x12`\n\x06\x43reate\x12\x1d.solver.jobs.CreateJobRequest\x1a\x1e.solver.jobs.CreateJobResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/api/v2/jobs:\x01*\x12[\n\x06Status\x12\x17.solver.jobs.JobRequest\x1a\x16.solver.jobs.JobStatus\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/api/v2/jobs/{id}/status\x12O\n\x07GetJobs\x12\x18.solver.jobs.ListRequest\x1a\x14.solver.jobs.JobList\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/api/v2/jobs\x12\x62\n\x08Schedule\x12\x17.solver.jobs.JobRequest\x1a\x16.google.protobuf.Empty\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/api/v2/jobs/{id}/schedule:\x01*\x12`\n\x08GetInput\x12\x17.solver.jobs.JobRequest\x1a\x1a.solver.jobs.InputResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/api/v2/jobs/{id}/input\x12\x65\n\nGetResults\x12\x17.solver.jobs.JobRequest\x1a\x1b.solver.jobs.ResultResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/api/v2/jobs/{id}/results\x12W\n\x04Stop\x12\x17.solver.jobs.JobRequest\x1a\x16.google.protobuf.Empty\"\x1e\x82\xd3\xe4\x93\x02\x18*\x16/api/v2/jobs/{id}/stop\x12T\n\x06\x44\x65lete\x12\x17.solver.jobs.JobRequest\x1a\x16.google.protobuf.Empty\"\x19\x82\xd3\xe4\x93\x02\x13*\x11/api/v2/jobs/{id}B\x07Z\x05protob\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,converter__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CREATEJOBREQUEST_OPTIONSENTRY = _descriptor.Descriptor(
  name='OptionsEntry',
  full_name='solver.jobs.CreateJobRequest.OptionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='solver.jobs.CreateJobRequest.OptionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='solver.jobs.CreateJobRequest.OptionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=308,
)

_CREATEJOBREQUEST = _descriptor.Descriptor(
  name='CreateJobRequest',
  full_name='solver.jobs.CreateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options', full_name='solver.jobs.CreateJobRequest.options', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='problems', full_name='solver.jobs.CreateJobRequest.problems', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CREATEJOBREQUEST_OPTIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=308,
)


_PROBLEM = _descriptor.Descriptor(
  name='Problem',
  full_name='solver.jobs.Problem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='solver.jobs.Problem.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='solver.jobs.Problem.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=347,
)


_JOBREQUEST = _descriptor.Descriptor(
  name='JobRequest',
  full_name='solver.jobs.JobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='solver.jobs.JobRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=373,
)


_CREATEJOBRESPONSE = _descriptor.Descriptor(
  name='CreateJobResponse',
  full_name='solver.jobs.CreateJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='solver.jobs.CreateJobResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=406,
)


_JOBSTATUS = _descriptor.Descriptor(
  name='JobStatus',
  full_name='solver.jobs.JobStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='solver.jobs.JobStatus.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=435,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='solver.jobs.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='solver.jobs.ListRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='solver.jobs.ListRequest.per_page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='per_page'),
    _descriptor.FieldDescriptor(
      name='sort', full_name='solver.jobs.ListRequest.sort', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='solver.jobs.ListRequest.user_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=437,
  serialized_end=523,
)


_JOBLIST = _descriptor.Descriptor(
  name='JobList',
  full_name='solver.jobs.JobList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobs', full_name='solver.jobs.JobList.jobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total', full_name='solver.jobs.JobList.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='total_obj', full_name='solver.jobs.JobList.total_obj',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=525,
  serialized_end=603,
)


_JOBMESSAGE = _descriptor.Descriptor(
  name='JobMessage',
  full_name='solver.jobs.JobMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='solver.jobs.JobMessage.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='user_id'),
    _descriptor.FieldDescriptor(
      name='id', full_name='solver.jobs.JobMessage.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='solver.jobs.JobMessage.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='solver.jobs.JobMessage.algorithm', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='submitted', full_name='solver.jobs.JobMessage.submitted', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='started', full_name='solver.jobs.JobMessage.started', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finished', full_name='solver.jobs.JobMessage.finished', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filenames', full_name='solver.jobs.JobMessage.filenames', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used_time', full_name='solver.jobs.JobMessage.used_time', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='used_time'),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='time', full_name='solver.jobs.JobMessage.time',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=606,
  serialized_end=888,
)


_INPUTRESPONSE = _descriptor.Descriptor(
  name='InputResponse',
  full_name='solver.jobs.InputResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='problems', full_name='solver.jobs.InputResponse.problems', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=890,
  serialized_end=945,
)


_RESULTRESPONSE = _descriptor.Descriptor(
  name='ResultResponse',
  full_name='solver.jobs.ResultResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='solver.jobs.ResultResponse.job_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='job_id'),
    _descriptor.FieldDescriptor(
      name='result', full_name='solver.jobs.ResultResponse.result', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=947,
  serialized_end=1029,
)

_CREATEJOBREQUEST_OPTIONSENTRY.containing_type = _CREATEJOBREQUEST
_CREATEJOBREQUEST.fields_by_name['options'].message_type = _CREATEJOBREQUEST_OPTIONSENTRY
_CREATEJOBREQUEST.fields_by_name['problems'].message_type = _PROBLEM
_JOBLIST.fields_by_name['jobs'].message_type = _JOBMESSAGE
_JOBLIST.oneofs_by_name['total_obj'].fields.append(
  _JOBLIST.fields_by_name['total'])
_JOBLIST.fields_by_name['total'].containing_oneof = _JOBLIST.oneofs_by_name['total_obj']
_JOBMESSAGE.fields_by_name['submitted'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOBMESSAGE.fields_by_name['started'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOBMESSAGE.fields_by_name['finished'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOBMESSAGE.oneofs_by_name['time'].fields.append(
  _JOBMESSAGE.fields_by_name['used_time'])
_JOBMESSAGE.fields_by_name['used_time'].containing_oneof = _JOBMESSAGE.oneofs_by_name['time']
_INPUTRESPONSE.fields_by_name['problems'].message_type = _PROBLEM
_RESULTRESPONSE.fields_by_name['result'].message_type = converter__pb2._RESULT
DESCRIPTOR.message_types_by_name['CreateJobRequest'] = _CREATEJOBREQUEST
DESCRIPTOR.message_types_by_name['Problem'] = _PROBLEM
DESCRIPTOR.message_types_by_name['JobRequest'] = _JOBREQUEST
DESCRIPTOR.message_types_by_name['CreateJobResponse'] = _CREATEJOBRESPONSE
DESCRIPTOR.message_types_by_name['JobStatus'] = _JOBSTATUS
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['JobList'] = _JOBLIST
DESCRIPTOR.message_types_by_name['JobMessage'] = _JOBMESSAGE
DESCRIPTOR.message_types_by_name['InputResponse'] = _INPUTRESPONSE
DESCRIPTOR.message_types_by_name['ResultResponse'] = _RESULTRESPONSE

CreateJobRequest = _reflection.GeneratedProtocolMessageType('CreateJobRequest', (_message.Message,), dict(

  OptionsEntry = _reflection.GeneratedProtocolMessageType('OptionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CREATEJOBREQUEST_OPTIONSENTRY,
    __module__ = 'svc_jobs_pb2'
    # @@protoc_insertion_point(class_scope:solver.jobs.CreateJobRequest.OptionsEntry)
    ))
  ,
  DESCRIPTOR = _CREATEJOBREQUEST,
  __module__ = 'svc_jobs_pb2'
  # @@protoc_insertion_point(class_scope:solver.jobs.CreateJobRequest)
  ))
_sym_db.RegisterMessage(CreateJobRequest)
_sym_db.RegisterMessage(CreateJobRequest.OptionsEntry)

Problem = _reflection.GeneratedProtocolMessageType('Problem', (_message.Message,), dict(
  DESCRIPTOR = _PROBLEM,
  __module__ = 'svc_jobs_pb2'
  # @@protoc_insertion_point(class_scope:solver.jobs.Problem)
  ))
_sym_db.RegisterMessage(Problem)

JobRequest = _reflection.GeneratedProtocolMessageType('JobRequest', (_message.Message,), dict(
  DESCRIPTOR = _JOBREQUEST,
  __module__ = 'svc_jobs_pb2'
  # @@protoc_insertion_point(class_scope:solver.jobs.JobRequest)
  ))
_sym_db.RegisterMessage(JobRequest)

CreateJobResponse = _reflection.GeneratedProtocolMessageType('CreateJobResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEJOBRESPONSE,
  __module__ = 'svc_jobs_pb2'
  # @@protoc_insertion_point(class_scope:solver.jobs.CreateJobResponse)
  ))
_sym_db.RegisterMessage(CreateJobResponse)

JobStatus = _reflection.GeneratedProtocolMessageType('JobStatus', (_message.Message,), dict(
  DESCRIPTOR = _JOBSTATUS,
  __module__ = 'svc_jobs_pb2'
  # @@protoc_insertion_point(class_scope:solver.jobs.JobStatus)
  ))
_sym_db.RegisterMessage(JobStatus)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTREQUEST,
  __module__ = 'svc_jobs_pb2'
  # @@protoc_insertion_point(class_scope:solver.jobs.ListRequest)
  ))
_sym_db.RegisterMessage(ListRequest)

JobList = _reflection.GeneratedProtocolMessageType('JobList', (_message.Message,), dict(
  DESCRIPTOR = _JOBLIST,
  __module__ = 'svc_jobs_pb2'
  # @@protoc_insertion_point(class_scope:solver.jobs.JobList)
  ))
_sym_db.RegisterMessage(JobList)

JobMessage = _reflection.GeneratedProtocolMessageType('JobMessage', (_message.Message,), dict(
  DESCRIPTOR = _JOBMESSAGE,
  __module__ = 'svc_jobs_pb2'
  # @@protoc_insertion_point(class_scope:solver.jobs.JobMessage)
  ))
_sym_db.RegisterMessage(JobMessage)

InputResponse = _reflection.GeneratedProtocolMessageType('InputResponse', (_message.Message,), dict(
  DESCRIPTOR = _INPUTRESPONSE,
  __module__ = 'svc_jobs_pb2'
  # @@protoc_insertion_point(class_scope:solver.jobs.InputResponse)
  ))
_sym_db.RegisterMessage(InputResponse)

ResultResponse = _reflection.GeneratedProtocolMessageType('ResultResponse', (_message.Message,), dict(
  DESCRIPTOR = _RESULTRESPONSE,
  __module__ = 'svc_jobs_pb2'
  # @@protoc_insertion_point(class_scope:solver.jobs.ResultResponse)
  ))
_sym_db.RegisterMessage(ResultResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\005proto'))
_CREATEJOBREQUEST_OPTIONSENTRY.has_options = True
_CREATEJOBREQUEST_OPTIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class JobStub(object):
    """A service for creating new jobs with the solveEngine
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Create = channel.unary_unary(
          '/solver.jobs.Job/Create',
          request_serializer=CreateJobRequest.SerializeToString,
          response_deserializer=CreateJobResponse.FromString,
          )
      self.Status = channel.unary_unary(
          '/solver.jobs.Job/Status',
          request_serializer=JobRequest.SerializeToString,
          response_deserializer=JobStatus.FromString,
          )
      self.GetJobs = channel.unary_unary(
          '/solver.jobs.Job/GetJobs',
          request_serializer=ListRequest.SerializeToString,
          response_deserializer=JobList.FromString,
          )
      self.Schedule = channel.unary_unary(
          '/solver.jobs.Job/Schedule',
          request_serializer=JobRequest.SerializeToString,
          response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          )
      self.GetInput = channel.unary_unary(
          '/solver.jobs.Job/GetInput',
          request_serializer=JobRequest.SerializeToString,
          response_deserializer=InputResponse.FromString,
          )
      self.GetResults = channel.unary_unary(
          '/solver.jobs.Job/GetResults',
          request_serializer=JobRequest.SerializeToString,
          response_deserializer=ResultResponse.FromString,
          )
      self.Stop = channel.unary_unary(
          '/solver.jobs.Job/Stop',
          request_serializer=JobRequest.SerializeToString,
          response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          )
      self.Delete = channel.unary_unary(
          '/solver.jobs.Job/Delete',
          request_serializer=JobRequest.SerializeToString,
          response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          )


  class JobServicer(object):
    """A service for creating new jobs with the solveEngine
    """

    def Create(self, request, context):
      """Create a new job for solving, it doesn't schedule the job
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
      """View the job status
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetJobs(self, request, context):
      """List users' jobs
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Schedule(self, request, context):
      """Schedule a job for solving
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetInput(self, request, context):
      """Get job input files
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetResults(self, request, context):
      """Get job result files
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
      """Stop a running job
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
      """Delete job
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_JobServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Create': grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=CreateJobRequest.FromString,
            response_serializer=CreateJobResponse.SerializeToString,
        ),
        'Status': grpc.unary_unary_rpc_method_handler(
            servicer.Status,
            request_deserializer=JobRequest.FromString,
            response_serializer=JobStatus.SerializeToString,
        ),
        'GetJobs': grpc.unary_unary_rpc_method_handler(
            servicer.GetJobs,
            request_deserializer=ListRequest.FromString,
            response_serializer=JobList.SerializeToString,
        ),
        'Schedule': grpc.unary_unary_rpc_method_handler(
            servicer.Schedule,
            request_deserializer=JobRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'GetInput': grpc.unary_unary_rpc_method_handler(
            servicer.GetInput,
            request_deserializer=JobRequest.FromString,
            response_serializer=InputResponse.SerializeToString,
        ),
        'GetResults': grpc.unary_unary_rpc_method_handler(
            servicer.GetResults,
            request_deserializer=JobRequest.FromString,
            response_serializer=ResultResponse.SerializeToString,
        ),
        'Stop': grpc.unary_unary_rpc_method_handler(
            servicer.Stop,
            request_deserializer=JobRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'Delete': grpc.unary_unary_rpc_method_handler(
            servicer.Delete,
            request_deserializer=JobRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'solver.jobs.Job', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaJobServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """A service for creating new jobs with the solveEngine
    """
    def Create(self, request, context):
      """Create a new job for solving, it doesn't schedule the job
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Status(self, request, context):
      """View the job status
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetJobs(self, request, context):
      """List users' jobs
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Schedule(self, request, context):
      """Schedule a job for solving
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetInput(self, request, context):
      """Get job input files
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetResults(self, request, context):
      """Get job result files
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Stop(self, request, context):
      """Stop a running job
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Delete(self, request, context):
      """Delete job
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaJobStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """A service for creating new jobs with the solveEngine
    """
    def Create(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Create a new job for solving, it doesn't schedule the job
      """
      raise NotImplementedError()
    Create.future = None
    def Status(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """View the job status
      """
      raise NotImplementedError()
    Status.future = None
    def GetJobs(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """List users' jobs
      """
      raise NotImplementedError()
    GetJobs.future = None
    def Schedule(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Schedule a job for solving
      """
      raise NotImplementedError()
    Schedule.future = None
    def GetInput(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Get job input files
      """
      raise NotImplementedError()
    GetInput.future = None
    def GetResults(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Get job result files
      """
      raise NotImplementedError()
    GetResults.future = None
    def Stop(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Stop a running job
      """
      raise NotImplementedError()
    Stop.future = None
    def Delete(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Delete job
      """
      raise NotImplementedError()
    Delete.future = None


  def beta_create_Job_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('solver.jobs.Job', 'Create'): CreateJobRequest.FromString,
      ('solver.jobs.Job', 'Delete'): JobRequest.FromString,
      ('solver.jobs.Job', 'GetInput'): JobRequest.FromString,
      ('solver.jobs.Job', 'GetJobs'): ListRequest.FromString,
      ('solver.jobs.Job', 'GetResults'): JobRequest.FromString,
      ('solver.jobs.Job', 'Schedule'): JobRequest.FromString,
      ('solver.jobs.Job', 'Status'): JobRequest.FromString,
      ('solver.jobs.Job', 'Stop'): JobRequest.FromString,
    }
    response_serializers = {
      ('solver.jobs.Job', 'Create'): CreateJobResponse.SerializeToString,
      ('solver.jobs.Job', 'Delete'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('solver.jobs.Job', 'GetInput'): InputResponse.SerializeToString,
      ('solver.jobs.Job', 'GetJobs'): JobList.SerializeToString,
      ('solver.jobs.Job', 'GetResults'): ResultResponse.SerializeToString,
      ('solver.jobs.Job', 'Schedule'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('solver.jobs.Job', 'Status'): JobStatus.SerializeToString,
      ('solver.jobs.Job', 'Stop'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
    }
    method_implementations = {
      ('solver.jobs.Job', 'Create'): face_utilities.unary_unary_inline(servicer.Create),
      ('solver.jobs.Job', 'Delete'): face_utilities.unary_unary_inline(servicer.Delete),
      ('solver.jobs.Job', 'GetInput'): face_utilities.unary_unary_inline(servicer.GetInput),
      ('solver.jobs.Job', 'GetJobs'): face_utilities.unary_unary_inline(servicer.GetJobs),
      ('solver.jobs.Job', 'GetResults'): face_utilities.unary_unary_inline(servicer.GetResults),
      ('solver.jobs.Job', 'Schedule'): face_utilities.unary_unary_inline(servicer.Schedule),
      ('solver.jobs.Job', 'Status'): face_utilities.unary_unary_inline(servicer.Status),
      ('solver.jobs.Job', 'Stop'): face_utilities.unary_unary_inline(servicer.Stop),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Job_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('solver.jobs.Job', 'Create'): CreateJobRequest.SerializeToString,
      ('solver.jobs.Job', 'Delete'): JobRequest.SerializeToString,
      ('solver.jobs.Job', 'GetInput'): JobRequest.SerializeToString,
      ('solver.jobs.Job', 'GetJobs'): ListRequest.SerializeToString,
      ('solver.jobs.Job', 'GetResults'): JobRequest.SerializeToString,
      ('solver.jobs.Job', 'Schedule'): JobRequest.SerializeToString,
      ('solver.jobs.Job', 'Status'): JobRequest.SerializeToString,
      ('solver.jobs.Job', 'Stop'): JobRequest.SerializeToString,
    }
    response_deserializers = {
      ('solver.jobs.Job', 'Create'): CreateJobResponse.FromString,
      ('solver.jobs.Job', 'Delete'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('solver.jobs.Job', 'GetInput'): InputResponse.FromString,
      ('solver.jobs.Job', 'GetJobs'): JobList.FromString,
      ('solver.jobs.Job', 'GetResults'): ResultResponse.FromString,
      ('solver.jobs.Job', 'Schedule'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('solver.jobs.Job', 'Status'): JobStatus.FromString,
      ('solver.jobs.Job', 'Stop'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
    }
    cardinalities = {
      'Create': cardinality.Cardinality.UNARY_UNARY,
      'Delete': cardinality.Cardinality.UNARY_UNARY,
      'GetInput': cardinality.Cardinality.UNARY_UNARY,
      'GetJobs': cardinality.Cardinality.UNARY_UNARY,
      'GetResults': cardinality.Cardinality.UNARY_UNARY,
      'Schedule': cardinality.Cardinality.UNARY_UNARY,
      'Status': cardinality.Cardinality.UNARY_UNARY,
      'Stop': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'solver.jobs.Job', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
