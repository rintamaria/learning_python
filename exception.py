def divide(x,y):
    try:
        result=x // y
    except Exception as e:
        print("division by zero")
    else:
        print("answer",result)

    finally:
        print("always executed")
divide(5,10)