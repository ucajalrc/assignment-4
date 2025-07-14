import heapq

class Task:
    """
    Represents a single task for scheduling.
    Each Task has a task ID, a numerical priority, an arrival time, and a deadline.
    """
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # Invert comparison to use heapq as a max-heap.
        # This way, tasks with higher priority will be 'less' and come out first.
        return self.priority > other.priority

    def __repr__(self):
        return (f"Task({self.task_id}, priority={self.priority}, "
                f"arrival={self.arrival_time}, deadline={self.deadline})")

class PriorityQueue:
    """
    Implements a max-heap priority queue for scheduling tasks.
    """
    def __init__(self):
        self.heap = []

    def insert(self, task):
        """
        Inserts a new task into the queue, preserving the heap property.
        Runs in O(log n) time.
        """
        heapq.heappush(self.heap, task)

    def extract_max(self):
        """
        Removes and returns the highest-priority task.
        Runs in O(log n) time.
        If the queue is empty, returns None.
        """
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return None

    def increase_key(self, task_index, new_priority):
        """
        Increases the priority of a task at the given index.
        The heap property is then restored by re-heapifying.
        Runs in O(log n) time.
        """
        self.heap[task_index].priority = new_priority
        heapq.heapify(self.heap)

    def decrease_key(self, task_index, new_priority):
        """
        Decreases the priority of a task at the given index.
        Heap is restored by re-heapifying.
        Runs in O(log n) time.
        """
        self.heap[task_index].priority = new_priority
        heapq.heapify(self.heap)

    def is_empty(self):
        """
        Returns True if there are no tasks left in the queue.
        O(1) time operation.
        """
        return len(self.heap) == 0
    

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task('A', 10, 1, 5))
    pq.insert(Task('B', 7, 2, 4))
    pq.insert(Task('C', 15, 3, 6))
    pq.insert(Task('D', 3, 4, 8))

    print("Order in which tasks are scheduled (highest priority first):")
    while not pq.is_empty():
        print(pq.extract_max())
