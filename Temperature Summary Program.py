"""
Program Purpose        : Determine the number of temperatures, the largest temperature and the smallest temperature.
Assignment #           : 6.1
Author                 : Kapambwe Chulu
Original Creation date : 1/19/2023

"""


# This function creates an empty list, populates it and then determines the largest and smallest temperature values.
def main():
    temperature_series = 0
    temperatures = []
    # The while loop below allows user to enter temperature values, and appends them to the empty temperature list
    while temperature_series != 'Q':
        temperature_series = input("Enter a valid value of temperature or Q to Quit: ")
        if temperature_series == 'Q':
            break
        elif temperature_series.replace('.', '').replace('-', '').isnumeric():
            temperatures.append(temperature_series)  # Populating the list based upon user input.
        else:
            print("  You entered an invalid value ")
    print("You have finished entering temperature values.")
    print(" ")
    length = len(temperatures)
    maximum_temperature = max(temperatures)
    minimum_temperature = min(temperatures)
    print("----------------------Summary of the entered temperature values -----------------")
    print(" ** The Largest temperature is " + str(maximum_temperature) + " degrees fahrenheit.")
    print(" ** The Smallest temperature is " + str(minimum_temperature) + " degrees fahrenheit.")
    print(" ** There are " + str(length) + " temperature values in the List.")
    print("-------------------------Thank you for using the program--------------------------.")


if __name__ == '__main__':
    main()
else:
    # The statements below will execute if this program is imported to another module.
    print(" Note: You are using a program which were created in another module. ")
