from hashtable import ChainedHashTable

# Create a hash table with 8 buckets for demonstration
ht = ChainedHashTable(num_buckets=8)

# Insert key-value pairs and update one key
print("Insert mango: Success" if ht.insert("mango", 10) is None else "Fail")
print("Insert banana: Success" if ht.insert("banana", 20) is None else "Fail")
print("Insert peach: Success" if ht.insert("peach", 30) is None else "Fail")
print("Update mango: Success" if ht.insert("mango", 40) is None else "Fail")

# Search for existing and deleted keys
print("Search mango:", ht.search("mango"))   # Should print 40
print("Delete banana:", ht.delete("banana")) # Should print True
print("Search banana:", ht.search("banana")) # Should print None
