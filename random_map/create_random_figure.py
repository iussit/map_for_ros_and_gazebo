import bs4
import random
import math
red_box = bs4.BeautifulSoup(open("figure//red_box"), "xml")
red_cylinder=bs4.BeautifulSoup(open("figure//red_cylinder"),"xml")
red_sphere=bs4.BeautifulSoup(open("figure//red_sphere"),"xml")

green_box = bs4.BeautifulSoup(open("figure//green_box"), "xml")
green_cylinder=bs4.BeautifulSoup(open("figure//green_cylinder"),"xml")
green_sphere=bs4.BeautifulSoup(open("figure//green_sphere"),"xml")

blue_box = bs4.BeautifulSoup(open("figure//blue_box"), "xml")
blue_cylinder=bs4.BeautifulSoup(open("figure//blue_cylinder"),"xml")
blue_sphere=bs4.BeautifulSoup(open("figure//blue_sphere"),"xml")


R=4.0

class figures:
    ox=0
    oy=0
    name=""


figure_list=[]


def create_figure(red_box,soup,quantity_red_box,string,coordinate):
    model_red_box = []
    for model in red_box.find_all('model'):
        if model.attrs["name"] == "unit_"+string:
            model_red_box.append(model)

    global_red_box_list = []
    red_box_list = []

    while (quantity_red_box != 0):
        temp = model_red_box[1]
        global_red_box = model_red_box[0]
        temp.attrs["name"] = "unit_"+string + "_" + str(quantity_red_box)

        for child in temp.link.descendants:
            if child.name == "pose":
                # print(child)
                rand_x = random.uniform(-9.5, 31.5)
                rand_y = random.uniform(-8.5, 31.5)
                coordinates = child.string
                coo_cyl = coordinates.split(" ")
                coo_cyl[0] = rand_x
                coo_cyl[1] = rand_y
                figure=figures()
                figure.ox,figure.oy,figure.name=coo_cyl[0],coo_cyl[1],string
                figure_list.append(figure)



                if len(figure_list) > 1:
                    for form1 in figure_list:
                        count = 0
                        while(True):
                            for form in figure_list:
                                diff_oy=form.oy-form1.oy
                                diff_ox=form1.ox-form.oy
                                hyp= math.hypot(diff_ox,diff_oy)
                                if(hyp!=0):
                                    if(hyp>=R):
                                        count+=1
                                    else:
                                        while(hyp<R):
                                            coo_cyl[0] = random.uniform(-9.5, 31.5)
                                            coo_cyl[1] = random.uniform(-8.5, 31.5)
                                            form.ox, form.oy = coo_cyl[0], coo_cyl[1]
                                            diff_oy = form.oy - form1.oy
                                            diff_ox = form1.ox - form.oy
                                            hyp = math.hypot(diff_ox, diff_oy)
                                        count+=1
                            # print(str(count)+" "+str(len(figure_list)))
                            if count > len(figure_list)-1:
                                break




                coordinate.write(str(figure.ox)+" "+str(figure.oy)+" "+figure.name+"\n")
                child.string = ""
                temp.pose.string = ""
                global_red_box.pose.string = ""

                for i in coo_cyl:
                    child.string += str(i) + " "
                    temp.pose.string += str(i) + " "
                    global_red_box.pose.string += str(i) + " "

        red_box_list.append(str(temp))
        global_red_box.attrs["name"] = "unit_"+string + "_" + str(quantity_red_box)
        global_red_box_list.append(str(global_red_box))
        quantity_red_box -= 1

    full_text = str(soup).split("\n")
    full_text_list = full_text

    i = 0
    while (i < len(red_box_list)):
        count = 0
        for word in full_text_list:
            if word == "<sim_time>13 781000000</sim_time>":
                full_text.insert(count, red_box_list[i])
                break;
            count += 1
        i += 1

    i = 0
    while (i < len(global_red_box_list)):
        count = 0
        for word in full_text_list:
            if word == "<gravity>0 0 -9.8</gravity>":
                full_text.insert(count, global_red_box_list[i])
                break;
            count += 1
        i += 1

    # print(len(figure_list))
    return full_text

def create_soup(full_text):
    f = open('result_world', "w")
    for word in full_text:
        f.write(word)
        f.write("\n")
    f.close()
    soup=bs4.BeautifulSoup(open("result_world"),"xml")
    return soup

