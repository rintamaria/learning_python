mark=int(input("enter your mark"))
if mark>89:
    print("A grade")
elif mark>79 and mark<90:
    print("B grade")
elif mark>69 and mark<80:
    print("C grade")
elif mark<70:  # can use else instead of elif here    print("F")

