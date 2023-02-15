import random


class LinkedListNode:
    def __init__(self, data):
        self.data = data 
        self.next = None

    def deleteLink(self):
        self.next = self.next.next

    def insert(self, node):
        old_next = self.next
        self.next = node
        node.next = old_next

    def add(self, add_node):
        node = self
        while node.next:
            node = node.next
        node.next = add_node

    def sort(self, is_sorted=True):
        if not self.next:
            return is_sorted 
        
        if self.next.data < self.data:
            is_sorted = False 
            swap = self.next.data
            self.next.data = self.data
            self.data = swap

        return self.next.sort(is_sorted)
        


    def search(self, val):
        node = self
        while node:
            if node.data == val:
                return True
            node = node.next 
        return False

    def print(self):
        node = self 
        while node:
            print(node.data)
            node = node.next

class DoublyLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.previous = None


class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def add(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data)
                return
            else:
                self.left.add(data)

        if data > self.data:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.add(data)

    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h 
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)
    
    def getNodesAtDepth(self, depth, nodes):
        if depth == 0:
            nodes.append(self)
            return nodes
        
        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        
        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes
    
    def search(self, target):
        if self.data == target:
            print('FOUND IT!')
            return self
        
        if self.left and self.data > target:
            return self.left.search(target)
        
        if self.right and self.data < target:
            return self.right.search(target)
        
        print('Does not exist!')

class Tree:
    def __init__(self, root, name='cool tree'):
        self.root = root
        self.name = name

    def add(self, data):
        return self.root.add(data)
    
    def search(self, target):
        return self.root.search(target)
    
    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_'+(' '*spacing)
        spacing = spacing-len(str(n))+1
        return str(n)+(' '*spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1)  + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.getNodesAtDepth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.links = []

    def search(self, target, visited=[]):
        if self.data == target:
            print('Found it!')
            return self.data 
        
        visited.append(self.data)

        for node in self.links:
            if node.data in visited:
                # don't continue search
                continue 
            found = node.search(target, visited)
            if found:
                print('Found it!')
                return found


one = GraphNode(1)
two = GraphNode(2)
three = GraphNode(3)
four = GraphNode(4)
five = GraphNode(5)
six = GraphNode(6)

g = one 
one.links = [two, three]
three.links = [four, five]
two.links = [four, one, two]

g.search(4)


root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(10)
root.right.right = TreeNode(20)
root.right.left = TreeNode(15)
root.left.left = TreeNode(4)
tree = Tree(root)
tree.print()

tree.search(21)

tree.add(21)
tree.print()

tree.search(21)


'''
ll = LinkedListNode(1)
next = ll
for i in range(10):
    next.next = LinkedListNode(random.randint(0, 10))
    next = next.next

ll.print()

while not ll.sort():
    pass
print('SORTED!')
ll.print()
'''
'''
one = LinkedListNode(1)
two = LinkedListNode(2)
three = LinkedListNode(3)
four = LinkedListNode(4)
one.next = two
two.next = three

one.insert(LinkedListNode(1.5))
one.add(four)

one.deleteLink()

one.print()

print(one.search(6))
'''




