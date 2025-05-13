def divide(a,b):
    try: #want to account for if it isn't dividable by 0
        result = a/b
    except ZeroDivisionError:
        print('Error cannot divide by 0')
    else: #if everything is working out
        print(result)

divide(10,0)

#normally app wouldn't run but try except handles errors