class ChainedHashTable:
    """
    Implements a hash table using chaining for collision resolution.
    Each bucket is a list of (key, value) pairs.
    """
    def __init__(self, num_buckets=16):
        # Create empty buckets (chains) for the table
        self.buckets = [[] for _ in range(num_buckets)]

    def _hash(self, key):
        """
        Hashes the key and maps it to a bucket index.
        Uses a simple multiplier for basic distribution.
        """
        A = 31
        return (hash(key) * A) % len(self.buckets)

    def insert(self, key, value):
        """
        Inserts the (key, value) pair into the table.
        Updates value if the key already exists.
        """
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return
        bucket.append((key, value))  # New entry

    def search(self, key):
        """
        Searches for 'key' and returns the value if found, else None.
        """
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        Deletes the (key, value) pair with the given key if it exists.
        Returns True if deleted, False if not found.
        """
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False
