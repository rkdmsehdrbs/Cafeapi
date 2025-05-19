print("컴포즈 메뉴 검색")
# 네이버 검색 API 예제 - 블로그 검색 (컴포즈 메뉴)
import os
import sys
import urllib.request
import json

print("네이버 '컴포즈 메뉴' 블로그 검색 시작")

# ----------------------------------------------------------------------
# 중요: 본인의 네이버 API Client ID와 Client Secret 값을 입력하세요.
# 네이버 개발자 센터(https://developers.naver.com/)에서 애플리케이션 등록 후 발급받을 수 있습니다.
client_id = "kNwlVzalbhmAD4rJveVh"
client_secret = "J_eV8qvXWk"
# ----------------------------------------------------------------------

# API 키가 입력되었는지 확인
if client_id == "YOUR_NAVER_CLIENT_ID" or client_secret == "YOUR_NAVER_CLIENT_SECRET":
    print("=" * 50)
    print("주의: 코드에 네이버 API Client ID와 Client Secret 값을 입력해야 합니다.")
    print("1. 네이버 개발자 센터(https://developers.naver.com/)에 접속하여 로그인합니다.")
    print("2. 'Application' 메뉴에서 '애플리케이션 등록'을 선택합니다.")
    print("3. '애플리케이션 이름'을 정하고 '비로그인 오픈 API 서비스 환경'에서 '검색'을 선택 후 등록합니다.")
    print("4. 등록된 애플리케이션 정보에서 Client ID와 Client Secret 값을 확인하여 코드에 입력합니다.")
    print("=" * 50)
    sys.exit() # ID, Secret이 없으면 프로그램 종료

# 검색어 설정
search_query = "컴포즈 메뉴"
encText = urllib.parse.quote(search_query)

# API URL 설정 (블로그 검색, JSON 결과 요청)
# display: 한 번에 가져올 검색 결과 개수 (기본값: 10, 최대: 100)
# start: 검색 시작 위치 (기본값: 1, 최대: 1000)
display_count = 20 # 예시로 20개 요청
url = f"https://openapi.naver.com/v1/search/blog?query={encText}&display={display_count}&start=1"

# API 요청 객체 생성 및 헤더 추가
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

raw_json_response = "" # API로부터 받은 원본 JSON 문자열을 저장할 변수
extracted_list = []    # 추출된 데이터를 저장할 리스트

try:
    print(f"\n'{search_query}'에 대한 블로그 검색을 API에 요청합니다...")
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        raw_json_response = response_body.decode('utf-8') # API 응답을 UTF-8로 디코딩
        print("API 응답을 성공적으로 받았습니다.")

        # JSON 데이터 파싱
        # print("\n--- API 원본 JSON 응답 (일부) ---")
        # print(raw_json_response[:500] + "..." if len(raw_json_response) > 500 else raw_json_response)

        data = json.loads(raw_json_response) # 문자열 형태의 JSON을 Python 딕셔너리/리스트로 변환

        # 'items' 리스트에서 필요한 정보 추출
        if 'items' in data and data['items']:
            print(f"\n총 {len(data['items'])}개의 검색 결과를 처리합니다.")
            for item_index, item in enumerate(data['items']):
                # HTML 태그 제거 (제목과 설명에서 자주 발견됨)
                # <b> 태그 외 다른 HTML 태그가 있을 경우 추가적인 처리가 필요할 수 있습니다.
                title_cleaned = item.get("title", "제목 없음").replace("<b>", "").replace("</b>", "")
                description_cleaned = item.get("description", "내용 없음").replace("<b>", "").replace("</b>", "")

                extracted_item = {
                    "title": title_cleaned,
                    "link": item.get("link", "링크 없음"),
                    "description": description_cleaned,
                    "bloggername": item.get("bloggername", "블로거명 없음"),
                    "postdate": item.get("postdate", "날짜 없음") # YYYYMMDD 형식
                }
                extracted_list.append(extracted_item)
                # print(f"  {item_index + 1}. \"{title_cleaned[:30]}...\" 처리 완료")
        else:
            print("API 응답에 'items' 필드가 없거나 비어있습니다.")
            if 'errorMessage' in data: # 에러 메시지가 있는지 확인
                print(f"  네이버 API 에러 메시지: {data['errorMessage']}")
                print(f"  네이버 API 에러 코드: {data.get('errorCode', 'N/A')}") # 에러 코드가 있다면 함께 출력

    else:
        print(f"API 요청 실패: Error Code {rescode}")
        # 오류 발생 시 응답 내용 확인 (JSON 형태일 수 있음)
        try:
            error_response_body = response.read().decode('utf-8')
            print(f"Error Response Body: {error_response_body}")
        except Exception as e_read:
            print(f"에러 응답 본문 읽기 실패: {e_read}")


except urllib.error.HTTPError as e:
    # HTTP 에러 (예: 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Internal Server Error)
    print(f"HTTP 에러 발생: {e.code} {e.reason}")
    try:
        error_details = e.read().decode('utf-8')
        print(f"에러 상세 정보: {error_details}")
        # 네이버 API 에러는 JSON 형태일 수 있으므로 파싱 시도
        try:
            error_json = json.loads(error_details)
            if 'errorMessage' in error_json:
                print(f"  네이버 API 에러 메시지: {error_json['errorMessage']}")
            if 'errorCode' in error_json:
                 print(f"  네이버 API 에러 코드: {error_json['errorCode']}")
        except json.JSONDecodeError:
            pass # JSON 파싱 실패 시 추가 작업 없음
    except Exception as e_read:
        print(f"HTTP 에러 상세 정보 읽기 실패: {e_read}")
except urllib.error.URLError as e:
    # URL 에러 (예: 네트워크 연결 실패)
    print(f"URL 에러 발생: {e.reason}")
except json.JSONDecodeError as e:
    print(f"JSON 파싱 에러 발생: {e}")
    print("API로부터 받은 응답이 유효한 JSON 형식이 아닙니다.")
    print(f"원본 응답 (일부): {raw_json_response[:500]}" if raw_json_response else "원본 응답 없음")
except Exception as e:
    # 기타 예외 처리
    print(f"알 수 없는 에러 발생: {e}")
    import traceback
    traceback.print_exc()


# 추출된 데이터를 JSON 형식으로 출력
if extracted_list:
    print("\n\n--- 추출된 데이터 (Python 리스트 of 딕셔너리) ---")
    # for item_data in extracted_list:
    # print(item_data) # 각 아이템(딕셔너리) 출력 (너무 길면 주석 처리)

    print("\n--- 추출된 데이터를 JSON 문자열로 변환하여 출력 ---")
    # indent=2 옵션은 JSON 문자열을 사람이 보기 좋게 들여쓰기합니다.
    # ensure_ascii=False 옵션은 한글이 유니코드 이스케이프 시퀀스(\uXXXX)로 변환되지 않고 그대로 출력되도록 합니다.
    final_json_output = json.dumps(extracted_list, indent=2, ensure_ascii=False)
    print(final_json_output)

    # 파일로 저장 (옵션)
    output_filename = "compose_menu_blog_search.json"
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(final_json_output)
        print(f"\n추출된 데이터가 '{output_filename}' 파일로 저장되었습니다.")
    except Exception as e:
        print(f"\n'{output_filename}' 파일 저장 중 오류 발생: {e}")

else:
    print("\n추출된 데이터가 없습니다.")

print("\n'컴포즈 메뉴' 블로그 검색 완료.")