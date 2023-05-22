A, B = map(int, input().split())
from decimal import *

root2 = Decimal(A) / Decimal(B)
root2 = root2.to_integral_exact(rounding=ROUND_CEILING)

print(root2)