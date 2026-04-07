""" Social Media "Trending" Feeds (Sliding Window)
The Problem:
A platform needs to show the most popular hashtags from the last 24 hours only.
As time moves forward, old "likes" must be discarded immediately while new ones are added.

The Solution:
Deque (Double-Ended Queue)A Deque allows you to add/remove from both ends in O(1) time.
Logic:As a new event occurs, push it to the Rear.
Periodically check the Front of the queue. 
If the timestamp is older than 24 hours, pop it.
This "Sliding Window" maintains a real-time, memory-efficient subset of data for trend calculations."""

"Code : "

import time
from collections import deque

class TrendingFeed:
    def __init__(self, window_seconds=86400): # Default 24h
        self.events = deque() # Stores (timestamp, event_id)
        self.window = window_seconds

    def record_event(self, event_id):
        now = time.time()
        self.events.append((now, event_id))
        self.cleanup(now)

    def cleanup(self, current_time):
        # Remove elements from the front if they are too old
        while self.events and (current_time - self.events[0][0]) > self.window:
            self.events.popleft()

    def get_current_count(self):
        self.cleanup(time.time())
        return len(self.events)
