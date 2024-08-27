# Taking user input for user height
height = int(input("Please enter your height : "))
#taking user input for  user age
age = int(input("Please enter your age : "))
# Taking  user input as yes for no for photo
w_photo = input(("If you want your ride with Photo then press \"y\" if you dont wnat photo press \"N\" : ")).lower()
bill = 0

if height > 120:
    bill+=0
    if age > 18:
        bill += 12
    elif age in range(12, 18):
        bill += 7
    elif age <= 5:
        bill += 5
    if w_photo == "y":
        bill += 3
else:
    print("Sorry better luck next time ")

print(f"Please pay {bill} ,Enjoy your ride !")


