def celcius_to_fahrenheit(celcius):
    return(celcius*9/5) +32

def fahrenheit_to_celcius(fahrenheit):
    return(fahrenheit - 32)

print("             Temperature converter ")
print(" ----------------------")

while True:
    print("enter 'C' for celcius or 'F' for fahrenheit")

    temp = float(input("enter the temperature value :"))
    unit =input("enter the unit of measurement (C/F) :").strip().upper()

    if unit == 'C':
        converted_temp = celcius_to_fahrenheit(temp)
        print(f"{temp}C is equal to {converted_temp}F")
    elif unit == 'F':
        converted_temp = fahrenheit_to_celcius(temp)
        print(f"{temp}F is equal to {converted_temp}C")
    else:
        print("Invalid unit of measurement.Please enter 'C' for celcius or 'F' for fahrenheit")

    continue_choice = input("want to perform another temperature conversion ? (yes to continue ,no to exit):").strip().lower()
    if continue_choice != "yes":
        print("exiting .........Goodbye!")
        break