def level(root):
    q = [root]
    next = []
    line = []
    depth = 0
    while q:
        if depth % 2 == 0:

            head = q.pop(0)
            if head.left:
                next.append(head.left)
            if head.right:
                next.append(head.right)
            line.append(head.val)
        else:
            head = q.pop(0)
            if head.right:
                next.append(head.right)
            if head.left:
                next.append(head.left)
            line.append(head.val)

        if not q:
            print(line)
            if next:
                q = next
                next = []
                line = []
