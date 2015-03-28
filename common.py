import os
import webapp2

from google.appengine.ext.webapp import template

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), 'app/' + templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

#Following is the queued linked list for waiting room
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,newdata):
        self.data = newdata

    def set_next(self,newnext):
        self.next = newnext

class LinkedList:

    def __init__(self):
        """post: creates an empty FIFO queue"""
        self.length = 0
        self.head = None
        self.tail = None

    def add(self, x):
        """post: adds x at back of queue"""
        new_node = Node(x)
        new_node.next = None
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
    def send_player (self):
        """pre: self.size() > 0
        post: removes and returns the front item"""
        item = self.head
        self.head = self.head.next 
        self.length = self.length - 1
        if self.length == 0:
            self.last = None
        return item.get_data()
    def size(self):
        return self.length
    def front(self):
        return self.head
