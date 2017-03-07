raw_data = input('Enter integer number: ')
try:
    x = int(raw_data)
except ValueError:
    print("Can't cast " + raw_data + " to integer!")