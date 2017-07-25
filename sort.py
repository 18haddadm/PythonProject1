list = [5,1,4,2,3]

def sort(list):
    a = 0
    b = 1
    #reverse = switch a and b
    for value in range(1, len(list)):
        if (list[a] > list[b]):
            reverse(a, b, list)
        a = a + 1
        b = b + 1
        if (list[a] < list[b]):
            reverse

#while switch needed, continur on calling sort function

    return list

def reverse(a, b, list):
    c = list[a]
    list [a] = list [b]
    list [b] = c

    #write code that switches list[a] and list[b]
print ("Original list: "  + str(list))
print("Reversed list: " + str(sort(list)))
