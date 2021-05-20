#!/usr/bin/env python3

import random as rd
'''
linear_search searches a list for a number in a linear way (i.e. start from the list at index 0 and continue till the number is found). If a number is not found, returns None by default.

input: list_to_search - the list that the method is searching through
num - the number to search for

output: steps - the number of steps took in order to find the number
'''
def linear_search(list_to_search, num):
  steps = 0

  for i in range(0, len(list_to_search)):
    if list_to_search[i] == num:
      return i, steps
    else:
      steps += 1

  return None, steps
'''
binary_search searches a list for number in a list by taking the middle point in a list and determining whether to move to the upper half or lower half by checking if the number is greater than the middle point, or less than the middle point.

input: list_to_search - the list that the method is searching through
num - the number to search for

output: steps - the number of steps took in order to find the number
'''
def binary_search(list_to_search, num):
  high = len(list_to_search) - 1
  low = 0
  mid = ((len(list_to_search) - 1) // 2)
  steps = 0

  while(low != mid or high != mid):
#    print("mid = %d" % (mid))
    if num > list_to_search[high]:
      return None, steps
    elif num < list_to_search[low]:
      return None, steps
    elif list_to_search[mid] == num:
      return mid, steps
    elif mid == high or mid == low:
      if num == list_to_search[low]:
        return low, steps
      elif num == list_to_search[high]:
        return high, steps
      else:
        return None, steps
    elif list_to_search[mid] < num:
      low = mid
      mid = (low + high) // 2
      steps += 1
    elif list_to_search[mid] > num:
      high = mid
      mid = (low + high) // 2
      steps += 1

    # if steps > 10:
    #   print("Breaking out of loop due to too many steps")
    #   break

######################################################################

'''
random_list creates a list of random elements and returns that list in a sorted manner from least to greatest.

input: list_size - the size of the created list
min_lim - the lowest number that can be added to the list
max_lim - the highest number that can be added to the list

output: new_list - a sorted list of elements
'''
def random_list(list_size=100, min_lim=0, max_lim=100):

  new_list = []

  for i in range(0, list_size):
    new_list.append(rd.randint(min_lim, max_lim))
    # print(newList.sort())

  return sorted(new_list)

######################################################################

list_siz = 10
min_li = 0
max_li = 10

# li = random_list(list_size=list_siz, min_lim=min_li, max_lim=max_li)
# li.sort()

# search_num = rd.randint(min_li, max_li)

# print(linear_search(li, search_num))

# print(binary_search(li, search_num))


# list_to_search = [x for x in range(15)]
list_to_search = [1, 3, 5, 7, 13, 16, 18, 22]
# print(list_to_search)
print(linear_search(list_to_search, 18))
print()
print(binary_search(list_to_search, 18))
# list_to_search = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14].sort()
