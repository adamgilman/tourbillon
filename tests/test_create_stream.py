
'''
Create a tourbillon click stream which accepts tuples of
time when it occurs and the data associated with the time
'''
import pytest
from tourbillon import Tourbillon

from fixtures.simple_tick_stream import oneTickperSecond

def test_create_stream():
	tb = Tourbillon()
	stream = tb.create_tick_stream("test_stream")

def test_add_tick_must_be_tuple():
	tb = Tourbillon()
	stream = tb.create_tick_stream("test_stream")
	with pytest.raises(Exception):
		stream.add( None )

def test_add_tick_must_be_tuple_with_datetime_as_1():
	tb = Tourbillon()
	stream = tb.create_tick_stream("test_stream")
	with pytest.raises(Exception):
		stream.add( (None, None) )

def test_add_stream_data():
	tb = Tourbillon()
	stream = tb.create_tick_stream("test_stream")
	stream.add( oneTickperSecond[0] )

def test_set_output_stream():
	tb = Tourbillon()
	stream = tb.create_tick_stream("test_stream")

	stream.output_channel("test-channel")

def test_pubsub_message_formatter():
	tb = Tourbillon()
	stream = tb.create_tick_stream("test_stream")

	assert	"test_stream: message here" == stream.format_message("message here")

def test_stream_cant_be_started_without_channel():
	tb = Tourbillon()
	stream = tb.create_tick_stream("test_stream")

	with pytest.raises(Exception):
		stream.start()
