# coding: utf-8
'''
显然，由于数组已经排序，所以重复的元素一定连在一起，找出它们并不难，
但如果毎找到一个重复元素就立即删除它，就是在数组中间进行删除操作，
整个时间复杂度是会达到 O(N^2)。而且题目要求我们原地修改，
也就是说不能用辅助数组，空间复杂度得是 O(1)。

其实，对于数组相关的算法问题，有一个通用的技巧：要尽量避免在中间删除元素，
那我就想先办法把这个元素换到最后去。这样的话，最终待删除的元素都拖在数组尾部，
一个一个 pop 掉就行了，每次操作的时间复杂度也就降低到 O(1) 了。
快，慢指针
'''
from SingleLinkedList import LList
def get_rid_of_dupl2(linkedlist):
    slow = linkedlist.head
    fast = linkedlist.head.next
    while fast.next!=None:
        # print 'slow.elem is', slow.elem, 'fast.elem is,', fast.elem
        if fast.elem !=slow.elem:
            slow.next=fast
            slow = fast
            fast = fast.next
        else:
            fast = fast.next
    slow.next = None

    return linkedlist
def get_rid_of_dupl(yourlist):
    slow=0
    fast=0
    for i in range(1,len(yourlist)-1):
        if yourlist[i] !=yourlist[fast]:
            value=yourlist[i]
            slow+=1
            yourlist[slow]=value
            fast+=1

        else:
            fast+=1
    del yourlist[slow+1:]
    return yourlist

if __name__ == '__main__':
    # yourlist = [0,0,0,0,0,1,1,2,3,3,3,3,3,3,5,5,5,7,7,7,10,10,10]
    # print get_rid_of_dupl(yourlist)
    # if get_rid_of_dupl(yourlist) == list(set(yourlist)):
    #     print 'pass'
    # else:
    #     print 'failed'

    yourlist = [0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 3, 3, 5, 5, 5, 7, 7, 7, 10, 10, 10]
    llist = LList()
    for item in yourlist:
        llist.append(item)
    get_rid_of_dupl2(llist).printall()

