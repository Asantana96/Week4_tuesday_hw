num_list = [10,8,1,4,9,3,12,5]

def bubble_sort(alist):
    is_sorted = False
    right_boundary = len(alist) -1
    while not is_sorted:
        is_sorted = True
        for i in range(right_boundary):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                is_sorted = False
        right_boundary -=1
        print(alist)

bubble_sort(num_list)

print(num_list)