import random
import time
start_time = time.time() 
 
rand_list=[]
n=4
for i in range(n):
    rand_list.append(random.randint(10,99))
print(rand_list)

input('')
print(sum(rand_list))
print('')

# Show digits 2nd time
rand_list=[]
n=4
for i in range(n):
    rand_list.append(random.randint(10,99))
print(rand_list)

input('')
print(sum(rand_list))
print('')

# Show ditigs 3rd time
rand_list=[]
n=4
for i in range(n):
    rand_list.append(random.randint(10,99))
print(rand_list)

input('')
print(sum(rand_list))
print('')

# Show digits 4th time
rand_list=[]
n=4
for i in range(n):
    rand_list.append(random.randint(10,99))
print(rand_list)

input('')
print(sum(rand_list))
print('')


# Show digits 5th time
rand_list=[]
n=4
for i in range(n):
    rand_list.append(random.randint(10,99))
print(rand_list)

input('')
print(sum(rand_list))
print('')
print("--- %s seconds ---" % round((time.time() - start_time)))
