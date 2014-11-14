from streams import TourbillonStream
import redis

class Tourbillon(object):
	def __init__(self, redis_server="localhost"):
		self.r = redis.StrictRedis(host=redis_server)
		self.ps = p = self.r.pubsub()

	def create_tick_stream(self, stream_name):
		return TourbillonStream(self, stream_name)

