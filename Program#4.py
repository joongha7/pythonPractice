def do_line(line):
    words = line.split()
    return words
        

with open('salary.txt','r') as f:
    lines = f.readlines()

max_job = 0
max_salary = 0
max_future = 0
max_delta = 0

sum_salary = 0
sum_future  = 0
avg_salary = 0
avg_future = 0

num = 0
for line in lines:
    num += 1


for line in lines:
    words = do_line(line)
    job = words[0]    
    salary = words[2]    
    future = words[4]
    
    salary = salary.replace('(','')
    salary = salary.replace('만원)','')
    salary = salary.replace(',','')
    future = future.replace('(','')
    future = future.replace('%)]','')

    salary = float(salary)
    future = float(future)
    delta = salary - future * 100
    if(delta < 0) : delta = delta * (-1)

    if(delta > max_delta):
        max_job = job
        max_salary = salary
        max_future = future
        max_delta = delta

    sum_salary += salary
    sum_future += future

avg_salary = sum_salary / num
avg_future = sum_future / num

print('Average Salary :', avg_salary, 'Average Future :', avg_future)
print('Max GAP :', max_job, max_salary, max_future, max_delta)
    
