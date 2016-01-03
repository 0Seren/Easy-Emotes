# -*- coding: utf-8 -*-
from Emote import Emote
class SearchTree():
    root = Node()

    def addemote(self, emote):
        for tag in emote.tags:
            #TODO

    def searchhelper(self, tag, currnode):
        if len(tag) <= 0:
            return currnode
        elif currnode.contains(tag[0]):
            return searchhelper(tag[1:], currnode.getnext(tag[0]))
        else:
            return currnode

    def search(self, tag):
        if len(tag) > 0:
            index = root.indexof(tag[0])
            if index >= 0:
                return searchhelper(tag[1:], root.getnode(index)).endpoints
        else:
            return []



class Node():
    def __init__(self, data, subnodes, endpoint = false)
        self.data = data
        self.subnodes = subnodes
        self.endpoint = endpoint

    def indexof(self, item):
        for i in range(len(self.subnodes)):
            if self.subnodes[i].data == item:
                return i
        return -1

    def contains(self, item):
        return self.indexof(item) != -1

    def getnode(self, index):
        return self.subnodes[index]
