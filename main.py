import threading
import time
import random


BUFFER_SIZE = 5          # Capacity of the shared buffer
NUM_ITEMS = 20           # How many items each producer will produce
PRODUCER_COUNT = 2
CONSUMER_COUNT = 2


class BoundedBuffer:
    def __init__(self, capacity: int):
        self.buffer = []
        self.capacity = capacity

        # Semaphores
        self.empty = threading.Semaphore(capacity)  # Counts empty slots
        self.full = threading.Semaphore(0)          # Counts filled slots
        self.mutex = threading.Semaphore(1)         # Mutual exclusion for buffer access

    def put(self, item, producer_id: int):
        # Wait for at least one empty slot
        self.empty.acquire()

        # Enter critical section
        self.mutex.acquire()
        try:
            self.buffer.append(item)
            print(
                f"[Producer {producer_id}] Produced {item} "
                f"(buffer size: {len(self.buffer)}/{self.capacity})"
            )
        finally:
            # Leave critical section
            self.mutex.release()

        # Signal that there is one more full slot
        self.full.release()

    def get(self, consumer_id: int):
        # Wait for at least one full slot
        self.full.acquire()

        # Enter critical section
        self.mutex.acquire()
        try:
            item = self.buffer.pop(0)
            print(
                f"[Consumer {consumer_id}] Consumed {item} "
                f"(buffer size: {len(self.buffer)}/{self.capacity})"
            )
        finally:
            # Leave critical section
            self.mutex.release()

        # Signal that there is one more empty slot
        self.empty.release()
        return item


def producer(buffer: BoundedBuffer, producer_id: int, num_items: int):
    for i in range(num_items):
        # Simulate time to produce an item
        time.sleep(random.uniform(0.1, 0.5))
        item = f"P{producer_id}-Item{i}"
        buffer.put(item, producer_id)


def consumer(buffer: BoundedBuffer, consumer_id: int, total_items: int):
    """
    Each consumer will keep consuming until it has consumed 'total_items'
    items. In many textbook examples, producers/consumers run forever,
    but here we stop so the program can terminate.
    """
    for _ in range(total_items):
        # Simulate time to consume an item
        time.sleep(random.uniform(0.1, 0.5))
        _ = buffer.get(consumer_id)


def main():
    buffer = BoundedBuffer(BUFFER_SIZE)

    # Total items produced overall
    total_items = PRODUCER_COUNT * NUM_ITEMS

    # Split expected items roughly evenly for consumers
    base_items_per_consumer = total_items // CONSUMER_COUNT
    remainder = total_items % CONSUMER_COUNT

    producers = []
    consumers = []

    # Create producer threads
    for pid in range(PRODUCER_COUNT):
        t = threading.Thread(
            target=producer,
            args=(buffer, pid, NUM_ITEMS),
            name=f"Producer-{pid}",
        )
        producers.append(t)

    # Create consumer threads
    for cid in range(CONSUMER_COUNT):
        # Distribute remainder among first 'remainder' consumers
        items_to_consume = base_items_per_consumer + (1 if cid < remainder else 0)
        t = threading.Thread(
            target=consumer,
            args=(buffer, cid, items_to_consume),
            name=f"Consumer-{cid}",
        )
        consumers.append(t)

    # Start all threads
    for t in producers + consumers:
        t.start()

    # Wait for all threads to finish
    for t in producers + consumers:
        t.join()

    print("Simulation finished.")


if __name__ == "__main__":
    main()

