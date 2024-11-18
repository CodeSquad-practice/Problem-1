import random

#make random arr
#rand_arr = make_random_arr(1,9)
def make_random_arr(start,end):
    arr=[i for i in range(start,end+1)]
    rand_arr=[]
    while arr:
        chosen_idx=random.randrange(0,len(arr))
        rand_arr.append(arr[chosen_idx])
        arr.pop(chosen_idx)

    return rand_arr
