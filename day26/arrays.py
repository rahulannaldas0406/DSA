#var ar = [19,12,23,4,15];
# var br = [26,37,18,79,10];

#a)Write script to merge array as the values of ar in the first and values of br next
# Expected output: [19,12,23,4,15,26,37,18,79,10];
# b)Write script to merge array as the values of ar in the first and values of br next
# Expected output: [26,37,18,79,10,19,12,23,4,15];

'''ar=[19,12,23,4,15]
br=[26,37,18,79,10]

print(ar+br)
print(br+ar)'''

'''different approach '''

''''ar.extend(br)
br.extend(ar)
ar.append(br)
print(ar)
print(br)'''

#var ar = [1,2,3,7,8,9];
#var br = [4,5,6];
#Expected output: [1,2,3,4,5,6,7,8,9];

'''ar=[1,2,3,7,8,9]
br=[4,5,6]'''

'''sort_arr=sorted(ar+br)
print(sort_arr)'''

'''merg=[]
i,j=0,0
while i<len(ar) and j<len(br):
    if ar[i]<br[j]:
        merg.append(ar[i])
        i+=1
    else:
        merg.append(br[j])
        j+=1

merg.extend(ar[i:])
merg.extend(br[j:])
print(merg)'''

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

i,j=0,0
merg=[]
while i<m and j<n:
    if nums1[i]<nums2[j]:
        merg.append(nums1[i])
        i+=1
    else:
        merg.append(nums2[j])
        j+=1
merg.extend(nums1[i:m])
merg.extend(nums2[j:n])
print(merg)