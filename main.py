
def main():
    debug = False
    if debug == True:
        top = input("top of equation")
        bottom = input("bottom of equation")
        bottom = split_terms(bottom)
        print(bottom)
    else:
        top = ["s+1"]
        bottom = "(s)(s+2)^2"

        # do a check to see if complex roots
        if "^" in bottom:
            print("has one distinct root")
            # find inter values
            bottom = split_terms(bottom)
            print(bottom)
        else:

            bottom = split_terms(bottom)

            # find inter values
            inter_values = []
            for i in range(len(bottom)):

                inter_values.append(extract_zero_value(bottom[i]))

            print(solver(top, bottom, inter_values[0])) # works but you cant call is sucessivly
            print(solver(top, bottom, inter_values[1]))
            print(solver(top, bottom, inter_values[2]))


# auxillary stuff

def split_terms(term): # this breaks (x)(x+2) into terms x and X+2
    arr = term.split('(')
    for i in range(len(arr)):
        arr[i] = arr[i].strip(')')
        if not arr[i]:
            print("found emtpy value ")
    arr.remove('')
    return arr
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

def solver(top,bottom,current_inter_value): # the solver takes all denom and numerator ,
    top_s = []
    bottom_s = []
    top_s = top[:] #  creates a barrier for the lists so the origional does not get modified .
    bottom_s = bottom[:] # so this is bizzare but it seems to keep the list local, you need the ":"

    for i in range(len(bottom_s)):

        try:
            top_s[i] = top_s[i].replace("s",str(current_inter_value))
        except:
            pass
        bottom_s[i] = bottom_s[i].replace("s",str(current_inter_value))
        #toss out the zero entry
        if eval(bottom_s[i]) == 0:
            bottom_s[i] = 1
        else:
            bottom_s[i] = eval(bottom_s[i])
    for i in range(len(bottom_s)):
        try:
            bottom_s[0] = bottom_s[0] * bottom_s[i+1] # this is a problem
        except:
            return str(eval(top_s[0]))+"/"+str(bottom_s[0])
main()