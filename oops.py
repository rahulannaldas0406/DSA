'''class Solution:
    def __init__(self,ram,proc):
        self.ram=ram
        self.proc=proc
    
    def config(self):
        print(self.ram)
        print(self.proc)

sol=Solution(4,"i5")

sol.config()'''


'''import heapq

def find_kth_smallest(arr, k):
    # Initialize an empty min-heap
    heap = []

    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num < heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    return heap[0]

# Example usage
arr = [100, 90, 80, 70, 60, 50, 40, 30]
k = 8
result = find_kth_smallest(arr, k)
print(result)  # Output: 20'''


arr=[1,2,3,4]
'''arr1=arr
rev_arr=arr
left=0
right=len(rev_arr)-1

while left<=right:
    rev_arr[left],rev_arr[right]=rev_arr[right],rev_arr[left]

    left+=1
    right-=1


print(arr)
print(rev_arr)
print(arr1)'''

'''rev_arr=[]

for i in range(len(arr)-1,-1,-1):
    rev_arr.append(arr[i])


print(rev_arr+arr)'''

#& "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" run qwen2.5-coder:1.5b

#Find the lowest frequency character in a string

s="hello World"

char_count={}

for char in s:
    if char not in char_count:
        char_count[char]=1
    else:
        char_count[char]+=1

min_count=min(char_count,key=char_count.get)
print(min_count)