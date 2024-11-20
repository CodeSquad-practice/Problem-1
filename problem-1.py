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
                    row.append(arr[idx])
                    idx+=1
                board.append(row)

            return board


# arr= make_random_arr()
# for elems in arr:
#     for elem in elems:
#         print(elem, end = ' ')
#     print()

def print_arr(arr):
    for elems in arr:
        for elem in elems:
            if elem == 0:
                print('[  ]',end='')
            else:
                print(f'[{elem:2}]',end='')
        print()

def is_sorted(arr):
    target_arr=[]
    num=1
    for i in range(4):
        row=[]
        for j in range(4):
            row.append(num)
            num+=1
        target_arr.append(row)
    target_arr[3][3]=0
    
    return arr==target_arr

def find_blank(arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j]==0:
                return (i,j)

def main():
    arr=make_random_arr()
    sorted=False
    turn = 0
    print("재미있는 15 퍼즐!")
    #정렬이 될때까지 반복
    while not sorted:
        #턴증가
        turn+=1
        print(f'\nTurn {turn}')
        print_arr(arr)
        #br,bc 는 blank의 r,c
        br,bc=find_blank(arr)
        input_nums(br,bc,arr)     
        sorted = is_sorted(arr)
    print(f'\n축하합니다! {turn}턴만에 퍼즐을 완성하셨습니다!')

def in_arr_range(r,c):
    return r>=0 and r<4 and c>=0 and c<4

def input_nums(br,bc,arr):
    dxs,dys=[0,0,1,-1],[1,-1,0,0]
    while True:
        print("숫자 입력>")
        num=int(input())
        # num이 blank 와 인접한지 확인
        for dx,dy in zip(dxs,dys):
            nr=br+dx
            nc=bc+dy
            # 범위를 벗어나지 않고, num이면 자리이동
            if in_arr_range(nr,nc) and arr[nr][nc]== num:
                # 자리 이동
                arr[nr][nc],arr[br][bc]=arr[br][bc],arr[nr][nc]
                return
        # blank와 인접하지 않으면 패스
        print("다시 입력해 주세요.\n")
        
        
if __name__=="__main__":
    main()
