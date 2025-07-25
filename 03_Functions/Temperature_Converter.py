# Descrption: 

# This Temperature converter project is based on python concepts : Functions

def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)*5/9


if __name__ == "__main__":
    
        val = input("Enter Temperature Value in (e.g., 35C or 98F): ").strip()
        
        if val[-1].lower() == 'c':
            try:
                c = float(val[:-1])
                f = celsius_to_fahrenheit(c)
                print(f"{c}°C = {f:.2f}F")
            except ValueError:
                print("Ouch! Invalid Input Format.")
        elif val[-1].lower() == 'f':
            try:
                f = float(val[:-1])
                c = fahrenheit_to_celsius(f)
                print(f"{f}F = {c:.2f}°C")
            except ValueError:
                print("Ouch! Invalid Input Format.")
        else:
            print("Invalid Input! Mention Units of Temperature")
            