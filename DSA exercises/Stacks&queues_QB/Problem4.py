"""Traffic Flow Optimization (Circular Buffer)
The Problem:
Streaming data (like live CCTV footage or a Netflix stream) arrives at unpredictable speeds. 
If the "Receiver" is slower than the "Sender," data is lost. 
If we use a standard queue, we constantly waste memory by shifting elements after every read.
  
The Solution:
Circular Queue (Ring Buffer)Logic:Use a fixed-size array where the tail wraps back to the head using modulo arithmetic: index = (i + 1) \% size.
This creates a continuous loop of memory.\
It is the gold standard for Asynchronous Data Transfer between a fast producer (the Internet) and a slower consumer (your screen's hardware)."""

"Code : "

class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, data):
        if self.count == self.size:
            raise Exception("Buffer Overflow")
        self.buffer[self.tail] = data
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return None
        data = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return data
