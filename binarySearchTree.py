class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если не найден узел
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        node = self.Root
        bsTFind = BSTFind()

        if key == node.NodeKey:
            bsTFind.Node = node
            bsTFind.NodeHasKey = True
            bsTFind.ToLeft = False

        elif key > node.NodeKey and node.RightChild is None:
            bsTFind.Node = node
            bsTFind.NodeHasKey = False
            bsTFind.ToLeft = False

        elif key < node.NodeKey and node.LeftChild is None:
            bsTFind.Node = node
            bsTFind.NodeHasKey = False
            bsTFind.ToLeft = True

        elif key < node.NodeKey:
            node = BST(node.LeftChild)
            return node.FindNodeByKey(key)

        elif key > node.NodeKey:
            node = BST(node.RightChild)
            return node.FindNodeByKey(key)

        return bsTFind

    def AddKeyValue(self, key, val):
        node = self.FindNodeByKey(key)

        if node.NodeHasKey is False:

            if node.ToLeft == True:
                node.Node.LeftChild = BSTNode(key, val, node.Node)

            else:
                node.Node.RightChild = BSTNode(key, val, node.Node)

            return True

        else:
            return False


    def FinMinMax(self, FromNode, Findmax):
        findNode = self.FindNodeByKey(FromNode)
        node = findNode.Node

        if Findmax is True:
            if node.RightChild is None:
                return node.NodeKey

            else:
                node = BST(node.RightChild)
                return node.FinMinMax(node.Root.NodeKey, True)

        if Findmax is False:
            if node.LeftChild is None:
                return node.NodeKey

            else:
                node = BST(node.LeftChild)
                return node.FinMinMax(node.Root.NodeKey, False)

    def DeleteNodeByKey(self, key):
        deleteNode = self.FindNodeByKey(key)
        left = deleteNode.Node.LeftChild
        right = deleteNode.Node.RightChild

        if left and right:
            replaceKey = self.FinMinMax(right.NodeKey, False)
            replaceNode = self.FindNodeByKey(replaceKey)

            if replaceNode.Node.RightChild:
                replaceNode = replaceNode.Node.RightChild

            else:
                replaceNode = replaceNode.Node

        elif left and right is None:
            replaceNode = left

        elif right and left is None:
            replaceNode = right

        else:
            deleteNode.Node.Parent.LeftChild = None
            deleteNode.Node.Parent.RightChild = None
            return

        deleteNode.Node.NodeValue = replaceNode.NodeValue
        deleteNode.Node.NodeKey = replaceNode.NodeKey
        replaceNode.Parent.RightChild = None
        replaceNode.Parent.LeftChild = None


    def Count(self, count = []):
        node = self.Root
        count.append(node.NodeKey)

        if node.LeftChild:
            lnode = BST(node.LeftChild)
            lnode.Count()

        if node.RightChild:
            rnode = BST(node.RightChild)
            rnode.Count()

        return len(count)
