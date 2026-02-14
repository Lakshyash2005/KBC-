

questions = [
["Q!. which language was used to create fb ?", " pyhton " , " french  ", " php  " ," none " , 4 ],
["Q2.2. Which of the following is used to take input from the user in Python?"  , "(A) scan()","(B) input()","(C) read()","(D) get()",2],
["Q3.What will be the output of this code?", "(A) <class 'float'>","(B) <class 'str'>","(C) <class 'int'>","(D) <class 'bool'>",2],
["Q4. Which data type is immutable in Python?","(A) List","(B) Set","(C) Dictionary","(D) Tuple",4],
["Q5.What is the output of this code?","(A) 2.5","(B) 2","(C) 3","(D) 2.0",4],
["Q6. is coding good for us", "(A) yes", "(B) no", "(C) maybe", "(D) not sure", 1]
      ]

levels= [1000, 20000, 30000, 500000, 1000000,320000]
money =0 
i =0
for i in range (0, len(questions)):
    question = questions[i]
    print(f"\nQuestion {i+1} for Rs. {levels[i]}")
    print(question[0])
    print(f"a.{question[1]}      b.{question[2]}")
    print(f"c.{question[3]}      d.{question[4]}")
    reply = int(input("enter your answer(1-4): or press 0  for quit "))
    if(reply ==0):
        money = levels[i-1]
        break
    if(reply == question[5]):
        print(f"correct answer, you have won Rs.{levels[i]}")
        if(i==4):
          money=1000
        elif(i==5):
            money = 32000
        money = levels[i]
        if(i == len(questions)-1):
            print("🏆 Congratulations! You won the game!")
    else:
        print("wrong answer")
        continue
print (f"you take off money home is {money}")


