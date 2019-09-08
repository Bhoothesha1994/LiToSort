list=[1,5,6,2,3,6]
def sort(list):
    for i in list:
        value = list[i]
        i = 1
        while i>=0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i -= 1
            else:
                break

sort(list)

