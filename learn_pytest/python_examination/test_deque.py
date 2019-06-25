# test_deque.py
from collections import deque 

dq1 = deque([1,3,4,2])

dq1.append(10)
dq1.appendleft(20)
print dq1

dq1.extend([30,40])
dq1.extendleft([50,60])
print dq1

dq1.pop()
dq1.popleft()
print dq1