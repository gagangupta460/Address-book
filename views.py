
from asyncore import write
import sys
import csv
import re


def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)


# add(['vivek', 'katni MP', '483770', '9109440576', '09/10/2001'])
# add(['anuj', 'katni MP', '483770', '9109440577', '09/10/2001'])


def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data


# view()

def remove(i):
    def save(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    mobile = i

    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                 if element == mobile:
                    new_list.remove(row)
    save(new_list)


# remove('9109440576')
# view()


def update(i):
    
    def update_newlist(j):
        with open('data.csv', 'w', newline='')as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    Mobile = i[0]
    #['9109440576','vivek','katni MP','483770','9109440576','09/10/2001']

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == Mobile:
                    Name = i[1]
                    Address = i[2]
                    District = i[3]
                    Pincode = i[4]
                    Mobile = i[5]
                


                    data = [Name, Address, District, Pincode, Mobile]
                    index = new_list.index(row)
                    new_list[index] = data

    update_newlist(new_list)

# sample = ['7000513498','vivek','katni MP','483770','7000513498','09/10/2001']
# update(sample)

def search(i):
    data =[]
    Mobile = i

    with open ('data.csv', 'r')as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == Mobile:
                    data.append(row)
    print(data)
    return data
# search('9109440576')
