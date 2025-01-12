#NameChecker
name = input("Enter your name and surname: ")
if len(name) > 12:
    print("Your name is more than 12 characters or equal 12 characters")
while not name.isalpha():
    print("You name can't contain any numbers")
    name = input("Enter your name and surname: ")

while not name.find(" ") == -1:
    print("Your profile name can't contain spaces")
    name = input("Enter your name and surname: ")

#AgeChecker
age = str(input("Enter your age: "))

while age < str(18):
    print("You are not elligible to order something without parrents access")
    age = str(input("Enter your age: "))
else:
    print("Alright , u can continue ur purchase")

food_name = input("Enter a food that u wanna to order (if u wanna to quit just answer 'q': ")
drink_name = input("Name a drink that u wanna to order (if u wanna to quit just answer 'q': ")

if drink_name and food_name == "q":
    print("Nicely to see u here later, have a nice day")

else:
    print(f"You order is {drink_name} and {food_name}")
    question = input("How would u rate our system?: ")
    print(f"Thx for ur rating , god bless u {name}")



