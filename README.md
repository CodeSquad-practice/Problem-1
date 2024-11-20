# Problem-1

## 무작위 배열 생성
우선 먼저 make_random_arr(start,end)라는 random array를 만드는 함수를 만들었다.  
이 함수는 순서대로 정렬된 배열에서 무작위 index를 선택하여,  
새로운 배열에 넣고, 원래 배열에서는 pop()을 원래 배열이 없어질 때 까지 반복한다.  

하지만, 배열 중간을 pop 하다보니 시간 복잡도가 늘어, fisher yates 알고리즘을 사용하게 되었다.  
파이썬에서는 shuffle 메서드가 존재하지만, 직접 구현해보았다.

## 입력받기
정확한 입력이 나올 때 까지 while 문을 통해 계속해서 입력을 받았다.  
","로 나누어 리스트에 넣었는데, 정확한 입력이 아닌 조건은
1. 리스트의 길이가 2가 아닌경우
2. 리스트의 각 element가 digit가 아닌경우  
(2번째 원소는 길이가 1 이상이며 처음 시작이 blank인 경우 blank를 없애고 다시)
3. 두 숫자가 범위를 벗어나는 경우
4. 두 숫자가 같은 경우 (조건에 명시되지는 않았지만 필요해보여 추가함)

# main 함수
arr의 정렬여부를 알려주는 sorted 변수를 통해 sorted==False 인 동안  
반복하여 입력받도록 했다. 입력을 받으면 input_nums 함수를 통해  
정확한 입력인지 확인하고, 정확한 입력을 받을 때 까지 반복한다.  
정확한 입력을 받으면, index 메서드로 숫자의 위치를 찾고, 자리를 바꾼다.  
자리를 바꾼 후 정렬되었는지 확인하는 is_sorted 함수를 실행하여  
sorted 변수를 업데이트한다.  
정렬이 되었다면 반복을 종료한다. 

#Problem -2 

## 무작위 배열 생성
1~16까지의 숫자를 무작위로 섞고, 순서대로 배열에 넣는다.  
단순히 무작위로 섞기만 하면 안되는데, 무작위로 섞인 배열에 따라 정렬이  
불가능할 수도 있기 때문이다. 
https://m.post.naver.com/viewer/postView.naver?volumeNo=17980703&memberNo=16868720
이 포스트의 내용을 보고, 랜덤함수에 대해 생각했다.
자신보다 자릿값이 큰 위치에 있으면서 크기가 작은 숫자는 몇 개인지 세어 보고 이 값을 f(n)이라 하자.
요약하자면 f(1)+f(2)+...f(15)=짝수가 되어야 배열을 풀 수 있다는 내용이다.
따라서 배열을 만들고, f값의 합을 구해, 짝수가 아니면 다시 배열을 생성하는 방식으로 구현하도록 했다.
