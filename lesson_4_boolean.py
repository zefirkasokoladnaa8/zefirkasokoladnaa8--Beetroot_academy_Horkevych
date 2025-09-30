#Task 1
#String manipulation

input_string = input("Enter a string: ")
if len(input_string) < 2:
  print('')
else:
  print(input_string[0:2] + input_string[-2:])


#Task 2
#The valid phone number program.
phone_number = input("Enter a phone number: ")
if phone_number.isdigit() and len(phone_number) == 10:
    print('Valid phone number')
else:
    print('Invalid phone number')


#Task 3
#The math quiz program.
print('Welcome to the Math Quiz!')
print('Answer the question correctly.')
question = 'What is 9 * 7? '
correct_answer = 63
while True:
    user_answer = int(input(question))
    if user_answer == correct_answer:
        print('Correct!')
        break
    else:
        print('Wrong!')
    print('Please try again.')


#Task4 
#The name check.
user_name = 'zefirka'
while True:
    input_name = input('What is your name? ').lower()
    if input_name == user_name:
        print(f'Hello, {input_name}!')
        break
    else:
        print(f'Hello, {input_name}!')
    print('Your name is not correct!')
    print('Please try again.')
  
