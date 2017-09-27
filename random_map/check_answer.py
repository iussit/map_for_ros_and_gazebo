import math


answer=open("coordinate2.txt")
true=open("coordinate.txt")


R=5.0


class figures:
    ox = 0
    oy = 0
    name = ""

answer_figures_list=[]
true_figures_list=[]
error=0



for line in answer:
    word = []
    word=line.split(" ")
    figure=figures()
    figure.ox,figure.oy,=float(word[0]),float(word[1])
    new_word=""

    for i in range(len(word[2])):
        if word[2][i]=="\n":
            break
        new_word+=word[2][i]

    figure.name=new_word
    answer_figures_list.append(figure)

for line in true:
    word = []
    word=line.split(" ")
    figure=figures()
    figure.ox,figure.oy,figure.name=float(word[0]),float(word[1]),word[2]
    new_word = ""

    for i in range(len(word[2])):
        if word[2][i] == "\n":
            break
        new_word += word[2][i]

    figure.name = new_word
    true_figures_list.append(figure)


numbers=[]
count_name=0
for true_figures in true_figures_list:
    count=0
    check_name=0
    for answer_figures in answer_figures_list:
        diff_oy = true_figures.oy - answer_figures.oy
        diff_ox = true_figures.ox - answer_figures.oy
        hyp = math.hypot(diff_ox, diff_oy)
        if (hyp<=R):
            if true_figures.name != answer_figures.name:
                check_name+=1
            count_name+=check_name
            count+=1



    if count > 1:
        temp_error=[]
        if check_name!=0:
            error+=0.5

        # error=
        check_numbers=0
        for answer_figures in answer_figures_list:
            diff_oy = true_figures.oy - answer_figures.oy
            diff_ox = true_figures.ox - answer_figures.oy
            hyp = math.hypot(diff_ox, diff_oy)
            if(hyp<=R):
                temp_error.append(hyp/R)
                numbers.append(check_numbers)
            check_numbers+=1
        error+=temp_error[0]
        temp_error.pop(0)
        s=0
        for temp in temp_error:
            s+=temp
        error+=math.log2(s)
        # for number in numbers:
        #     answer_figures_list.pop(number)


    if count == 1:
        number=0
        if check_name!=0:
            error+=0.5
        for answer_figures in answer_figures_list:
            diff_oy = true_figures.oy - answer_figures.oy
            diff_ox = true_figures.ox - answer_figures.oy
            hyp = math.hypot(diff_ox, diff_oy)
            if (hyp <= R):
                error+=hyp/R
                numbers.append(number)
                answer_figures_list.pop(number)
            number+=1

    if count==0:
        error+=1.5







print("Error:"+" "+str(error))
print("False detection:"+" "+str(len(numbers)))
print("Detection with false name:"+" "+str(count_name))







