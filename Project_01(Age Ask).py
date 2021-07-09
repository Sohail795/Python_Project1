def UserInput():
    User=int(input("Please Enter Your Age/Year of Birth: "))
    if (User>1000 and User<1901) or (User>150 and User <1000):
        print("\nYou Seems to be the Oldest ")
        print("Limits for\n1. Age = 150 Max, 5 Min\n2. Year of Birth = 2020 Max, 1901 Min\n")
        UserInput()

    elif (User>0 and User<5) or (User>2020 and User < 3000):
        print("\nYou Seems to be the Oldest ")
        print("Limits for\n1. Age = 150 Max, 5 Min \n2. Year of Birth = 2020 Max, 1901 Min\n")
        UserInput()
    else:
        Choice(User)

def Choice(User):
    print('''\nPlease Select an Option:
    1. Know When You Will Be 100
    2. Know Your Age After a Specific Years''')

    choice=int(input("Enter Choice"))
    if choice==1:
        YearCal(User)
    elif choice==2:
         SpecificYear(User)
    else:
        print("Please Enter Valid Option\n")
        Choice(User)

def YearCal(User):
    if User>=5 and User <= 150:
        print(f"Your Current Age is i.e {User}")
        print(f"You will be 100 after {100-User} Years")
    elif User<2021 and User >1900:
        print(f"Your Current Age is i.e {User}")
        print(f"You will be 100 Years  in  {100 + User} ")


def SpecificYear(User):
        if User <= 100 and User >= 5:
            Usr = 2020 - User
        elif User <= 2020 and User >= 1901:
            Usr = User

        RandYrs = int(input("Please enter any random year: "))
        if RandYrs >= Usr + 100:
            print("\nYou will be dead by that time\n")

        elif RandYrs <= Usr:
            print("\nSorry but are you born yet?")

        else:
            print(f"Your age in Year {RandYrs} will be {RandYrs - Usr}")
        again()

def again():
  x = input("Do you wish to play again?(Y/n): ")

  if x == 'Y' or x == 'y':
        UserInput()
  elif x == 'N' or x == 'n':
          print("See you later")
  else:
          print("Invalid Input!")
          again()


if __name__ == '__main__':
    UserInput()