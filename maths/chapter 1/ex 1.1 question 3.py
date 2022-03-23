from euclid import algo_hcf
n1 = 616

n2 = 32

greater = n1 if n1 > n2 else n2
smaller = n1 if n1 < n2 else n2

result = algo_hcf(greater, smaller)
print(result)

"""Given
An army contingent of"""+str(n1)+"""members is to march behind an army band of """+str(n2)+"""members in a parade.
Find out
The maximum number of columns in which they can march
Solution
The maximum number of columns in which they can march = HCF ({army_band_number, members})
So can use Euclid’s algorithm to find the HCF
Since"""+str(greater)+">"+str(smaller)+""", applying Euclid’s Division Algorithm we have
""""""616 = 32 x 19 + 8
Since remainder ≠ 0
we again apply Euclid’s Division Algorithm
Since 32 > 8
32 = 8 × 4 + 0
Since remainder = 0 we conclude, 8 is the HCF of 616 and 32.
The maximum number of columns in which they can march is 8.
Answer
The maximum number of columns in which they can march is 8."""