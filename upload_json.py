# 수동으로 수집한 데이터를 추가하기 위한 스크립트
from dotenv import load_dotenv
import os
import json
import mysql.connector
from datetime import datetime

# .env 파일 로드
load_dotenv()

# 데이터베이스 연결 설정
conn = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PW'),
    database=os.environ.get('DB_DB')
)
cursor = conn.cursor()

# JSON 경로 지정
folder_path = 'PassData/'

# 폴더 내 JSON 모든 JSON
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # 현재 시간을 사용하여 create_at 및 update_at 값을 설정
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            # SiteList 테이블에 데이터 삽입
            site_insert_query = """
            INSERT INTO `SiteList` (`siteName`, `Url`)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE `siteName` = VALUES(`siteName`), `Url` = VALUES(`Url`)
            """
            site_data = (data['siteName'], data['siteID'])
            cursor.execute(site_insert_query, site_data)
            
            # 삽입된 siteID 가져오기
            cursor.execute("SELECT `siteID` FROM `SiteList` WHERE `Url` = %s", (data['siteID'],))
            site_id = cursor.fetchone()
            if site_id is None:
                print(f"Error: Could not retrieve siteID for URL {data['siteID']}")
                continue
            site_id = site_id[0]
            
            # PassInformation 테이블에 데이터 삽입
            pass_insert_query = """
            INSERT INTO `PassInformation` 
            (`siteID`, `title`, `period`, `transportType`, `cityNames`, `create_at`, `update_at`, `imageURL`, `benefitInformation`, `reservationInformation`, `refundInformation`, `productDescription`, `stationNames`, `price`, `Map_Url`, `break_even_usage`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            pass_data = (
                site_id, data['title'], data['period'], data['transportType'], data['cityNames'], 
                now, now, data['imageURL'], data['benefitInformation'], data['reservationInformation'], 
                data['refundInformation'], data['productDescription'], data['stationNames'], 
                data['price'], data['Map_Url'], data['break_even_usage']
            )
            cursor.execute(pass_insert_query, pass_data)
            
            # CrawledPassData 테이블에 데이터 삽입
            crawled_insert_query = """
            INSERT INTO `CrawledPassData` 
            (`siteID`, `title`, `description`, `price`, `period`, `transportType`, `cityNames`, `create_at`, `imageURL`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            crawled_data = (
                site_id, data['title'], data['productDescription'], data['price_adult'], data['period'], 
                data['transportType'], data['cityNames'], now, data['imageURL']
            )
            cursor.execute(crawled_insert_query, crawled_data)
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            conn.rollback()

# 변경사항 커밋
conn.commit()
# 연결 종료
cursor.close()
conn.close()

print("데이터 삽입 완료")
