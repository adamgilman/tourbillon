import redis, time

r = redis.StrictRedis()
p = r.pubsub()

p.psubscribe('test-*')

while True:
	message = p.get_message()
	if message:
		print message
	time.sleep(0.001)  # be nice to the system :)