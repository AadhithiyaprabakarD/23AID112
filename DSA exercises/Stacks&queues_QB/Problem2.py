""" 2. Distributed Task Scheduling (The "Fair Share" Problem)
The Problem:
A cloud server receives thousands of print jobs or API requests from different users. A simple queue might let one user with 1,000 requests "starve" a user with only 1 request.

The Solution: Multi-Level Feedback Queues (MLFQ) or Round-Robin Queues

Instead of one queue, the system maintains a Queue of Queues (or a Map of Queues per User ID).

Logic:

The scheduler visits User A’s queue, processes one task, then moves to User B’s queue.

This ensures no single process monopolizes the CPU (Time-Slicing).

If a task takes too long, it is "demoted" to a lower-priority queue. """\

"Code : "

"We use a dictionary to hold a separate deque for each user to ensure no one is blocked by a heavy hitter."

from collections import deque

class FairScheduler:
    def __init__(self):
        self.user_queues = {}  # Map: UserID -> deque of tasks
        self.user_order = deque() # Queue of UserIDs for Round-Robin

    def add_task(self, user_id, task):
        if user_id not in self.user_queues:
            self.user_queues[user_id] = deque()
            self.user_order.append(user_id)
        self.user_queues[user_id].append(task)

    def process_next(self):
        if not self.user_order: return None
        
        current_user = self.user_order.popleft()
        task = self.user_queues[current_user].popleft()
        
        # If user still has tasks, put them back at the end of the line
        if self.user_queues[current_user]:
            self.user_order.append(current_user)
        else:
            del self.user_queues[current_user]
            
        return f"User {current_user}: {task}"
