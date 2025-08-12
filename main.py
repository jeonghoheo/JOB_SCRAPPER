# BLUEPRINT | DONT EDIT

from bs4 import BeautifulSoup
import requests

MAIN_URL = "https://berlinstartupjobs.com"
ENGINEERING_URL = f"{MAIN_URL}/engineering/"
SKILL_AREA_URL = f"{MAIN_URL}/skill-areas/"
SKILL_AREA_PYTHON_URL = f"{SKILL_AREA_URL}python/"
SKILL_AREA_JAVASCRIPT_URL = f"{SKILL_AREA_URL}javascript/"
SKILL_AREA_TYPESCRIPT_URL = f"{SKILL_AREA_URL}typescript/"

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:

# 헤더를 실제 브라우저의 것과 최대한 유사하게 추가해 줍니다.(봇으로 인식하는것을 방지하기위해)
# Add headers to mimic a real browser to prevent being blocked as a bot.
# Добавляем заголовки, максимально имитирующие реальный браузер 
# (чтобы избежать блокировки как бота).

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


def scrap_url(url, area):
    print("***************************")
    print(f"AREA: {area}")
    print(f"Scrapping {url}...")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all("li", class_="bjs-jlid")[0:-1]
    for job in jobs:
        job_title = job.find("h4", class_="bjs-jlid__h").text
        company_name = job.find("a", class_="bjs-jlid__b").text
        job_description = job.find("div", class_="bjs-jlid__description").text
        job_link = job.find("h4", class_="bjs-jlid__h").find("a").attrs.get("href")
        job_info = {
            "job_title":job_title,
            "company_name":company_name,
            "job_description":job_description,
            "job_ink":job_link
        }
        print("==============")
        print(f"JOB INFORMATION: {job_info}")    
        
def get_pages():
    response = requests.get(ENGINEERING_URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # 특정 태그로 정해져 있지 않을때 select로 특정 class명으로만 검색해서 해당 태그를 가져온다.
    # When the tag name isn't specific, use select with a class name pattern 
    # to get all matching tags.
    # Когда имя тега не указано точно, используем select с шаблоном имени класса 
    # для получения всех соответствующих тегов.
    buttons_len = len(soup.select('[class*="page-numbers"]'))
    return buttons_len - 1

for page in range(get_pages()):
    url = f"{ENGINEERING_URL}page/{page + 1}"
    scrap_url(url, "ENGINEERING_URL")

# 각 스킬별 직업들 목록을 스크랩
# Now, scrape jobs for specific skill areas
# Теперь собираем вакансии по конкретным областям навыков
# PYTHON
scrap_url(SKILL_AREA_PYTHON_URL, "SKILL_AREA_PYTHON_URL")
# JAVASCRIPT
scrap_url(SKILL_AREA_JAVASCRIPT_URL, "SKILL_AREA_JAVASCRIPT_URL")
# TYPESCRIPT
scrap_url(SKILL_AREA_TYPESCRIPT_URL, "SKILL_AREA_TYPESCRIPT_URL")

# /YOUR CODE