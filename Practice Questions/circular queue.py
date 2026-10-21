
# This is a simple implementation of a circular queue in Python. 
# The queue has a fixed size of 10 elements and supports basic operations such as enqueue, dequeue, checking if the queue is empty or full.

class QueueImplementation:
    def __init__(self):
        # Initialize the queue array with 10 elements set to 0
        self.queue = [0] * 10
        self.front_pointer = 0
        self.rear_pointer = 0
        self.queue_size = 10

    def enqueue(self, item):
        # Check if the queue is full using circular logic
        if (self.rear_pointer + 1) % self.queue_size == self.front_pointer:
            print("queue is full, cannot enqueue")
            return False
        else:
            # Insert item and move the rear pointer circularly
            self.queue[self.rear_pointer] = item
            self.rear_pointer = (self.rear_pointer + 1) % self.queue_size
            return True

    def dequeue(self):
        # Check if the queue is empty
        if self.rear_pointer == self.front_pointer:
            print("queue is empty, cannot dequeue")
            return None
        else:
            # Retrieve item and move the front pointer circularly
            item = self.queue[self.front_pointer]
            self.front_pointer = (self.front_pointer + 1) % self.queue_size
            return item

    def is_empty(self):
        return self.rear_pointer == self.front_pointer

    def is_full(self):
        return (self.rear_pointer + 1) % self.queue_size == self.front_pointer


# Create an instance of the queue
queue_instance = QueueImplementation()

    # Add three items to the queue
queue_instance.enqueue(1)
queue_instance.enqueue(2)
queue_instance.enqueue(3)

    # Attempt to remove four items (the 4th will fail because the queue is empty)
print("dequeued item:", queue_instance.dequeue())
print("dequeued item:", queue_instance.dequeue())
print("dequeued item:", queue_instance.dequeue())
print("dequeued item:", queue_instance.dequeue())
