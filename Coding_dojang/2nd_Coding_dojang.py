# NOTE : 문자열의 공백제거

def conut_string():

    in_str = input('공백을 제거할 문자열을 입력하세요 : ')
    in_str = in_str.replace('\n','')
    in_str = in_str.replace('\t', '')
    in_str = in_str.replace(' ', '')

    return len(in_str)

if __name__ == '__main__':
    print(conut_string())

