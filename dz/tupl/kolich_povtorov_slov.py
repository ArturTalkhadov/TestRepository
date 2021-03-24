from collections import Counter
spisok = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
count = Counter(spisok)
for i in count:
    print(f"слово {i} повторяется {count[i]} раз(а)")
