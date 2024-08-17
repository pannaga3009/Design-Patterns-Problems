import time
from collections import defaultdict, deque

"""
"How can you implement a system to track and display the top 10 purchased items 
over the last hour, assuming you cannot use a database and must rely on in-memory storage?"
The solution involves:
Storing purchased items and their timestamps in memory.
Cleaning up items older than one hour to manage memory usage.
Calculating the top 10 items based on purchase counts from the last hour.


"""
class TopItemsCalculator:
    def __init__(self, time_window=3600):
        self.time_window = time_window
        self.items = defaultdict(int)
        self.timestamps = deque()
        self.current_time = time.time()

    def add_purchase(self, item):
        now = time.time()
        self.items[item] += 1
        self.timestamps.append((item, now))
        self.cleanup_old_items(now)

    def cleanup_old_items(self, now):
        # Remove items older than the time window
        while self.timestamps and (now - self.timestamps[0][1]) > self.time_window:
            old_item, old_time = self.timestamps.popleft()
            if old_time < now - self.time_window:
                self.items[old_item] -= 1
                if self.items[old_item] <= 0:
                    del self.items[old_item]

    def get_top_items(self, top_n=10):
        # Sort items by count and return the top N
        sorted_items = sorted(self.items.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:top_n]

# Example usage
if __name__ == "__main__":
    calculator = TopItemsCalculator()

    # Simulate some purchases
    calculator.add_purchase("item1")
    calculator.add_purchase("item2")
    time.sleep(1)  # Sleep to simulate time passing
    calculator.add_purchase("item1")

    # Generate widget
    top_items = calculator.get_top_items()
    print("Top Items:", top_items)
    
    # Simulate time passing
    time.sleep(2)
    
    # Add more purchases
    calculator.add_purchase("item3")
    
    # Generate widget
    top_items = calculator.get_top_items()
    print("Top Items:", top_items)
