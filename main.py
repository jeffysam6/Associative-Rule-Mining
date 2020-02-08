
#blacklight
#works only upto 3 iteration


from math import ceil
from itertools import combinations 
from collections import Counter



# print(list(combinations([1,2,3,4,5,6,7,8,9,10],2)))

n = int(input("Enter the no. of transactions: "))

support = int(input("Enter the minimum support: "))

confidence = 100-support

support_count = ceil((support/100)*n)

print("Support Count",support_count)

s_1 = set()

# transaction_1 = [['A', 'B', 'D'], ['B', 'C', 'D'], ['B', 'A'], ['B', 'D'],['A','B','C','D']]
#[['1','3','4'],['2','3','5'],['1','2','3','5'],['2','5']]



#for taking the input(uncomment it)
for i in range(n):
  print(f"Enter items for transaction {i+1}")

  temp = list(input().split(" "))


  transaction_1.append(temp)



print("input transaction",transaction_1)

# for i in transaction_1:
#   for j in i:
#       s_1.add(j)

# s_1 = sorted(list(s_1))

# print("Itemset 1",s_1)

temp_c_1 = Counter()

c_1 = []

for i in transaction_1:
    for j in i:
        temp_c_1[j] += 1

for i in temp_c_1.keys():
    if(temp_c_1[i] >= support_count):
        c_1.append(i)



print("L1")
print("Itemset    Support Count")
for i in c_1:
    print(f"{i}          {temp_c_1[i]}")

print()

transaction_2 = list(combinations(c_1,2))
# print(transaction_2)

temp_c_2 = Counter()

for i in transaction_2:
    for j in transaction_1:

        if(i[0] in j and i[1] in j):
            temp_c_2[i] += 1


# print(temp_c_2)
c_2 = []

for i in temp_c_2.keys():
    if(temp_c_2[i] >= support_count):
        c_2.append(i)

# print("C2",c_2)

print("L2")
print("Itemset            Support Count")
for i in c_2:
    print(f"{i}          {temp_c_2[i]}")

print()


temp_set = []
transaction_3 = []
for i in range(len(c_2)-1):
    for j in range(i+1,len(c_2)):

        if(c_2[i][0] in c_2[j] or c_2[i][1] in c_2[j]):
            temp_set.append(c_2[i][0])
            temp_set.append(c_2[i][1])
            temp_set.append(c_2[j][0])
            temp_set.append(c_2[j][1])


            if(list(set(temp_set)) not in transaction_3):
                transaction_3.append(tuple(set(temp_set)))

            temp_set = []

# print((transaction_3))

temp_c_3 = Counter()

for i in transaction_3:
    for j in transaction_1:

        if(i[0] in j and i[1] in j and i[2] in j):
            temp_c_3[i] += 1



c_3 = []

for i in temp_c_3.keys():
    if(temp_c_3[i] >= support_count):
        c_3.append(i)


print("L3")
# print(temp_c_3)
print("Itemset")
for i in c_3:
    print(f"{i}")

print()


if(len(c_3) > 1):
    if(sorted(c_3[0]) == sorted(c_3[1])):
        print("Frequent item set is",[c_3[0]])
else:
    print("Frequent item set is",c_3)

#association rules

k = len(c_3[0])

association_rules = 2**k -2

print("no. of association rules = ",association_rules)
print()

freq_item = c_3[0]

subsets = []
#generating subsets
for i in range(1,len(freq_item)):
    for subset in combinations(freq_item, i):
        subsets.append(list(subset))
print("Subsets are ",subsets)
print()


rule_map = []

def cal_conf(a,b):

    cal_ab,cal_a = 0,0

    for i in transaction_1:

        if(set(a).issubset(i) and set(b).issubset(i)):
            cal_ab += 1

        if(set(a).issubset(i)):
            cal_a += 1

    return (cal_ab/cal_a)*100



for i in subsets:

    for j in subsets:

        if(j != i):

            if(len(i)==1 and len(j)==2 and i[0] not in j):
                rule_map.append([i,"=>",j])

            elif(len(i)==2 and len(j)==1 and j[0] not in i):
                rule_map.append([i,'=>',j])

# print("association rule")
for i in rule_map:
    i.append(cal_conf(i[0],i[2]))

print("Association Rule                Confidence(%)")

for i in rule_map:
    print(f"{i[:3]}                {i[-1]}")

print()
print("\\\\\\\\STRONG ASSOCIATION RULES//////")

print("Association Rule                Confidence(%)")

for i in rule_map:

    if(i[-1] >= confidence):
        print(f"{i[:3]}                {i[-1]}")
