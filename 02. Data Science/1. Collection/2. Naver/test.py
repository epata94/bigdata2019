import json
import re

with open('이명박_naver_news.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_data = json.loads(json_string)


def analysis():
    print('=' * 10, '빅데이터 분석기', '=' * 10)
    # keyword = input('분석 키워드를 입력하세요 : ')
    keyword = '이명박'
    print('\n 데이터 분석을 시작합니다..')
    not_link = 0
    link = []
    text = re.compile('//.+?/')
    for i in json_data:
        if i['org_link']:
            re_text = text.search(i['org_link']).group()[2:-1]
            link.append(re_text)
        if not i['org_link']:
            print('org_link가 없는 기사를 발견했습니다.')
            not_link += 1

    print('\n<네이버 검색 빅데이터 분석>')
    print('검색어 : %s' % keyword)
    print('전체 도메인 수 : %s' % len(set(link)))
    print('전체 건수 : %s' % (len(json_data) - not_link))
    print('부정확한 데이터 수 : %s' % not_link)

    count = {}
    for i in link:
        try:
            count[i] += 1
        except:
            count[i] = 1

    print('도메인 별 기사 분석 : ')
    print(count)


analysis()