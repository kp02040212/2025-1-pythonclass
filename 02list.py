# 인덱싱
colors = ['red', 'blue','green']
print(colors) # 리스트 전체 출력
print(colors[1]) # 리스트 두번째 원소 출력 , 0부터 시작
print(colors[-1]) # 리스트 마지막 원소 출력
print(len(colors)) # 리스트 길이 출력



sities = ['서울','부산','인천','의정부','대전','강릉','논산','포항']
print(sities[0:5]) #cities[0:n] 0~ n-1 표시
print(sities[:7]) # 0 ~ 6 번쨰 원소
print(sities[:-1]) # 0 ~ -2 까지
print(sities[3:])
print(sities[:]) # 전부표시
print(sities[-4:]) # 뒤에서부터 4번째 까지
print(sities[:7:2]) # 처음부터 6번째 원소까지, 한간씩 건너뜀
print(sities[::3]) # 처움부터 끝까지 , 3칸씩 건너 뜀
print(sities[::-1]) # 처음부터 끝까지 , 거꾸로
print(sities[4::-2])

# 리스트의 추가
colors = ['red', 'blue','green']
colors.append('white') # white 추가
print(colors[:]) # 출력
colors.extend(['black','purple'])
print(colors[:])
colors.insert(1,'orange')
print(colors[:])
colors.remove('purple')
print(colors[:])
colors[1] = 'sky'
print(colors[:])

# 패킹, 언패킹
c1, _, c2, c3, _, _ = colors # 언패킹 세트에 있는 것에서 하나씩 뺀다
print(c1, c2, c3)

# 다차원 리스트
colors = ['red', 'blue','green']
sities = ['서울','부산','인천','의정부','대전','강릉','논산','포항']
combi = [colors, sities]
print(combi)
print(combi[1][2]) # 인천
# print(combi[2][3]) # 에러
bigcombi = [combi, [0,2,7]]
print(bigcombi)
print(len(bigcombi))
print(bigcombi[0][1][2]) # 인천
print(bigcombi[1][1]) # 2


# 퀴즈
first = ["egg","salad","bread","soup","canafe"]
second = ["fish","lemb","pork","beek","chicken"]
third = ["apple","banana","orange","grape","mango"]

order = [first,second,third]
john = [order[0][:-2],second[1::3],third[0]] #john = ["soup", [len,chicken],apple
print(john)
del john[2] # john = [soup,[lamd, chicken]]
john.extend([order[2][0:1]]) # john = [soup,[lamd, chicken]], [apple]
print(john)