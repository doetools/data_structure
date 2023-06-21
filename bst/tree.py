# %%

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


x = [1, 2, 4, None, None, 5, None, None, 3, 6, None, None, 7, None, None]


def preorder_construct(x):
    if not x:
        return None

    n = x.pop(0)

    if not n:
        return None

    node = TreeNode(n)

    node.left = preorder_construct(x)
    node.right = preorder_construct(x)

    return node


root = preorder_construct(x)


def preorder_traverse(root):
    if not root:
        return [None]

    ret = [root.val]
    ret += preorder_traverse(root.left)
    ret += preorder_traverse(root.right)

    return ret


x_1 = preorder_traverse(root)
print(x_1)

# %%
