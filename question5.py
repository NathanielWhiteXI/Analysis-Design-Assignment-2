
# huffman coding, using heap tree

import heapq

with open("ascii_chars", "r") as f:
	txt_file = f.read()

freq_map = {}

for i in txt_file:
	if i in freq_map:
		freq_map[i] +=1
	else:
		freq_map[i] = 1

#print(freq_map)


#part 2

class Node:

	def __init__(self, char, freq_):
		self.char = char
		self.freq = freq_
		self.left = None
		self.right = None

	def __lt__(self, other_node):
		return self.freq < other_node.freq

	def __str__(self):
		return f"char={repr(self.char)}, freq={self.freq}, left={self.left}, right={self.right}"


n1 = Node("n", freq_map["n"])
#print(n1)

#part 3

heap_tree = []

for (key, val) in freq_map.items():
	new_node = Node(key, val)
	heapq.heappush(heap_tree, new_node)


#huffman parrt

while len(heap_tree)>1:

	left = heapq.heappop(heap_tree)
	right = heapq.heappop(heap_tree)

	merged_freq = left.freq + right.freq
	merged_node = Node(None, merged_freq)
	merged_node.left = left
	merged_node.right = right

	heapq.heappush(heap_tree, merged_node)
root = heap_tree[0]

#print(len(heap_tree))      # should be 1
#print(root.freq)           # should equal total number of characters
#print(len(txt_file))       # should match root.freq

def build_code(node, prefix, codes):

	#first checking if its a leaf node
	if (node.right== None and node.left == None):
		codes[node.char] = prefix
		return
	
	if (node.left):
		build_code(node.left, prefix +"0", codes)
	
	if (node.right):
		build_code(node.right, prefix +"1", codes)

	return codes


huff_codes = build_code(root, "", {})



for key, value in huff_codes.items():
    code = huff_codes[key]        # use key
    freq = freq_map[key]          # get frequency from freq_map
    print(f"{key}  {freq}  {code}")




# ---- Part 4: length before and after Huffman coding ----

# Original length in bits (ASCII = 8 bits per character)
original_bits = len(txt_file) * 8

# Huffman-encoded length in bits
huffman_bits = 0
for char, freq in freq_map.items():
    code_len = len(huff_codes[char])
    huffman_bits += freq * code_len

# Print summary
print("\n--- Compression Summary ---")
print(f"Original length (bits): {original_bits}")
print(f"Huffman length  (bits): {huffman_bits}")
print(f"Bits saved             : {original_bits - huffman_bits}")
print(f"Compression ratio      : {huffman_bits / original_bits:.4f}")

