import random

#무작위 배열 생성
def make_random_arr(start,end):
    arr=[i for i in range(start,end+1)]
    rand_arr=[]
    while arr:
        chosen_idx=random.randrange(0,len(arr))
        rand_arr.append(arr[chosen_idx])
        arr.pop(chosen_idx)

    return rand_arr

def main():
    arr=make_random_arr(1,8)
    turn = 1

    print("간단 숫자 퍼즐")
    print(f'Turn {turn}')
    print(arr)

    num1,num2=input_nums()
    num1_idx=arr.index(num1)
    num2_idx=arr.index(num2)
    arr[num1_idx],arr[num2_idx] = arr[num2_idx] ,arr[num1_idx]
    print(arr)

def in_range(num):
    return num>0 and num<=8

def input_nums():
    while True:
        print("교환할 두 숫자를 입력>")
        nums=list(input().split(","))
        #2개가 아니면 다시
        if len(nums)!=2:
            continue

        num1,num2=nums[0],nums[1]
        
        if not (num1.isdigit() and num2.isdigit()):
            continue
        elif not (in_range(int(num1)) and in_range(int(num2))):
            continue
        elif int(num1)==int(num2):
            continue
        
        return  int(num1),int(num2)
        


if __name__=="__main__":
    main()
