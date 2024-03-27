from tkinter import *
import math
import random

#Setting a class to write down the destination points
class City:
    def __init__(self, coordinates, name):
        self.coordinates = coordinates
        self.name = name

#Setting up the lists that we will need
fake_origin_list = []
list_origin = []
distance_to_weight_center = []
closests_to_weight_center = []
last_list = []
sorted_sum_distance = []
sum_one = 0
sum_two = 0

for i in range(50):
    a = City((random.randint(0, 700), random.randint(0, 800)), str(i))
    list_origin.append(a)


def calculate(av_x, av_y):
    distance_to_weight_center.clear()
    for aa in list_origin:
        distance_to_weight_center.append([int(math.sqrt((av_x-aa.coordinates[0])**2 + (av_y-aa.coordinates[1])**2)), aa.name])
    for b in distance_to_weight_center:
        closests_to_weight_center.append(b[0])
    closests_to_weight_center.sort()
    return closests_to_weight_center[-1]


def city_finder(distance):
    for i in distance_to_weight_center:
        if i[0] == distance:
            last_list.append(i)
            distance_to_weight_center.remove(i)
            for dd in list_origin:
                if int(dd.name) == int(i[1]):
                    fake_origin_list.append(dd)
                    list_origin.remove(dd)

            break
    return last_list[0][0]


xx = 0

def city_finder_two():
    summone = 0
    summtwo = 0
    for a in list_origin:
        summone += a.coordinates[0]
        summtwo += a.coordinates[1]
    avg_x = sum_one / len(list_origin)
    avg_y = sum_two / len(list_origin)
    sumfd = int(city_finder(calculate(avg_x,avg_y)))
    for asdf in list_origin:
        if int(asdf.name) == int(last_list[0][1]):
            ff = asdf
            awq = int(ff.coordinates[0])
            b = int(ff.coordinates[1])
            for i in list_origin:
                c = int(i.coordinates[0])
                d = int(i.coordinates[1])
                sorted_sum_distance.append([math.sqrt((awq-c)**2+(b-d)**2) +sumfd,i.name])
            sorted_sum_distance.sort()
            return sorted_sum_distance[0][0]

for i in range(50):
    for a in list_origin:
        sum_one += a.coordinates[0]
        sum_two += a.coordinates[1]
    avg_x = sum_one / len(list_origin)
    avg_y = sum_two / len(list_origin)
    if i == 0:
        city_finder(calculate(avg_x,avg_y))
    else:
        city_finder_two()

window=Tk()
window.config(bg='White')
window.title('Hello Python')
window.geometry("1000x1000+10+20")
canvas = Canvas(width = 800, height = 900, bg = "white")
canvas.pack(pady = 5)

total_road = 0
for i in fake_origin_list:
    canvas.create_oval(i.coordinates[0]-3,i.coordinates[1]-3,i.coordinates[0]+3,i.coordinates[1]+3, fill="Black")
for i in range(len(fake_origin_list)):
    if i == len(fake_origin_list)-1:
        total_road += math.sqrt((fake_origin_list[i].coordinates[0]-fake_origin_list[0].coordinates[0])**2 + (fake_origin_list[i].coordinates[1] - fake_origin_list[0].coordinates[1])**2)
        canvas.create_line(fake_origin_list[i].coordinates[0], fake_origin_list[i].coordinates[1], fake_origin_list[0].coordinates[0],fake_origin_list[0].coordinates[1], width=2, fill='Blue')
    else:
        total_road += math.sqrt((fake_origin_list[i].coordinates[0]-fake_origin_list[i+1].coordinates[0])**2 + (fake_origin_list[i].coordinates[1] - fake_origin_list[i+1].coordinates[1])**2)
        canvas.create_line(fake_origin_list[i].coordinates[0],fake_origin_list[i].coordinates[1],fake_origin_list[i+1].coordinates[0],fake_origin_list[i+1].coordinates[1],width=2,fill='Blue')
Label(window, text= total_road).place(x=400,y=3)
window.mainloop()