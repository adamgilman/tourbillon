#example implemntation

from tourbillon import Tourbillon
tb = tourbillon(redis_server)

#create test stream
stream = tb.create_tick_stream("test_stream")

#set test stream redis output channel
stream.output_channel("test-channel")

#create fake test data
oneTickperSecond = [
	(datetime(2014, 11, 14, 9, 0, 1), "tick 1"),
	(datetime(2014, 11, 14, 9, 0, 2), "tick 2"),
	(datetime(2014, 11, 14, 9, 0, 3), "tick 3"),
	(datetime(2014, 11, 14, 9, 0, 4), "tick 4"),
	(datetime(2014, 11, 14, 9, 0, 5), "tick 5"),
	(datetime(2014, 11, 14, 9, 0, 6), "tick 6"),
	(datetime(2014, 11, 14, 9, 0, 7), "tick 7"),
	(datetime(2014, 11, 14, 9, 0, 8), "tick 8"),
	(datetime(2014, 11, 14, 9, 0, 9), "tick 9"),
	(datetime(2014, 11, 14, 9, 0, 10), "tick 10"),
	(datetime(2014, 11, 14, 9, 0, 11), "tick 11"),
	(datetime(2014, 11, 14, 9, 0, 12), "tick 12"),
	(datetime(2014, 11, 14, 9, 0, 13), "tick 13"),
	(datetime(2014, 11, 14, 9, 0, 14), "tick 14"),
	(datetime(2014, 11, 14, 9, 0, 15), "tick 15"),
	(datetime(2014, 11, 14, 9, 0, 16), "tick 16"),
	(datetime(2014, 11, 14, 9, 0, 17), "tick 17"),
	(datetime(2014, 11, 14, 9, 0, 18), "tick 18"),
	(datetime(2014, 11, 14, 9, 0, 19), "tick 19"),
	(datetime(2014, 11, 14, 9, 0, 20), "tick 20"),
]

#add tick data to stream
for tick in oneTickperSecond:
	stream.add( tick )

#set delay in seconds
stream.set_delay(.5)

#stream out data on redis "test-channel" w/ msg every 1/2 second
stream.start()