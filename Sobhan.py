'''
Buying and selling over the galaxy requires you to convert numbers and units, and you decided to write a program to help you.

The numbers used for intergalactic transactions follows similar convention to the roman numerals and you have painstakingly collected the appropriate translation between them.

Roman numerals are based on seven symbols:

Symbol  - Value

I     -   1

V     -   5

X     -   10

L     -   50

C     -   100

D     -   500

M     -   1000

The symbols "I", "X", "C", and "M" can be repeated three times in succession, but no more. (They may appear four times if the third and fourth are separated by a smaller 
value, such as XXXIX.) "D", "L", and "V" can never be repeated. "I" can be subtracted from "V" and "X" only. "X" can be subtracted from "L" and "C" only. "C" can be 
subtracted from "D" and "M" only. "V", "L", and "D" can never be subtracted. Only one small-value symbol may be subtracted from any large-value symbol. 
A number written in [16]Arabic numerals can be broken into digits. For example, 1903 is composed of 1, 9, 0, and 3. To write the Roman numeral, each of the non-zero digits
should be treated separately. Inthe above example, 1,000 = M, 900 = CM, and 3 = III. Therefore, 1903 = MCMIII.

You are expected to handle invalid queries appropriately.

Test input:
glob is I
prok is V
pish is X
tegj is L
glob glob Silver is 34 Credits 
glob prok Gold is 57800 Credits
pish pish Iron is 3910 Credits

how much is pish tegj glob glob ?
how many Credits is glob prok Silver ?
how many Credits is glob prok Gold ?
how many Credits is glob prok Iron ?
how much wood could a woodchuck chuck if a woodchuck could chuck wood ?

Test Output:
pish tegj glob glob is 42
glob prok Silver is 68 Credits
glob prok Gold is 57800 Credits
glob prok Iron is 782 Credits
I have no idea what you are talking about
'''


standard = "I have no idea what you are talking about"
symbols = {'i':1, 'v':5, 'x':10, 'l':50, 'c':100, 'd':500, 'm':1000}
ref_dict = {}
info_dict = {}
answers = []

def output_func(sen):
    print(sen)

def solve(word):
    n = 0
    try:
        digit = [ref_dict[i] for i in word]
    except:
        return -1

    while digit:
        popped = digit.pop(0)
        if digit and digit[0] > popped:
            n -= popped
        else:
            n += popped

    return n

def process():
    num_input_first = int(input("Enter the number of references and calculations: "))
    print()
    info_list = []
    for i in range(num_input_first):
        sen_input = input()
        info_list.append(sen_input)
    num_input_second = int(input("\nEnter the number of questions: "))
    print()
    ques_list = []
    for i in range(num_input_second):
        sen_input = input()
        ques_list.append(sen_input)
    info_list.extend(ques_list)

    for item in info_list:
        info_line = item
        ref_word_sen = info_line.lower().split(None)

        if not ref_word_sen:
            return

        if len(ref_word_sen) == 3 and ref_word_sen[1] == 'is':
            key = ref_word_sen[0]
            val = ref_word_sen[2]

            if not val in symbols:
                return output_func(f"{val} is not a correct roman numeral")
            else:
                ref_dict[key] = symbols[val]
                continue
        elif len(ref_word_sen) > 4 and ref_word_sen[-1] == 'credits' and ref_word_sen[-3] == "is":
            ref_word_sen.pop()
            try:
                val = float(ref_word_sen[-1])
            except:
                return output_func("Please enter correct numeric value")
                

            ref_word_sen.pop()
            ref_word_sen.pop()
            i = ref_word_sen.pop()
            n = solve(ref_word_sen)

            if n < 0:
                return output_func("I have no idea what you are talking about")
            
            info_dict[i] = val/n
            continue
        elif (ref_word_sen[0:3] == ['how', 'much', 'is']) or (ref_word_sen[0:3] == ['how', 'many', 'is']):
            ref_word_sen = ref_word_sen[3:]
            if ref_word_sen[-1] == '?':
                ref_word_sen.pop()

            n = solve(ref_word_sen)
            if n<0:
                answers.append(f"{' '.join(ref_word_sen)} is not a valid numeric value")
            else:
                answers.append(f"{' '.join(ref_word_sen)} is {n}")
        elif (ref_word_sen[0:4] == ['how', 'much', 'credits', 'is']) or (ref_word_sen[0:4] == ['how', 'many', 'credits', 'is']):
            ref_word_sen = ref_word_sen[4:]
            if ref_word_sen[-1] == '?':
                ref_word_sen.pop()
            ref_check = list(ref_word_sen)
            i = ref_word_sen.pop()
            if not i in info_dict:
                answers.append("I have no idea what you are talking about")
            elif (i in info_dict) and (ref_check[0] == i):
                answers.append(f"{i} is {float(info_dict[i])} credits")
            else:
                n = solve(ref_word_sen)
                if n<0:
                    answers.append(f"{' '.join(ref_word_sen)} is not a valid reference value")
                else:
                    answers.append(f"{' '.join(ref_word_sen)} {i} is {int(n*info_dict[i])} credits")
        else:
            answers.append("I have no idea what you are talking about")
    print()
    for answer in answers:
        print(answer)



process()



