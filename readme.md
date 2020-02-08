Sample Input


C:\Users\ADMIN\Desktop\Association Rule Mining>python main.py
Enter the no. of transactions: 4
Enter the minimum support: 30
Support Count 2
Enter items for transaction 1
1 3 4
Enter items for transaction 2
2 3 5
Enter items for transaction 3
1 2 3 5
Enter items for transaction 4
2 5
input transaction [['1', '3', '4'], ['2', '3', '5'], ['1', '2', '3', '5'], ['2', '5']]
L1
Itemset    Support Count
1          2
3          3
2          3
5          3

L2
Itemset            Support Count
('1', '3')          2
('3', '2')          2
('3', '5')          2
('2', '5')          3

L3
Itemset
('2', '5', '3')

Frequent item set is [('2', '5', '3')]
no. of association rules =  6

Subsets are  [['2'], ['5'], ['3'], ['2', '5'], ['2', '3'], ['5', '3']]

Association Rule                Confidence(%)
[['2'], '=>', ['5', '3']]                66.66666666666666
[['5'], '=>', ['2', '3']]                66.66666666666666
[['3'], '=>', ['2', '5']]                66.66666666666666
[['2', '5'], '=>', ['3']]                66.66666666666666
[['2', '3'], '=>', ['5']]                100.0
[['5', '3'], '=>', ['2']]                100.0

\\\\STRONG ASSOCIATION RULES//////
Association Rule                Confidence(%)
[['2', '3'], '=>', ['5']]                100.0
[['5', '3'], '=>', ['2']]                100.0
