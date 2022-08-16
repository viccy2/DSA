# Create a Queue

# import Queue
import queue

test = queue.Queue()

# insert value into queue
test.put(1)
test.put(2)
test.put(3)

print(test.get())

