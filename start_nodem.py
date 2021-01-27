#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code to test functions in linkedlistp.py
Created on Tue Jan 26 12:02:53 2021
@author: Marine Girardey
"""
from likedlist_node import Node
from linkedlistm import ChainedList

# Test node prints
def test_print_node():
    """
    test print Function
    """
    num1 = Node(1)
    num2 = Node(5)
    num1.link = num2

if __name__ == "__main__":
    # just a test to see how the __str__ method of node work's
    test_print_node()
    chained_list = ChainedList([1, 5, 6, 12, 34])

    print(chained_list.first_node)
    chained_list.delete_node(12)
    # chained_list.insert_node_after(10,11)
    print(chained_list.first_node)
