# 'countryCodes' stores the country code of the country person 'n' is residing in, at index 'n'.
# 'salaries' stores the annual salary of person 'n' at index 'n'.
# Calculate the difference between the salary of each person and the average salary of their country. 

from collections import Counter

countryCodes = list(map(int, (input('Enter space separated country code : ')).strip().split()))
salaries = list(map(int, (input('Enter space separated salaries : ')).strip().split()))

n = min(len(countryCodes), len(salaries))
avgSalary = {}
count = Counter(countryCodes)

for i in range(n):
    if (countryCodes[i]) not in avgSalary.keys():
        avgSalary[countryCodes[i]] = salaries[i]
    else:
        avgSalary[countryCodes[i]] += salaries[i]

# print(avgSalary)
# print(count)

for k, v in avgSalary.items():
    avgSalary[k] = v // count[k]

# print(avgSalary)
# print(salaries)

salaries = [salaries[i] - avgSalary[countryCodes[i]] for i in range(len(salaries))]

print(salaries)