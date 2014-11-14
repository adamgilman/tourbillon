'''
Make a tourbillon tick stream fire out tick data
at a set pacing, within reason
'''
import pytest
from tourbillon import Tourbillon

from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

from fixtures.simple_tick_stream import oneTickperSecond
import redis, time

from nose.tools import nottest as slowskip

r = redis.StrictRedis()
p = r.pubsub()

@slowskip
def _send_test_message_time_frequency(delay_seconds, max_counter):
	time.sleep(2.5) #wait for any previous messages to clear
	tb = Tourbillon()
	stream = tb.create_tick_stream("test_stream")
	stream.output_channel("test-channel")
	stream.set_delay(delay_seconds)
	for tick in oneTickperSecond:
		stream.add( tick )

	p.psubscribe('test-*')

	stream.start()
	#get max messages
	counter = 0
	messages = []
	while counter < max_counter:
		message = p.get_message()
		if message:
			#make sure it's the right type of message
			if message['channel'] == "test-channel":
				#messages[counter] = datetime.now()
				message['arrived'] = datetime.now()
				messages.append(message)
				counter = counter + 1
		time.sleep(0.001)

	stream.stop()
	return messages

'''def test_reset_channel():
	tb = Tourbillon()
	stream = tb.create_tick_stream("test_stream")
	stream.output_channel("test-channel")
	for tick in oneTickperSecond:
		print tick
		stream.add( tick )

	assert stream.length() == 20

	stream.reset()

	assert stream.length() == 0'''
	

def test_real_time_stream_1ps():
	max_counter = 5
	messages = _send_test_message_time_frequency(1, max_counter)
	#ensure all messages have a 1 second delta
	for i in range(0, max_counter-1):
		assert (messages[i+1]['arrived'] - messages[i]['arrived']).seconds == 1


def test_real_time_stream_2seconds_pm():
	max_counter = 5
	messages = _send_test_message_time_frequency(2, max_counter)
	#ensure all messages have a 2 second delta
	for i in range(0, max_counter-1):
		assert (messages[i+1]['arrived'] - messages[i]['arrived']).seconds == 2

def test_real_time_stream_Halfsecond_pm():
	max_counter = 5
	messages = _send_test_message_time_frequency(.5, max_counter)
	#ensure all messages have a 2 second delta
	for i in range(0, max_counter-1):
		print messages
		assert int((messages[i+1]['arrived'] - messages[i]['arrived']).microseconds/100000) == 5


def test_message_conatins_correct_data():
	max_counter = 5
	messages = _send_test_message_time_frequency(.5, max_counter)
	return_messages = ["tick 1", "tick 2", "tick 3", "tick 4", "tick 5"]
#	for message in messages:



