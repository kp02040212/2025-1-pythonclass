# 2025.4.2 파이썬수업 프로젝트 두번재
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지 숫자중, 가장 많은 단계를 거쳐서 1로 가는 수는 무엇인가?, 가장 많은 단계는 몇단계인가
# 규칙: n짝수 -> n/2
#      n홀수 -> 3 * n + 1
#   예: 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5단계)
#from sympy.polys.subresultants_qq_zz import res_q
# from statsmodels.sandbox.distributions.mv_normal import np_pi
# from sympy.stats.sampling.sample_numpy import numpy
# from p02Collaz import ncount

import numpy as np
import  statistics
import time
from p02Collatzfunc import  collatz

MAXNUM =  100

#2025.4.9 우박수 프로젝트 두번째: 기본 통계량 구하기
# numpy 배열,list 두가지 방식 으로 시험
# 구하는 통계량: 최대값 평균 ,중앙값, 표준 편차, 최빈값, 최대값
# 단계의 갯수를 셀것
# n을 1부터 99까지 변화하면서 각각의 단계수를 풀력할것
# 그중 가장 큰 수를 찾을 것


# 리스트 방식
start = time.time()
ncountl = []

for n  in range(1,MAXNUM):
  ncount = collatz(n)
  ncountl.append(ncount)

print(ncountl)
print(sum(ncountl) / len(ncountl))

# 최대값 평균, 중앙값, 표준편차, 최빈값,
#평균
print(f'평균={statistics.mean(ncountl):.5f}')
print(f'최대값={max(ncountl)}')
print(f'중앙값={statistics.median(ncountl)}')
#print(f'최빈값={statistics.mean(ncountl):.5f}')
print(f'표준편차={statistics.stdev(ncountl):.5f}')

end = time.time()
print(f'{end - start:.5f} 초가 걸렸습니다')


# numpy 넘파이 방식
from scipy import stats
ncounta = np.zeros(MAXNUM-1)
for n  in range(1,MAXNUM):
    # print(f'{n=}')
    ncount = 0
    i = n

    while i!= 1:
        if i % 2 == 1:
            i = 3 * i +1
        else:
            i = i / 2
        ncount = ncount + 1

    ncounta[n-1] = ncount


print(ncounta)
# print(f'최빈값={np.mode(ncounta).argmax():.5f}')
#최대값 평균, 중앙값, 표준편차, 최빈값, 평균
print(f'최대값={np.max(ncounta)}')
print(f'평균 = {np.mean(ncounta):.5f}')
print(f'중앙값={np.median(ncounta):.5f}')
print(f'표준편차={np.std(ncounta):.5f}')
print(f'{end - start:.5f} 초가 걸렸습니다')