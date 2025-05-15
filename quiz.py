import json

name = input("enter ur name ")
print(f'Welcome {name.capitalize()}')
playgame = input('do you want to play a quiz ')

if playgame.lower() != 'yes':
  print('Bye Bye !')
  quit()

score = 0

with open('quizdatabase.json','r') as file:
  data  =  json.load(file)


for q in data:

  question = q['question']
  options = q['options']
  answer = q['answer']

  print(f'Question {question}')
  for i , op in enumerate(options,1):
    print(f'{i} {op}')

  ans = int(input("Answer "))

  if options[ans-1].lower() == answer.lower():
    print("correct")
    score = score + 1
  else:
    print(f'incorrect ! , correct answer is {answer}')

print(f'Quiz Over ur Score is {score}')
 





