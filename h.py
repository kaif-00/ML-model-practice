# nums = [-1,0,1,2,-1,-4]

# nums.sort()
# v = []

# for i in range(len(nums)):
#     if i > 0 and nums[i] == nums[i-1]:
#         continue
#     l = i + 1
#     r = len(nums)-1
#     while l < r:
#         total = nums[i] + nums[l] + nums[r]
#         if total == 0:
#             v.append([nums[i],nums[l],nums[r]])
#             l += 1
#             r -= 1

#             while l < r and nums[l] == nums[l-1]:
#                 l+=1

#             while l< r and nums[r] == nums[r+1]:
#                 r -=1
#         elif total < 0:
#             l += 1
#         else:
#             r -= 1
# print(v)


# dividend = 10 
# divisor = 3

# quatient = dividend/divisor

# if quatient == float(quatient):
#     a = int(quatient)

#     if a > 2**31 - 1:
#         print(2**31 - 1)

#     elif a < -2**31:
#         print(-2**31)

# print(a)


# nums = [101,135,2]
# l = len(nums)
# v =[]

# for i in range(l):
#     digit_sum = 0
#     for digit in str(nums[i]):
#         digit_sum += int(digit)
#     if digit_sum == i:
#         v.append(i)
    
# if len(v) > 0:
#     print(min(v))
# else:
#     print(-1)


# nums1 = [1,2]
# nums2 = [3,4]

# a = nums1+nums2
# b = sorted(a)
# l = len(b)


# if l%2 == 1:
#     print(float(nums[l/2]))
# else:
#     s = l//2
#     x = float((b[s-1]+b[s])/2)
#     print(x)

# s1 = "(name)is(age)yearsold"
# knowledge = [["name","bob"],["age","two"]]

# k = dict(knowledge)

# result, i = [],0
# while i < len(s1):
#     if s1[i] == '(':
#         j = s1.find(')',i+1)
#         result.append(k.get(s1[i+1:j],'?')) # i am using the string here
#         i = j
#     else:
#         result.append(s1[i])
#     print(result)
#     i += 1
# print("".join(result))

s = "(ed(et(oc))el)"
stack = []
current = ''

for i in s:
    if i == '(':
        stack.append(current)
        current = ''
    elif i == ')':
        current = current[::-1]
        current = stack.pop() + current
        print(current)
    else:
        current += i # when we are at the last element 'el' it will be 'edcoteel'then with last ')' it reverse

print(current)

s = "(1+(2*3)+((8)/4))+1"
counter = 0
maxcounter = 0
for i in s:
    if i == '(':
        counter += 1
        maxcounter=max(maxcounter,counter)
    elif i ==")":
        counter -=1
    
print(maxcounter)

digits = [0,2,2]
v = set()

for i in range(len(digits)):
    if digits[i] == 0:
        continue
    for j in range(len(digits)):
        for k in range(len(digits)):
            c = str(digits[i])+str(digits[j])+str(digits[k])
            if int(c)%2 == 0 and i != j and i!=k and j!=k:
                v.add(int(c))
print(len(v))
print(v)


#this is multiple question solution 
nums = [8,2,3,4,6]
k = 2

i = k
while k in nums: #this will only activate when k in in nums if not then k will be the answer
    k += i
print(k)

nums = [13,25,83,77]
result = []

for i in range(len(nums)):
    for j in str(nums[i]):
        result.append(int(j))
print(result)


# we are using two pointer technique here to find the common elements in both arrays
#start at the beginning of both arrays and compare the elements at the current positions of
#the pointers. If they are equal, we have found a common element and print it. If the element 
#in nums1 is smaller, we move the pointer in nums1 forward. If the element in nums2 is smaller, 
#we move the pointer in nums2 forward. We continue this process until we reach the end of either array.


nums1 = [1,2,3] 
nums2 = [0,4,1,2,4]

i = 0
j = 0

while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        print(nums1[i])
        break
    elif nums1[i] < nums2[j]:
        i +=1
    else:
        j += 1
print(-1)


s = ")()())"

stack = [-1]
max_lenght = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            lenght = i - stack[-1]
            max_lenght = max(max_lenght,lenght)

print(max_lenght)

# print(brac.pop())

n = 3
b = []
def backtrack(curr, open, close):
    if open == n and close == n:
        b.append(curr)
        return
    if open<n:
        backtrack(curr+'(', open+1, close)
    if close<open:  
        backtrack(curr+')', open, close+1)

backtrack("", 0, 0)
print(b)

nums = [3,1,2,4]

left = 0
right = len(nums)-1

while left < right:
    if nums[right]%2 == 1:
        right -= 1
    elif nums[left]%2 == 0:
        left += 1
    else:
        nums[left],nums[right] = nums[right],nums[left]
        right -= 1
        left += 1
print(nums)


nums = [5,3,6,1,12]
# nums.sort()
original = 3
i = 0
while i <= len(nums)-1:
    if original == nums[i]:
        original = original*2
    i += 1
print(original)

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

a = set()
b = set()
for i in range(len(nums1)):
    if nums1[i] not in nums2:
        a.add(nums1[i])
for j in range(len(nums2)):
    if nums2[j] not in nums1:
        b.add(nums2[i])

print([list(a),list(b)])


s = "babadc"

i = 0
mid = len(s)//2
left = mid
right = mid


a = []
while left >= 0 and right < len(s) and s[left] == s[right]:
        
        a.append(left)
        a.append(right)

        left -= 1
        right += 1


print(s[min(a):max(a)+1])