from datetime import datetime
import pytz
# pip install pytz
# document : http://pytz.sourceforge.net/#example-usage

class Country:
    # 클래스를 완성하세요
    """Super Class
    - def __init__(country : str , continent: str, capital: str)
    - def show_info( ) -> 국가 정보 출력
    """
    def __init__(self,country : str , continent: str, capital: str):
        self.country = country
        self.continent = continent
        self.capital = capital

    def show_info(self):
        print('Country: ' + self.country)
        print('Continent: ' + self.continent)
        print('Capital: ' + self.capital)

class Time(Country):
    # 클래스를 완성하세요
    """Sub Class
    - def __init__(country : str , continent: str, capital: str)
    - def show_info( ) -> 국가 정보 + 해당 국가 시간 출력
        -	부모 클래스의 show_info()메소드를 상속 받아 재정의
    """
    def __init__(self, country : str, continent: str, capital: str):
        super().__init__(country, continent, capital)

    def show_info(self):
        current_time = datetime.now(pytz.timezone('{}/{}'.format(self.continent, self.capital)))
        super().show_info()
        print('Time: ', current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z\n'))

    """
    해당 국가 현재 시간 출력 예시
    # current_time = datetime.now(pytz.timezone('Asia/Tokyo')))
    # print('Time: ', current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z\n'))
    
    # 대륙,수도 찾기: ex. print(' '.join(pytz.country_timezones['nz'])) 
    # 'nz' -> 뉴질랜드 ISO 3116 국가 코드
    # ISO 3116: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes 
    """


###### do not edit here #######
Korea = Time("Korea","Asia","Seoul")
Spain = Time("Spain","Europe","Madrid")
Korea.show_info()
Spain.show_info()