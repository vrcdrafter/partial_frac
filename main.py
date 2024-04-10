
def main():
    debug = False
    if debug == True:
        top = input("top of equation")
        bottom = input("bottom of equation")
        bottom = split_terms(bottom)
        print(bottom)
    else:
        top = ["s+1"]
        bottom = "(s+4)(s+2)(s+3)"
        bottom = split_terms(bottom)
        print("bottom",bottom)
        # find inter values
        inter_values = []
        for i in range(len(bottom)):

            inter_values.append(extract_zero_value(bottom[i]))
        print("inter values",inter_values)
        solver(top,bottom,inter_values[0])

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

            sign = 1
        if values[i].isdigit():

            if sign > 0:

                return int(values[i]) * -1
            else:

                return values[i]

    if len(values) == 1:
        return 0

def solver(top,bottom,current_inter_value): # the solver takes all denom and numerator
    for i in range(len(bottom)):

        try:
            top[i] = top[i].replace("s",str(current_inter_value))
            print(top[i])
        except:
            print("index out of range ")

        bottom[i] = bottom[i].replace("s",str(current_inter_value))
        print("bottom stuff with entered inter value ",bottom[i])
main()