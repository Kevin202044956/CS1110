# Kaiwen Zhu(kz8pr) Yanwen Wang(yw9cj)
import math
import webbrowser

lat_1 = float(input("Enter the latitute: "))
lon_1 = float(input("Enter the longtitude: "))

file = open('location.csv', 'r')
data1 = file.read()
data2 = data1.strip().split('\n')
closest_distance = 10000000000000


def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1) * math.sin(lat_2) + math.cos(lat_1) * math.cos(lat_2) * math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06  # 69.09 = circumference of earth in miles / 360 degrees
    return dist


for line in data2:
    cells = line.split(',')
    lat_2 = float(cells[0])
    lon_2 = float(cells[1])
    store_name = cells[2]
    state = cells[3]
    street = cells[4]
    city = cells[5]
    state_and_postal_code = cells[6]
    distance = distance_between(lat_1, lon_1, lat_2, lon_2)
    if distance < closest_distance:
        closest_distance = distance
        closest_street = street
        closest_city = city
        closest_state_and_postal_code = state_and_postal_code

webbrowser.open('http://maps.google.com/maps?q=' + closest_street + closest_city + closest_state_and_postal_code)
