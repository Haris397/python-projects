print("Welcome, How well do u know your math problem?Pick a number and we will give you 10 math problem  to solve")
print()
number= int(input("Enter YOur Number:"))
print()
counter=0  # it acutally counts your score
for i in range(1,11):
  correct_answer=i*number
  print(i,"x",number)
  answer=int(input(">")) # check for the answer
  if answer == correct_answer:
    print("you got the right answer!")
    counter=counter+1
  else:
    print("that's not correct, it should have been",correct_answer ) # concatenation

if counter == 10:
  print("Wow! A perfect SCore 😎") 
else:
  print("You got ", counter, "out of 10 correct")
