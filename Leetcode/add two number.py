# define ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# define examples
l1_2 = ListNode(3)
l1_1 = ListNode(4, l1_2)
l1 = ListNode(2, l1_1)

l2_2 = ListNode(4)
l2_1 = ListNode(6, l2_2)
l2 = ListNode(5, l2_1)

# define l1 and l2  and answer string
l1_temp = ""
l2_temp = ""
answer_temp = ""

# define answer ListNode
answer = ListNode()

# set l1 and l2 list to l2 and l1 string
while True:
    l1_temp += str(l1.val)
    if l1.next is None:
        break
    l1 = l1.next
while True:
    l2_temp += str(l2.val)
    if l2.next is None:
        break
    l2 = l2.next

# reverse strings
l1_temp = l1_temp[::-1]
l2_temp = l2_temp[::-1]

# sum the number
answer_temp = str(int(l1_temp) + int(l2_temp))

# convert answer string to ListNode
answer.val = int(answer_temp[0])
for i in range(len(answer_temp) - 1):
    temp = answer
    answer = ListNode(int(answer_temp[i + 1]), temp)
