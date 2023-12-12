from node import Node

class LinkedList:
    def __init__(self,value=None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
  
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node


def find_middle(linked_list):
  slow = linked_list.head_node
  fast = linked_list.head_node
  while fast is not None and fast.get_next_node() is not None:
    print("old slow "+ str(slow.value))
    slow = slow.get_next_node()
    print("new slow "+str(slow.value))
    print("old fast "+ str(fast.value))
    fast = fast.get_next_node().get_next_node()
    print("new fast "+ str(fast.value))
    print("new fast next" + str(fast.get_next_node().value))

  return slow


def generate_test_linked_list(length):
  linked_list = LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

test_list = generate_test_linked_list(9)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)