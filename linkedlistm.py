#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:02:53 2021

@author: Marine Girardey
"""
from node import Node

class ChainedList:
    """
    Chained list Object
    Parameters
    ----------
    nodes : list
        list that we want to transfert in a chained list of Node object
    """

    def __init__(self, nodes):
        self.first_node = Node(nodes[0])
        n = self.first_node
        i = 1
        while i < len(nodes):
            n.link = Node(nodes[i])
            n = n.link
            i += 1

    def insert_node_after(self, data, new_node):
        """
        insert a new node after the node with the value == data
        Parameters
        ----------
        data : searched data
        new_node : node to insert
        """
        my_node = self.first_node
        while my_node is not None:
            
            if my_node.data == data:
                
                break
            my_node = my_node.link
        
        # Create a new node
        node = Node(new_node)
        # Make next of new Node as next of prev_node  
        node.link = my_node.link
        # Make next of prev_node as new_node  
        my_node.link = node

    def delete_node(self, data):
        """
        delete all node(s) value == data
        Parameters
        ----------
        data : searched data to delete
        """
        my_node = self.first_node
        while my_node.link is not None:
            if my_node.link.data == data:
                print(my_node.link.data)
                my_node.link = my_node.link.link
            my_node = my_node.link
    
