'''///////////////////////////////////
인덱싱 - 문자열의 순서
a = "Life is too short, You need Python"
print(a[1]) = i
print(a[-2]) = o
슬라이싱
[시작:끝:간격]
a = "Life is too short, You need Python"
print(a[0::])
print(a[0:5:])
print(a[3:8:])
print(a[::2])
i를 y로 수정하기
a="pithon"
print(a[0]+"y"+a[2:])
//////////////////////////////////////'''

'''///////////////////////////////////
문자열 포매팅
numbur = 10
day = "three"
a= "i eat %d apple %s days" %(numbur,day)
print(a)
%s - 문자열
%c - 문자 1개
%d - 정수
%f - 부동 소수
%o - 8진수
%x - 16진수
%% - %문자
%s는 뒤에 붙는 값을 무조건 문자로 집어 넣는다
a = "error is %s%%" %(50)
print(a)
///////////////////////////////////////'''

'''////////////////////////////////////
정렬과 공백
a= "%10s jane" % ("hi") - 오른쪽으로 10칸을 띄우고 hi 출력
print(a)
a= "%-10s jane"  % ("hi") - 왼쪽으로 10칸을 띄우고 hi 출력
print(a)
///////////////////////////////////////'''

'''////////////////////////////////////
소수점 표현하기
a="%0.4f" %(1.23456789) - 소수점 4째자리 반올림
print(a)
a="%10.6f" %(1.23456789) - 총10개인 문자열에서 6째자리 반올림
print(a)
///////////////////////////////////////'''
'''///////////////////////////////////////
Format 함수
a="i eat {0} apple".format(3)
print(a)
a="i eat {0} apple".format("five")
print(a)
num = 5
a="i eat {0} apple".format(num)
print(a)
num = 10
day = "three"
a="i eat {0} apple. so i was sick for {1} days.".format(num, day)
print(a)
a="i eat {1} apple. so i was sick for {0} days.".format(num, day)
print(a)
a="i eat {num} apple. so i was sick for {day} days.".format(num=1, day=2)
print(a)
a="i eat {0} apple. so i was sick for {day} days.".format(5, day=2)
print(a)
#왼쪽 정렬
a="{0:<10}".format("hi")
print(a)
#오른쪽 정렬
a="{0:>10}".format("hi")
print(a)
#가운데 정렬
a="{0:^10}".format("hi")
print(a)
#공백 채우기
a="{0:=^10}".format("hi")
print(a)
a="{0:!<10}".format("hi")
print(a)
a=1.23456789
#소숫점 4째자리 반올림
b="{0:0.4f}".format(a)
print(b)
#10자리수 소숫점4째자리 반올림
b="{0:10.4f}".format(a)
print(b)
#문자표현
a="{{and}}".format()
print(a)
//////////////////////////////////////////'''

'''//////////////////////////////////////////
f 문자열 포매팅
name = "hong"
age=30
a = f"나의 이름은 {name} 입니다. 나이는 {age} 입니다."
print(a)
a = f"내년에 나이는 {age+1} 입니다."
print(a)
d={'name':'jung','age':30}
a = f'나의 이름은 {d["name"]} 이고 나이는 {d["age"]} 입니다.'
print(a)
#왼쪽 정렬
a=f'{"hi":<10}'
print(a)
#오른쪽 정렬
a=f"""{"hi":>10}"""
print(a)
#가운데 정렬
a=f"""{"hi":^10}"""
print(a)
#공백 채우기
a=f"""{"hi":=^10}"""
print(a)
a=f"""{"hi":!<10}"""
print(a)
y=1.23456789
a=f'{y:0.4f}'
print(a)
a=f'{y:10.4f}'
print(a)
a=f"{{jung}}"
print(a)
#나 혼자 코딩
## '!!!pyrhon!!!' 문자열을 출력해 보자
a=f"{'python':!^12}"
print(a)
//////////////////////////////////////////'''

'''//////////////////////////////////////////
문자열 관련 함수
///////////////////////////////////////////'''
# 문자 개수 세기 (count)
a="hobby"
b=a.count('b')
print(b)
#위치 알려주기1(find)
a="python is the best choice"
b=a.find('b')
print(b) #14번째에 b가 있음
b=a.find('k')
print(b) #원하는 글자가 없으면 -1로 표시
#위치알려주기 2(index)
a="life is too short"
b=a.index('t')
print(b)
#b=a.index('k')
#print(b)# 원하는 글자가 없으면 error 처리

#문자열 삽입 (join)
a=",".join('abcd')
print(a)

#소문자를 대문자로 (upper)
a="hi"
b=a.upper()
print(b)

#대문자를 소문자로 (lower)
a="HI"
b=a.lower()
print(b)

#왼쪽 공백 지우기 (lstrip)
a="  hi  "
b=a.lstrip()
print(b)

#오른쪽 공백 지우기 (rstrip)
a="  hi  "
b=a.rstrip()
print(b)

#양쪽 공백 지우기 (strip)
a="  hi  "
b=a.lstrip()
print(b)

#문자열 바꾸기(replace)
a="Life is too short"
b=a.replace("Life", "you")
print(b)

#문자열 나누기(split)
a="Life is too short"
b=a.split()
print(b)
c="a:b:c:d"
d=c.split(':')
print(d)
