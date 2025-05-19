# cafe.py 에서 함수 만들어서 모듈 포함시켜서 활용
import cafe
print("컴포즈 커피")

# 여기에서 메인 프로그램 작성
# 메뉴 검색: 메뉴를 입력하면 cafe 함수로 가서 결과가
search = input("메뉴 검색: ")
# 결과가 나오는 프로그램 만들기
cafe.nblog(search)