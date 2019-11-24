import requests # 요청을 보내고 응답을 변수에 저장하기 위해 필요한 모듈
from decouple import config # 인증키 보안을 위해 필요한 모듈
import datetime

SECRET_KEY = config('SECRET_KEY')
dt = datetime.datetime.now()
yyyy, mm, dd = dt.year, dt.month, dt.day

url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={SECRET_KEY}&targetDt={yyyy}+{mm}+{dd}'
# response