from Linked_list_problems_main import LinkedList
from Linked_list_problems_main import Node


########################################################################################
# helper functions:
def show_nodes(head):
    if head is None:
        print('[]')
    else:
        elements = []
        cur_node = head
        while cur_node:
            elements.append(cur_node.data)
            cur_node = cur_node.next
        print(elements)


def add_same_nodes(list1, list2, data):
    new_node = Node(data)
    list1.end.next = new_node
    list1.end = new_node
    list2.end.next = new_node
    list2.end = new_node


########################################################################################


########################################################################################
#################### I. Remove duplicates with/without extra space #####################
########################################################################################

# 1. With extra space
#######################################

# def remove_duplicates(linked_list):
#     if linked_list.head is None:
#         return '[]'
#     else:
#         new_set = { linked_list.head.data }
#         cur_node = linked_list.head
#
#         while cur_node.next:
#             if cur_node.next.data in new_set:
#                 cur_node.next = cur_node.next.next
#                 print(new_set)
#             else:
#                 new_set.add(cur_node.next.data)
#                 cur_node = cur_node.next
#
#         return linked_list.display()
#
#
# my_list = LinkedList()
# my_list.extend([7, 3, 1, 2, 1, 3, 4, 2, 5, 4])
# my_list.display()
# remove_duplicates(my_list)

# 2. Without extra space
#
# def remove_duplicates(linked_list):
#     if linked_list.head is None:
#         return '[]'
#     else:
#         cur_node = linked_list.head
#
#         while cur_node:
#             runner = cur_node
#             while runner.next:
#                 if cur_node.data == runner.next.data:
#                     runner.next = runner.next.next
#                 else:
#                     runner = runner.next
#             cur_node = cur_node.next
#
#     return linked_list.display()


# my_list = LinkedList()
# my_list.extend([7, 3, 1, 2, 1, 3, 4, 2, 5, 4])
# my_list.display()
# remove_duplicates(my_list)


########################################################################################
############################## II. Nth-to-last node ####################################
########################################################################################

# 1. Iterative solution
#######################################

# def nth_to_last(linked_list, num):
#     if linked_list.head is None:
#         print('[]')
#     else:
#         x = len(linked_list) - num
#
#         cur_node = linked_list.head
#         while x != 0:
#             cur_node = cur_node.next
#             x -= 1
#         print(cur_node.data)


# my_list = LinkedList()
# my_list.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# nth_to_last(my_list, 4)


# 2. Two pointers
#######################################

# def nth_to_last(linked_list, num):
#     if linked_list.head is None:
#         print('[]')
#     else:
#         p1 = linked_list.head
#         p2 = linked_list.head
#
#         for i in range(num):
#             if p1 is None:
#                 return None
#             p2 = p2.next
#
#         while p2:
#             p2 = p2.next
#             p1 = p1.next
#         print(p1.data)
#
#
# my_list = LinkedList()
# my_list.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# nth_to_last(my_list, 4)


########################################################################################
############################## III. Partition list #####################################
########################################################################################

# def partition(linked_list, separator):
#     left, right = Node(), Node()
#     left_end, right_end = left, right
#     cur_node = linked_list.head
#
#     while cur_node:
#         if cur_node.data < separator:
#             left_end.next = cur_node
#             left_end = left_end.next
#             print('left:', left.data, 'left_end:', left_end.data)
#         else:
#             right_end.next = cur_node
#             right_end = right_end.next
#             print('right:', right.data, 'right_end:', right_end.data)
#         cur_node = cur_node.next
#
#     left_end.next = right.next
#     right_end.next = None
#     show_nodes(left.next)


# my_list = LinkedList()
# my_list.extend([7, 3, 1, 2, 1, 3, 4, 2, 5, 4])
# partition(my_list, 3)

# https://www.youtube.com/watch?v=KT1iUciJr4g

########################################################################################
############################## IV. Add two numbers #####################################
########################################################################################

# def add_two_numbers(list_one, list_two):
#     new_list = Node()
#     cur_node = new_list
#     carry = 0
#
#     while list_one or list_two or carry:
#         print('cur_node:', cur_node.data)
#         value_one = list_one.data if list_one else 0
#         value_two = list_two.data if list_two else 0
#         print('value_one:', value_one, 'value_two:', value_two)
#
#         new_value = value_one + value_two + carry
#         print(value_one, '+', value_two, '+', carry, '=', new_value)
#         carry = new_value // 10
#         print(f'carry: {new_value} // 10 =', carry)
#         new_value = new_value % 10
#         print('new_value:', new_value, '% 10 =', new_value)
#         cur_node.next = Node(new_value)
#
#         cur_node = cur_node.next
#         list_one = list_one.next if list_one else None
#         list_two = list_two.next if list_two else None
#
#     show_nodes(new_list.next)
#
#
# my_list_one = LinkedList()
# my_list_two = LinkedList()
# my_list_one.extend([2, 7, 9])
# my_list_two.extend([8, 4, 5])
# add_two_numbers(my_list_one.head, my_list_two.head)

# https://www.youtube.com/watch?v=wgFPrzTjm7s


########################################################################################
########################## V. Intersection of Two Linked Lists #########################
########################################################################################

# def get_intersection_node(head_one, head_two):
#     list_one, list_two = head_one, head_two
#
#     while list_one != list_two:
#         list_one = list_one.next if list_one else head_two
#         list_two = list_two.next if list_two else head_one
#     print(list_one.data)
#
#
# my_list1 = LinkedList()
# my_list1.extend([1, 2, 3])
# my_list2 = LinkedList()
# my_list2.extend([5, 6, 4])
# add_same_nodes(my_list1, my_list2, 7)
# add_same_nodes(my_list1, my_list2, 8)
# add_same_nodes(my_list1, my_list2, 9)
# get_intersection_node(my_list1.head, my_list2.head)

# https://www.youtube.com/watch?v=D0X0BONOQhI

########################################################################################
################################# Practice here ########################################
########################################################################################

