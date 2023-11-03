# Crawling_code


## news folder

[news](https://github.com/eunkk01/Crawling_code/tree/main/news)

#### 1-1.naver_news_link_crawl

- 네이버에 검색 쿼리 날려서 해당 날짜에 올라온 뉴스 전부 수집
  - 네이버 뉴스 툴 존재 유무 표시(is_status=1: 존재O / is_status=0: 존재X)
  - 언론사와 기사 제목으로 중복 drop


#### 1-2.naver_news_text_crawl

- 수집된 네이버 기사 링크 중 네이버 뉴스 툴에 존재하는 기사 내용만 수집(http://n.news.naver.com/...)


#### 2-1.daum_news_crawl

- 네이버 뉴스 툴이 아닌 기사들만 다음에다가 title로 검색 날려서 수집
  - 다음 뉴스 툴이 있는 기사들만 걸러서 수집(http://v.daum.net/v/...)


#### 2-2.daum_news_text_crawl

- 다음에서 수집된 뉴스 기사 내용 수집


-----------


## naver_news_TV연예 folder

[naver_news_TV연예](https://github.com/eunkk01/Crawling_code/tree/main/naver_news_TV%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%8B%E1%85%A8)

#### 1.naver_news_TV연예_link_crawl

- 네이버 뉴스 중 TV연예 섹션의 뉴스 수집
  - https://entertain.naver.com/now#sid=106&date={D}&page={page_num}


#### 2.naver_news_TV연예_text_crawl

- 기사 텍스트 수집


#### 3.naver_news_text_preprocessing

- 의미없는 텍스트 전처리 진행
