from datetime import datetime
from threading import Timer

class TourbillonStream(object):
	def __init__(self, tb, stream_name):
		self.tb = tb
		self.r = self.tb.r
		self.stream_name = stream_name
		self.channel = None
#		self.message_queue
		self.halt_next = False
		self.seconds_delay = 1

	def add(self, tick_tuple):
		if type(tick_tuple) is not tuple:
			raise Exception("Tick data must be a tuple (datetime, data)")
		if type(tick_tuple[0]) is not datetime:
			raise Exception("Tick data must be a tuple (datetime, data)")

		self.r.rpush(self.stream_name, tick_tuple)

	def format_message(self, message):
		return "%s: %s" % (self.stream_name, message)

	def length(self):
		if self.channel is not None:
			return self.r.llen(self.stream_name)
		else:
			return None

	def output_channel(self, output_channel):
		self.channel = output_channel

	def announce(self, message):
		self.r.publish(self.channel, message)

	def set_delay(self, seconds_delay):
		self.seconds_delay = seconds_delay

	def start(self):
		if self.channel is None:
			raise Exception("Channel must be set before starting")

		self.queueNextEmit()

	def stop(self):
		self.halt_next = True
		
	def queueNextEmit(self):
		self.timer = Timer(self.seconds_delay, self.emitter)
		self.timer.start()

	def emitter(self):
		#self.announce("test emitter")
		self.announce( self.r.lpop(self.stream_name) )

		if not self.halt_next:
			self.queueNextEmit()

		