

def function(a,b):
    sum = 0
    for i in range(len(a)-1):
        sum += (b[i]-a[i])**2/b[i]
    return sum


list1 = [433.4617,76.2959,84.6501,216.3116,171.0371,36.2135,83.5383,14.7040,16.3199,41.6884,32.9629,6.7865]
list2 = [434,62,86,236,161,38,83,29,15,22,43,4]

print(function(list1,list2))

print(1-(6/7)**5)