# # # TASK_01: Write Python Program to Calculate the Length of a String
# # # Without Using Built-In len() Function.
# # name = "AhmedAli"
# # ch = 0
# # for i in name:
# #     ch += 1
# # print(f"Total Characters in {name}: {ch}")



# # # TASK_02: Write a program that creates a list of 10 random integers.Then 
# # # create two lists by name odd_list and even_list that have all odd
# # # and even values of the list respectively.

# # odd_list = []
# # even_list = []
# # list = [2,4,3,8,1,9,5,17,11,18,10]

# # for i in list:
# #     if i % 2 == 0:
# #         even_list.append(i)
# #     else:
# #         odd_list.append(i)

# # print(f"Even List: {even_list}\nOdd List: {odd_list}")



# #TASK 3: Explore the following functions of list:
# list = [1,2,3]
# #1) list.append(x):
# list.append(4)
# print(f"apppend: {list}")
# #2) list.extend(L):
# a = [1,2,3,4]
# l = [5,6]
# a.extend(l)
# print(f"extend: {a}")
# #3) list.insert(i, x):
# x = [0,10]
# x.insert(1, 5)
# print(f"insert: {x}")
# #4) list.remove(x):
# x.remove(10)
# print(f"remove: {x}")
# #5) list.pop():
# x.pop()
# print(f"pop: {x}")
# #6) list.count(x):
# l1 = [2,3,5,2,7,7,4,7]
# print(f"count: {l1.count(7)}")
# #7) list.sort():
# l1.sort()
# print(f"sort: {l1}")
# #8) list.reverse():
# l1.reverse()
# print(f"reverse: {l1}")





# # take integer as an input from the user and prints the last digit:
# x = int(input("Enter any integer: "))
# print(x%10)





# # Reversing the string
# string = "abc"
# new_string = ""
# for i in string:
#     new_string = i + new_string
# print(new_string)






# # Given an array and a target sum, find two numbers in the array that add up to the target.
# arr = [1,7,3,4,6,6,7,8]
# target_sum = 10
# n1 = 0 
# n2=0
# for i in arr:
#     if arr[i] + arr[i+1] == 10:
#        n1 = arr[i]
#        n2 = arr[i+1]
#        break

# print(n1,n2)  





# # Generate all prime numbers less than a given number N.
# primes = []
# for i in range(2, 12):
#     is_prime = True
#     for x in range(2, i):
#         if i % x == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(i)
# print(primes)





# # Count the number of vowels in a given string.
# vowels = 'aeiou'
# string = "syed"
# count = 0
# for i in string:
#     if vowels.__contains__(i):
#         count = count + 1
# print(count)






# # Find Second Largest Number in an Array
# arr = [54, 5, 101, 100, 102]
# max = 0
# second_max = 0

# for i in arr:
#     if i > max:
#         second_max = max
#         max = i
#     elif i > second_max and i != max:
#         second_max = i

# print("Largest number:", max)
# print("Second largest number:", second_max)







# Remove duplicate elements from an array.
