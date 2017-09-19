tel = {'jack':700, 'sape':4139}
tel['guido'] = 8890
print(tel)
del tel['jack']
print(list(tel.keys()))
print('guido' in tel)
print(list(tel.values()))
print(78457 in tel)
tel['ere'] =0
sorted(tel.keys())
print(sorted(tel.values()))

knights = {'gallahad':'the pure', 'robin': 'the brave'}
count = 0
for k, v in knights.items():
    count+=1
    print(count,k,v)
    
    
for  i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)
    
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0}? it is {1}'.format(q,a))
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(basket):
        print(f)
        
    