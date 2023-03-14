from cmath import pi

def circumference():
    while True:
        response = input("To calculate a cirle's circumference, enter yes; otherwise, enter no. ")

        if response.lower() == 'yes':
            print("The circumference of the circle is: ")
            user_response_radius = input("Enter radius please: ")
            calculation2 = int(user_response_radius)*2*pi
            print(f'The circumference of your circle is {calculation2}.')
        else:
            break

circumference()
