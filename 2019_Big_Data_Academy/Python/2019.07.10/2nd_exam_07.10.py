# -*- coding : utf-8 -*-
# NOTE : 딕셔너리 자료형

# NOTE
# 딕셔너리 자료형은 키와 밸류로 구성됨.
dic = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
dic2 = {1 : 'hi'}
dic3 = {'a' : [1, 2, 3]}
print(dic)
print(dic2)
print(dic3)

# NOTE : 딕셔너리 쌍 추가, 삭제

# NOTE : 쌍 추가
dic4 = {1:'a'}
dic4[2] = 'b'
dic4['name'] = 'pey'
print(dic4)
# NOTE : 쌍 삭제
del dic4['name']
print(dic4)

# NOTE : Key를 이용해 value얻기
dic5 = {'pey' : 10, 'julliet' : 99}
dic6 = {1 : 'a', 2 : 'b'}
dic7 = {'a' : 1, 'b' : 2}
print(dic5['julliet'])
print(dic6[1], dic6[2])
print(dic7['a'], dic7['b'])

# NOTE
# 키값은 중복되면 안된다.
# 중복 될 시에 맨 마지막 하나만 남겨두고 나머지는 무시된다.
# dic8 = {a : 1, a : 2}

# NOTE : 딕셔너리 관련함수

# NOTE : 키, 밸류 리스트 만들기
dic8 = {'name' : 'pey', 'phone' : '100993323', 'birth' : '1118'}
print(dic8.keys())
print(dic8.values())

for rep in dic8.keys():
    print(rep)

keys = list(dic8.keys())
values = list(dic8.values())
print(keys)
print(values)

# NOTE : 딕셔너리 쌍 얻기
print(dic8.items())
# NOTE : 딕셔너리 모두 지우기
dic8.clear()
print(dic8)

# NOTE : get함수
print(dic.get('name'))


# NOTE
# dic['nokey']는 에러가 나지만, dic.get('nokey')는 None을 반환

# NOTE
# 키 값이 딕셔너리에 없지만, 디폴트 값을 반환하게 하고 싶은 경우 dic.get(x, 'default')로 지정하면 된다.
print(dic.get('none', 'No'))

# NOTE : 키 값 존재여부 확인
print('name' in dic)
print('nokey' in dic)

