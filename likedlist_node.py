#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creation of node class for a linked list
Created on Tue Jan 26 12:02:53 2021
@author: Marine Girardey
"""

# Node class
class Node:
    """Node class for a linked list
    Attributes
    ----------
    param_data : int
    link : node.Node
    """
    def __init__(self, param_data=None):
        """Class constructor
        Parameters
        ----------
        param_data : int
            the data
        Returns
        -------
        None
            Node object
        """
        self.data = param_data
        self.link = None

    def __str__(self):
        """data property getter
        Returns
        -------
        int
            value of the data
        """
        liste = []
        node = self
        while node.link != None:
            liste.append(node.data)
            node = node.link
        liste.append(node.data)
        return str(liste)

# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def __listprint__(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval = printval.link
