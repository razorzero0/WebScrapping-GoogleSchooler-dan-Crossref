
from bs4 import BeautifulSoup
import requests

header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "cookie":"__Secure-ENID=6.SE=O1PW_VwGrLKJkDhBVGQlBDZ0UE4XXe9vzbyUBdtiJaF05nWAEm_fT7o055udEmhCWTppB6c1wMDiSccMlWoaSPoOouBesTsacbk0moSUkPmHMRm5UpBS24We0QcmJ22_J0TbDSaZPL3qlOWgsZZ2og9213n1a6vTSYV8I79RoW1fa6Je7hShfD4ywAQZW_lLwEsa963W3tct07Lq6ax8rI57Mafbuj2Hl_8WZHZNu-SzRSrbL-kBHGv1; HSID=ARwAd36SdGhNGo8yL; SSID=AocdnXNhGxoxwN2Yo; APISID=YONvxNoSZtWKuEcc/ADAf5JOCPO_5uxVqj; SAPISID=9yWF54ZoztZoYsnq/ALQjhOmV-7_doE_u3; __Secure-1PAPISID=9yWF54ZoztZoYsnq/ALQjhOmV-7_doE_u3; __Secure-3PAPISID=9yWF54ZoztZoYsnq/ALQjhOmV-7_doE_u3; GSP=LM=1670155768:S=d5UYC-SJOIdUX4oO; SID=SQjYObDNjWqpt60uXEsWbgk3BbgK-VgM9QOdAcEKhsiEcz_nuifDZPYgKEzdck34W5XQ8g.; __Secure-1PSID=SQjYObDNjWqpt60uXEsWbgk3BbgK-VgM9QOdAcEKhsiEcz_nreOvos-d6kCR6LcXIVHWWg.; __Secure-3PSID=SQjYObDNjWqpt60uXEsWbgk3BbgK-VgM9QOdAcEKhsiEcz_nxfC2McOq0Z-w_LYc3l-nKw.; SEARCH_SAMESITE=CgQIsZcB; OGPC=19022622-1:; 1P_JAR=2023-01-31-10; AEC=ARSKqsLIObTO6bRDHRtB_M9uRqVGLWx-MaXt-tsLcm4cFKBDzYsDaP6GEA; NID=511=enGdCNghBhIIYiDlRBS02X4J0_NjjpSlnrWP-A5NW_Hs9rycf32-vEZnLyi-YQI_zmecUSmXxOBkwXRhVFNztmaA8cnrRkLad-A_5IdnHmw1tij8lQhMC1vc8BmPHTVgsIPVphCwL2EAPSh9ytPqsPtoQYrzUoWKebycAFWJEsJR1icJ-21O_b9xJhbcL84ItiN3y3sxf3FDvc6jLV0e7SOGzHnG9BoYfc3Xl26MSDvUUHbfewRMcv3yqeZwZ3XIc0I1t0e3Iu-8OOgnH5gD11vmBOeAUw5os3vMt9XroqUqxlRy4_w9gcmkFhDH5EyIRtQv1uYcDTqkIVZB3Zy6Ct0B; SIDCC=AFvIBn_FVG3i1yYQy5RYOIAYK_v5_4-WWmzFq7ZaDAuynLP6fduhJYCjj4veTn22nRqcWnVjYtir; __Secure-1PSIDCC=AFvIBn9JT4YAuj2w-PiXaJJlw6cQ4Y5weyUU3sjuPJUFWVRgWo8CYrEbii0VRO--xb3IWVwTYTc; __Secure-3PSIDCC=AFvIBn8jNcw1pYefwaQv5iQzXFamYGeXLz_vxZIeVy9D4YUkLr1_i7nTTH9dluKaahGWu9Dkw3p8"
}

url = "https://scholar.google.com/scholar?hl=id&as_sdt=0%2C5&q=web+indo&btnG="
req = requests.get(url,headers=header)
soup = BeautifulSoup(req.text, 'html.parser')
items = soup.find("div", {"id": "gs_res_ccl_mid"})
for i in items.findAll("h3"):
    print(i.text)
    name = i.find('a',href=True)
    print(name['href'])


 

 