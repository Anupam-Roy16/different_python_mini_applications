user_input = input("Enter a Phrase: ")
text = user_input.split()
print(text)
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)