import bs4
import create_random_figure



world = bs4.BeautifulSoup(open("world_v1"), "xml")




quantity_red_box = 2
quantity_red_cylinder=3
quantity_red_sphere=4

quantity_green_box = 3
quantity_green_cylinder=3
quantity_green_sphere=2

quantity_blue_box = 1
quantity_blue_cylinder=2
quantity_blue_sphere=3



coordinate=open("coordinate.txt","w")

# box_red
if quantity_red_box !=0:
    full_text=create_random_figure.create_figure(create_random_figure.red_box,world,quantity_red_box,"box_red",coordinate)
    world=create_random_figure.create_soup(full_text)

# cylinder_red
if quantity_red_cylinder !=0:
    full_text=create_random_figure.create_figure(create_random_figure.red_cylinder,world,quantity_red_cylinder,"cylinder_red",coordinate)
    world=create_random_figure.create_soup(full_text)

# sphere_red
if quantity_red_sphere !=0:
    full_text=create_random_figure.create_figure(create_random_figure.red_sphere,world,quantity_red_sphere,"sphere_red",coordinate)
    world=create_random_figure.create_soup(full_text)

# box_green
if quantity_green_box !=0:
    full_text=create_random_figure.create_figure(create_random_figure.green_box,world,quantity_green_box,"box_green",coordinate)
    world=create_random_figure.create_soup(full_text)

# cylinder_green
if quantity_red_cylinder !=0:
    full_text=create_random_figure.create_figure(create_random_figure.green_cylinder,world,quantity_green_cylinder,"cylinder_green",coordinate)
    world=create_random_figure.create_soup(full_text)

# sphere_green
if quantity_red_sphere !=0:
    full_text=create_random_figure.create_figure(create_random_figure.green_sphere,world,quantity_green_sphere,"sphere_green",coordinate)
    world=create_random_figure.create_soup(full_text)

# box_blue
if quantity_blue_box !=0:
    full_text=create_random_figure.create_figure(create_random_figure.blue_box,world,quantity_blue_box,"box_blue",coordinate)
    world=create_random_figure.create_soup(full_text)

# cylinder_blue
if quantity_blue_cylinder !=0:
    full_text=create_random_figure.create_figure(create_random_figure.blue_cylinder,world,quantity_blue_cylinder,"cylinder_blue",coordinate)
    world=create_random_figure.create_soup(full_text)

# sphere_blue
if quantity_blue_sphere !=0:
    full_text=create_random_figure.create_figure(create_random_figure.blue_sphere,world,quantity_blue_sphere,"sphere_blue",coordinate)
    world=create_random_figure.create_soup(full_text)






coordinate.close()

f = open('mybot.world', "w")
for word in full_text:
    f.write(word)
    f.write("\n")
f.close()
