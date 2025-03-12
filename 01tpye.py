# 2025.03.12
# 파이썬 수업 - 변수, 타입, 출력
# 타입 (형) - 정수 : int (integer) (복잡하지 않고 떨어지는 수)0.1.2.3
#            실수 : float (floating point)
#            문자열 : str (string)
#            논리값 : bool (boolean)

title = "시간계산"
sec = 3700
min = sec / 60
bigger = min > sec
print(sec, min, bigger)
print(type(title), type(sec), type(min), type(bigger))

a = int(10.99999999)  # floor 버림 , ceiling 올림 , round 반올림
b = float(10.3)
c = str(10.3)
print(type(a), type(b), type(c))
print(a)

sec1 = 1300; sec2 = 500
seca = sec1 + sec2
secs = sec1 - sec2
secm = sec1 * sec2

secd = sec1 / sec2

secq = sec1 // sec2
seqr = sec1 % sec2 # % 는 2로 나눈 나머지 값을 나타내는 문자
print(f'{seca=}, {secs=}, {secm=}, {secd=}, {secq=}, {seqr=}') # f string / f 문자열

# 화씨를 섭씨로 바꿈
# tc = (tf - 21) * 5/9
# tf = (tc * 9/5) + 32
tf = 39
tc = (tf - 32) * 5/9
print(f'{tf}===>{tc}')

tc = 37.7
tf = tc * 9 / 5 + 32
print(f'{tc}===>{tf}')

print(2 ** 3, 2 ** (1/2), 2** (-1/2)) # **은 제곱
