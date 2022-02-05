def has_cycle(head):
    while head != None:
        if head.data != False:
            head.data = False
        else:
            return 1
        head = head.next

    return 0
