# 2025.4.2 파이썬수업 프로젝트 두번재
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지 숫자중, 가장 많은 단계를 거쳐서 1로 가는 수는 무엇인가?, 가장 많은 단계는 몇단계인가
# 규칙: n짝수 -> n/2
#      n홀수 -> 3 * n + 1
#   예: 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5단계)
from sympy.polys.subresultants_qq_zz import res_q

n = 10

# 단계의 갯수를 셀것
# n을 1부터 99까지 변화하면서 각각의 단계수를 풀력할것
# 그중 가장 큰 수를 찾을 것
maxvalue = 0
maxvaluen = 0

for n  in range(1,100):
    # print(f'{n=}')
    ncount = 0
    i = n

    while i!= 1:
        if i % 2 == 1:
            i = 3 * i +1
        else:
            i = i / 2
        ncount = ncount + 1


    print(f'{ncount}')
    if  maxvalue < ncount:
        maxvalue = ncount
        maxvaluen = n

print(f'{maxvalue=},{maxvaluen=}')

