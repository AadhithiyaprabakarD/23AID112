"""1. The "Undo/Redo" Logic in Professional Design Software
The Problem:
In applications like Photoshop or CAD software, users need to revert multiple actions. However, a simple history list isn't enough because performing a new action after an "Undo" must invalidate the previous "Redo" path.

The Solution: Dual-Stack Architecture

Undo Stack: Stores every state change or command.

Redo Stack: Stores commands that were popped from the Undo stack.

Logic: 1. When a user acts, push to Undo Stack and clear Redo Stack.
2. On "Undo," pop from Undo, apply the reverse, and push to Redo.
3. On "Redo," pop from Redo and push back to Undo."""

"Code : "

This implementation uses two lists as stacks to manage state history.

Python
class DocumentManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.content = ""

    def type_text(self, text):
        self.undo_stack.append(self.content)
        self.redo_stack.clear()  # New action invalidates redo path
        self.content += text

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.content)
            self.content = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.content)
            self.content = self.redo_stack.pop()
2. Fair-Share Scheduler (Queue of Queues)
We use a dictionary to hold a separate deque for each user to ensure no one is blocked by a heavy hitter.

Python
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

