from queue import PriorityQueue

# Create a PriorityQueue object
pq = PriorityQueue()

# Add elements using the .put() method
pq.put((2, [0,1]))
pq.put((1, [0,2]))
pq.put((3, [0,3]))

# Remove elements using the .get() method
while not pq.empty():
    priority, task = pq.get()
    print(f"Priority: {priority}, Task: {task}")
