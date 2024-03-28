#딕셔너리
d = {'a':1, 'b':2, 'c':3}
d.items() #key와 value를 출력하는 함수
#d[x] = d.get(x, 0) + 1 #이러한 형태로 딕셔너리 항목 없을 때 입력 가능

#셋
s = set(A) & set(B) # 교집합
L = set(A) - set(B) # 차집합

A.remove('a') # 셋에서 제거

#소트의 키 값을 주는 방법
A.sort(key = lambda x : (x*4)[:4], reverse = True)

#리스트 사용 법
dnf = [k for k, v in d.items() if v > 0]
