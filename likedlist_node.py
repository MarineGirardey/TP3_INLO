#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:02:53 2021

@author: Marine Girardey
"""

class Node:
    def __init__(self, param_data=None):
        self.data = param_data
        self.link = None

    def __str__(self):
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

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.data)
            printval = printval.link


