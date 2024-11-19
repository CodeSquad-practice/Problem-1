import random

#무작위 배열 생성
def make_random_arr(start,end):
    arr=[i for i in range(start,end+1)]
    #Fisher-Yates 알고리즘 구현
    for i in range(len(arr)-1,-1,-1):
        idx=random.randint(0,i)
        arr[i],arr[idx]=arr[idx],arr[i]

    return arr

def is_sorted(arr):
    return arr==sorted(arr)

def main():
    arr=make_random_arr(1,8)
    sorted=False
    turn = 0

    print("간단 숫자 퍼즐")
    #정렬이 될때까지 반복
    while not sorted:
        #턴증가
        turn+=1
        print(f'\nTurn {turn}')
        print(arr,"\n")
        # 입력받고 교환
        num1,num2=input_nums()
        num1_idx=arr.index(num1)
        num2_idx=arr.index(num2)
        arr[num1_idx],arr[num2_idx] = arr[num2_idx] ,arr[num1_idx]
        sorted=is_sorted(arr)
    print(f'\n축하합니다! {turn}턴만에 퍼즐을 완성하셨습니다!')

def in_range(num):
    return num>0 and num<=8

def input_nums():
    while True:
        print("교환할 두 숫자를 입력>")
        nums=list(input().split(","))
        #2개가 아니면 다시
        if len(nums)!=2:
            print("\n잘못 입력하셨습니다. 다시 입력해주세요\n")
            continue

        num1,num2=nums[0],nums[1]
        #num2의 시작이 공백이면 공백제거
        if len(num2)>0 and num2[0]==" ":
            num2=num2[1:]
        #2개 모두 숫자인가?
        if not (num1.isdigit() and num2.isdigit()):
            print("\n잘못 입력하셨습니다. 다시 입력해주세요\n")
            continue
        # 2개 모두 범위 안인가?
        elif not (in_range(int(num1)) and in_range(int(num2))):
            print("\n잘못 입력하셨습니다. 다시 입력해주세요\n")
            continue
        # 2 숫자가 같은가?
        elif int(num1)==int(num2):
            print("\n잘못 입력하셨습니다. 다시 입력해주세요\n")
            continue
        
        return  int(num1),int(num2)
        


if __name__=="__main__":
    main()
