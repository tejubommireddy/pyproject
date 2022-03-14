# import array as arr
# a = arr.array('l',[10, 21, 12, 13])
# print('sum of the array is ', sum(a))

# to calculate average value of an array
# num_list = [10, 20, 30, 45, 50]
# res = sum(num_list)
# avg = res / len(num_list)
# print("sum is: ",res, "average is: ", avg)
# res1 = 0
# for num in num_list:
#     res1 += num
# avg1 = res1 / len(num_list)
# print("sum is: ", res1, "average is: ", avg1)

# to find the index of an array element
# list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
# print(list1.index(4))
# list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
# print(list2.index('cat'))

# to test if array contains a specific value
# test_list = [ 1, 6, 3, 5, 3, 4]
# print("checking if 4 exists in list (using loop) : ")
# for i in test_list:
#     if(i == 4):
#         print("elemet exists")
#         print("checking if 4 exists in list (using in) : ")
#         if(4 in test_list):
#             print("element exists")

# to remove a specific element from an array
# mylist=["boy", 11, 22, 33, "teju", 22, 33, 11]
# mylist.remove(22)
# print(mylist)

# to copy an array to another array
# from array import *
# vals = array('i',[44, 55, 66, 77, 33, 21])
# print("vals")
# print(vals)
# newarr = array(vals.typecode,(a*a for a in vals))
# print("newarr")
# print(newarr)

# to insert an element at a specific position in the array
# def insert_spec_position(x, n_list, pos):
#     return n_list[:pos-1]+[x]+n_list[pos-1:]
# n_list = [1, 1, 2, 3, 4, 4, 5, 1]
# print("original list:")
# print(n_list)
# kth_position = 3
# x = 12
# result = insert_spec_position(x, n_list, kth_position)
# print("\nafter inserting an element at kth position in the said list:")
# print(result)

# to find the maximum and minimum value of an array
# list1 = [3, 2, 8, 5, 10, 6]
# max_number = max(list1);
# print("the larges number is:", max_number)
# list2 = [4, 6, 78, 9, 0]
# min_number = min(list2);
# print("the smallest number is:", min_number)


# to reverse of an array of integer values
# arr = [1, 2, 3, 4, 5]
# print("array is :",arr)
# res = arr[::-1]
# print("resultant new reversed arrayay:",res)

# to find the duplicate values of an array
# some_list=['a','b','c','b','d','m','n','n']
# my_list=sorted(some_list)
# duplicates=[]
# for i in my_list:
#     if my_list.count(i)>1:
#         if i not in duplicates:
#             duplicates.append(i)
#             print(duplicates)

# to find the comman values between two arrays
# list1 = [1, 2, 3]
# list2 = [2, 3, 4]
# list1_as_set = set(list1)
# intersection = list1_as_set.intersection(list2)
# intersection_as_list = list(intersection)
# print(intersection_as_list)

# to remove the duplicates elements from an array
# sam_list = [10, 10, 20, 20, 30,]
# print("the list is:" + str(sam_list))
# result = []
# for i in sam_list:
#     if i not in result:
#         result.append(i)
#         print("the list after removing duplicates : " + str(result))

# to find the second largest number in an array
# list1 = [10, 20, 30, 40]
# list1.sort()
# print("second largest element is:",list1[1])

# to find the number of even numbers and odd numbers in an array
# array_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("orginal arrays:")
# print(array_nums)
# odd_ctr = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
# even_ctr = len(list(filter(lambda x: (x%2 == 0), array_nums)))
# print("\nNumber of even numbers in the above array: ", even_ctr)
# print("\nNumber of odd numbers in the above array: ",odd_ctr)

# to get the difference of largest and smallest value
# print("input an integer created by 8 numbers from 0 to 9.:")
# num = list(input())
# print("difference between the largest and the smallest integer from the given integer:")
# print(int("".join (sorted(num,reverse=True))) - int("".join(sorted(num))))

# to verify if the array contains two specified elements (12,23)
# test_list = [12, 23, 34, 45, 67, 78]
# print("checking if 12,23 exists in list ( using loop ) : ")
# for i in test_list:
#     if(i == 12,23):
#         print("element exists")
#         print("checking if 12,23 exists in list ( using in ) : ")
#         if(12,23 in test_list):
#             print("element exists")

# to remove the duplicate elements and return the new array
# my_list = [1, 1, 2, 2, 3, 3, 4, 4]
# my_final_list = set(my_list)
# print(list(my_final_list))
# print(" 1, 2, 3, 4, 8, 9")
#



