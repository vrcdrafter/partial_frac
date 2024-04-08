
def main():
    debug = False
    if debug == False:
        top = input("top of equation")
        bottom = input("bottom of equation")
        bottom = split_terms(bottom)
        print(bottom)
    else:
        test = find_inter_value("s+3")
        test = find_inter_value(test)
        print(test)
        print("extracted value",extract_zero_value(test))

# auxillary stuff
def quadratic():
    pass
def split_terms(term):
    # check for form if ()() or x2+x3+x4
    arr = term.split('(')
    for i in range(len(arr)):
        arr[i] = arr[i].strip(')')
        if not arr[i]:
            print("found emtpy value ")
    arr.remove('')
    return arr
        # See PyCharm help at https://www.jetbrains.com/help/pycharm/
def find_inter_value(arg):
    # break into parts in order
    chars = [char for char in arg]
    for i in range(len(chars)):
        try:
            if (chars[i].isdigit() and chars[i+1].isdigit()):
                print("found two sequential digits", chars[i],chars[i+1] )
                temp=str(chars[i+1])+str(chars[i])
                chars[i+1] = temp
                chars.remove(chars[i])

        except:
            print("move on")
    return chars
def extract_zero_value(values):

    sign = 0 # one being positive
    for i in range(len(values)):
        if values[i] == '+':
            print("found a positive value")
            sign = 1
        if values[i].isdigit():
            print("found a number ")
            if sign > 0:
                print("make it negative")
                return int(values[i]) * -1
            else:
                print("leave it positive")
                return values[i]

main()