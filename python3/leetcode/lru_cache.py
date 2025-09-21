from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        print(f"Getting {key} from {self.dict}")
        try:
            self.dict.move_to_end(key)
            return self.dict[key]["value"]
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.dict) >= self.cap:
            # Evict LRU
            self.prune_lru()
        self.dict[key] = {}
        self.dict[key]["value"] = value

    def prune_lru(self):
        self.dict.popitem(False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)