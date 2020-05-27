import datetime
import time
import itertools
import random

# start_time = datetime.datetime.now()
# # time.sleep(10)
# end_time = datetime.datetime.now()
# all_time = start_time - end_time
# print(all_time)
num_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letter_str = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
chi_str = ['桂', '粤', '川', '渝']
i = 1
data = []
print(len(num_str))


while i < 10:
    c = random.randint(0, 3)
    l = random.randint(0, 9)
    str_num = []
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    n4 = random.randint(0, 9)
    n5 = random.randint(0, 9)
    data.append(chi_str[c] + letter_str[l] + num_str[n1] + num_str[n2] + num_str[n3] + num_str[n4] + num_str[n5])
    i += 1

print(str(data))
with open('test.txt', 'w') as f:
    f.write(str(data))