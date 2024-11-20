import random

#무작위 배열 생성
def can_solve(arr):
    cnt=0
    # 빈칸이 몇번째 행에 있냐에 따라 cnt의 값이 짝수여야하냐,홀수여야하냐가 달라짐
    # 2,4행이면 cnt가 짝수여야하고, 1,3행이면 cnt가 홀수여야함
    # 그렇기 때문에 1,3 행일 경우 cnt의 처음 시작을 홀수로 만들어줌
    for i in range(16):
        if arr[i]==0:
            cnt+=(i//4)+1
    #arr에서 숫자 하나를 뽑고
    for i in range(16):
        if arr[i] == 0:
            continue
        # 뽑은 숫자보다 자릿수가 큰 숫자들 중 뽑은 숫자보다 작은 숫자 구하기
        for j in range(i,16):
            if arr[j]==0:
                continue    
            if arr[i]>arr[j]:
                cnt+=1
    return cnt%2==0


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,15,14,0]
print(can_solve(a))

def make_random_arr():
    while True:
        arr=[i for i in range(16)]
        #Fisher-Yates 알고리즘 구현
        for i in range(len(arr)-1,-1,-1):
            idx=random.randint(0,i)
            arr[i],arr[idx]=arr[idx],arr[i]
        if can_solve(arr):
            # 2차원 배열로 바꿔서 전달
            board=[]
            idx=0
            for i in range(4):
                row=[]
                for j in range(4):
                    if arr[idx]==0:
                        arr[idx]=' '
                    row.append(f"[{arr[idx]:2}]")
                    idx+=1
                board.append(row)

            return board


arr= make_random_arr()
for elems in arr:
    for elem in elems:
        print(elem, end = ' ')
    print()



# def is_sorted(arr):
#     return arr==sorted(arr)

# def main():
#     arr=make_random_arr(1,8)
#     sorted=False
#     turn = 0

#     print("간단 숫자 퍼즐")
#     #정렬이 될때까지 반복
#     while not sorted:
#         #턴증가
#         turn+=1
#         print(f'\nTurn {turn}')
#         print(arr,"\n")
#         # 입력받고 교환
#         num1,num2=input_nums()
#         num1_idx=arr.index(num1)
#         num2_idx=arr.index(num2)
#         arr[num1_idx],arr[num2_idx] = arr[num2_idx] ,arr[num1_idx]
#         sorted=is_sorted(arr)
#     print(f'\n축하합니다! {turn}턴만에 퍼즐을 완성하셨습니다!')

# def in_range(num):
#     return num>0 and num<=8

# def input_nums():
#     while True:
#         print("교환할 두 숫자를 입력>")
#         nums=list(input().split(","))
#         #2개가 아니면 다시
#         if len(nums)!=2:
#             print("\n잘못 입력하셨습니다. 다시 입력해주세요\n")
#             continue

#         num1,num2=nums[0],nums[1]
#         #num2의 시작이 공백이면 공백제거
#         if len(num2)>0 and num2[0]==" ":
#             num2=num2[1:]
#         #2개 모두 숫자인가?
#         if not (num1.isdigit() and num2.isdigit()):
#             print("\n잘못 입력하셨습니다. 다시 입력해주세요\n")
#             continue
#         # 2개 모두 범위 안인가?
#         elif not (in_range(int(num1)) and in_range(int(num2))):
#             print("\n잘못 입력하셨습니다. 다시 입력해주세요\n")
#             continue
#         # 2 숫자가 같은가?
#         elif int(num1)==int(num2):
#             print("\n잘못 입력하셨습니다. 다시 입력해주세요\n")
#             continue
        
#         return  int(num1),int(num2)
        


# if __name__=="__main__":
#     main()
