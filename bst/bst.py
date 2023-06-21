# %%

from tree import preorder_construct, TreeNode, preorder_traverse
x = [6, 4, 3, None, None, 5, None, None, 8, 7, None, None, 9, None, None]

# %%
root = preorder_construct(x)


def search(root, target):
    if not root:
        return None

    if root.val == target:
        return root

    if root.val > target:
        return search(root.left, target)
    else:
        return search(root.right, target)


node = search(root, 3)
print(node.val)
# %%


def add(root, target):
    node = TreeNode(target)

    if root.val > target:
        if not root.left:
            root.left = node
        else:
            add(root.left, target)

    if root.val < target:
        if not root.right:
            root.right = node
        else:
            add(root.right, target)


add(root, 11)
add(root, 1)
print(preorder_traverse(root))

# %%


def delete(root, target):
    """
    suppose node.val == target:

    if node has no child: delete

    if node has only right child: replace node with right child

    if node has left node: find left right most node and link the node's
    right child to it.
    """

    pass


# %%
root = preorder_construct(x)
print(preorder_traverse(root))


def flip(root):
    if not root:
        return root

    root.left = flip(root.left)
    root.right = flip(root.right)

    root.left, root.right = root.right, root.left

    return root


root = flip(root)
print(preorder_traverse(root))
