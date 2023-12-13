import unittest
from linked_list.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.filled_ll = LinkedList()
        self.filled_ll.append(2)
        self.filled_ll.append(4)
        self.filled_ll.append(6)
        self.filled_ll.append(8)
        
        self.single_ll = LinkedList()
        self.single_ll.append(1)
        
        self.empty_ll = LinkedList()        
    
    def test_append(self):
        self.assertEqual(self.filled_ll.head.data,2)
        self.assertEqual(self.filled_ll.head.next.data,4)
        self.assertEqual(self.filled_ll.head.next.next.data,6)
        self.assertEqual(self.filled_ll.tail.data,8)
        self.assertEqual(self.filled_ll.length,4)
        
        self.assertEqual(self.single_ll.head.data,1)
        self.assertEqual(self.single_ll.tail.data,1)
        self.assertEqual(self.single_ll.length,1)
    
    
    def test_print_list(self):
        self.assertEqual(self.filled_ll.print_list(),'2->4->6->8->')        
        self.assertEqual(self.single_ll.print_list(),'1->')
        self.assertEqual(self.empty_ll.print_list(),'')
    
    def test_pop(self):
        result = self.filled_ll.pop()
        self.assertEqual(result.data,8)
        self.assertEqual(self.filled_ll.print_list(),'2->4->6->')
        self.assertEqual(self.filled_ll.length,3)
        self.assertEqual(self.filled_ll.tail.data,6)
        
        result = self.single_ll.pop()
        self.assertEqual(result.data,1)
        self.assertEqual(self.single_ll.print_list(),'')
        self.assertEqual(self.single_ll.length,0)
        
        result = self.empty_ll.pop()
        self.assertIsNone(result)
        self.assertEqual(self.empty_ll.print_list(),'')
        self.assertEqual(self.empty_ll.length,0)
        
    def test_prepend(self):
        self.filled_ll.prepend(1)
        self.single_ll.prepend(0)
        self.empty_ll.prepend(1)    
        
        self.assertEqual(self.filled_ll.length,5)
        self.assertEqual(self.filled_ll.print_list(),'1->2->4->6->8->')
        self.assertEqual(self.filled_ll.head.data,1)
        
        self.assertEqual(self.single_ll.tail.data,1)
        
        self.assertEqual(self.empty_ll.head.data,1)
        self.assertEqual(self.empty_ll.length,1)
        
    def test_pop_first(self):
        
        result = self.filled_ll.pop_first()
        self.assertEqual(result.data,2)
        self.assertEqual(self.filled_ll.print_list(),'4->6->8->')
        self.assertEqual(self.filled_ll.length,3)
        self.assertEqual(self.filled_ll.head.data,4)
        
        result = self.single_ll.pop_first()
        self.assertEqual(result.data,1)
        self.assertEqual(self.single_ll.print_list(),'')
        self.assertEqual(self.single_ll.length,0)
        
        result = self.empty_ll.pop_first()
        self.assertIsNone(result)
        self.assertEqual(self.empty_ll.print_list(),'')
        self.assertEqual(self.empty_ll.length,0)
        
    def test_get(self):
        self.assertEqual(self.filled_ll.get(2),6)
        
        with self.assertRaises(ValueError):
            self.filled_ll.get(10)
            
        with self.assertRaises(ValueError):
            self.filled_ll.get(-1)
            
        
    def test_set_value(self):
        other_list = [1,3,5,7]
        for index,value in enumerate(other_list):
            self.filled_ll.set_value(index,value)
        
        self.assertEqual(self.filled_ll.head.data,1)
        self.assertEqual(self.filled_ll.head.next.data,3)
        self.assertEqual(self.filled_ll.head.next.next.data,5)
        self.assertEqual(self.filled_ll.tail.data,7)
        self.assertEqual(self.filled_ll.length,4)
        self.assertEqual(self.filled_ll.print_list(),'1->3->5->7->')
        
        with self.assertRaises(ValueError):
            self.filled_ll.set_value(10,1)
            
        with self.assertRaises(ValueError):
            self.filled_ll.set_value(-1,1)

    def test_insert(self):
        self.filled_ll.insert(1,3)
        self.assertEqual(self.filled_ll.print_list(),'2->3->4->6->8->')
        
        

        