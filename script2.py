import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from captcha_solver import solve
# import sqlite3

# conn = sqlite3.connect('signatures.db')


# s = requests.Session()


# import requests

# cookies = {
#     'dtCookie': '1$3C268066F689499D606B8589E4F353DD',
#     'nlbi_2043128': 'yEexWi81tC02HFabqtI6oAAAAAC7XG1fZ6zzeSHh3a2IqesN',
#     'PHPSESSID': 'im94nqo48865gg1f3c45d6m1c4',
#     'A10_Insert-20480': 'AJAFOJAKFAAA',
#     'incap_ses_466_2043128': '6xYPKrfyZRv803ApK5N3BjqFFF0AAAAALCbfhS/MVHArMdq5zXGgxg==',
#     'visid_incap_2043128': 'b/GX5d/WTyaoFZ2iZqWvWu2HE10AAAAAQ0IPAAAAAACAYiSNAYSmsTICDEezBdikdcta4D+o5vep',
# }

# headers = {
#     'Connection': 'keep-alive',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.38 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Referer': 'https://www.referendum.interieur.gouv.fr/consultation_publique/8/A/AA',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
#     'If-Modified-Since': 'Wed, 26 Jun 2019 09:02:35 GMT',
# }

# response = requests.get('https://www.referendum.interieur.gouv.fr/consultation_publique/8/A/AA', headers=headers, cookies=cookies)

# # print(response.content)

# html = BeautifulSoup(response.content, 'html.parser')

# # print(html)

# # Get form token
# token = html.select('#form__token')[0].attrs['value']
# print('Form token : {}'.format(token))


# cookies = {
#     'nlbi_2043128': 'yEexWi81tC02HFabqtI6oAAAAAC7XG1fZ6zzeSHh3a2IqesN',
#     'PHPSESSID': 'im94nqo48865gg1f3c45d6m1c4',
#     'A10_Insert-20480': 'AJAFOJAKFAAA',
#     'incap_ses_466_2043128': '6xYPKrfyZRv803ApK5N3BjqFFF0AAAAALCbfhS/MVHArMdq5zXGgxg==',
#     'visid_incap_2043128': 'b/GX5d/WTyaoFZ2iZqWvWu2HE10AAAAAQ0IPAAAAAACAYiSNAYSmsTICDEezBdikdcta4D+o5vep',
#     'rxVisitor': '1561627858362O8PN3MU6169DJ2S4ORR40UJJ726SNIGA',
#     'dtLatC': '2',
#     'dtPC': '1$428699333_204h-vCOEHOCBOLOLPCIMKHGENAAAKLCPGDCKO',
#     'rxvt': '1561630505420|1561627858372',
#     'dtSa': 'true%7CC%7C-1%7CValider%7C-%7C1561628709702%7C428699333_204%7Chttps%3A%2F%2Fwww.referendum.interieur.gouv.fr%2Fconsultation_5Fpublique%2F8%2FJ%2FJA%3Fpage%3D1%7CR%C3%A9f%C3%A9rendum%20d%27initiative%20partag%C3%A9e%7C1561628705421%7C',
#     'dtCookie': '1$3C268066F689499D606B8589E4F353DD|7b801f37abff0e14|1',
# }

# headers = {
#     'Connection': 'keep-alive',
#     'Cache-Control': 'max-age=0',
#     'Origin': 'https://www.referendum.interieur.gouv.fr',
#     'Upgrade-Insecure-Requests': '1',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.38 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Referer': 'https://www.referendum.interieur.gouv.fr/consultation_publique/8/J/JA?page=1',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
# }

# params = (
#     ('page', '1'),
# )

# data = {
#   'form[captcha]': '7beaylzl',
#   'form[_token]': 'IZLy6BRgEtsTkG0fGpWIfKzCDLbZdGRgt-ZCujgslpI'
# }

# response = requests.post('https://www.referendum.interieur.gouv.fr/consultation_publique/8/A/AA', headers=headers, params=params, cookies=cookies, data=data)


# html = BeautifulSoup(response.content, 'html.parser')

# print(html)



#############################################
# GET SECURITY IMAGE
#############################################
cookies = {
    'PHPSESSID': 'im94nqo48865gg1f3c45d6m1c4',
    'A10_Insert-20480': 'AJAFOJAKFAAA',
    'rxVisitor': '1561627858362O8PN3MU6169DJ2S4ORR40UJJ726SNIGA',
    'incap_ses_466_2043128': '28pLRlpMEEtDRIopK5N3BmWsFF0AAAAAnm6YVY+MKnLmx4ApsWMETw==',
    'visid_incap_2043128': 'b/GX5d/WTyaoFZ2iZqWvWu2HE10AAAAAREIPAAAAAACAHSWNAYSmsTIcD0fYqZaeNa1uJk5lZjKF',
    'nlbi_2043128': '5HtZFgs6MT9RXmNHqtI6oAAAAADIZ3I5xL6/2jAiWAtbyshx',
    'visid_incap_651915': '9UE3OI2KSz+Y4yaM6ytYP8C8FF0AAAAAQUIPAAAAAABVPzeX7xMx9010y8EpofS7',
    'incap_ses_729_651915': 'vL91akpUK2gO2jBfo+4dCsC8FF0AAAAA6EWj+bUpNbWVPM2YLK1iYw==',
    'dtLatC': '5',
    'dtPC': '1$440171000_386h-vCOEHODCPIAAONIMKHGFOBDOBKNPGDCKP',
    'rxvt': '1561641977082|1561634966881',
    'dtSa': 'true%7CC%7C-1%7CValider%7C-%7C1561640181302%7C440171000_386%7Chttps%3A%2F%2Fwww.referendum.interieur.gouv.fr%2Fconsultation_5Fpublique%2F8%2FA%2FAA%7CR%C3%A9f%C3%A9rendum%20d%27initiative%20partag%C3%A9e%7C1561640177083%7C',
    'dtCookie': '1$3C268066F689499D606B8589E4F353DD|7b801f37abff0e14|1',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://www.referendum.interieur.gouv.fr',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.38 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'https://www.referendum.interieur.gouv.fr/consultation_publique/8/A/AA',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
}



main_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for ml in main_letters:
    for sl in main_letters:
        url_data = ml + '/' + ml+sl
        page_number = 0
        still_pages = True
        while(still_pages):
            page_number += 1
            while(True):
                print('TRYING {} page {}...'.format(url_data, page_number))

                response = requests.get('https://www.referendum.interieur.gouv.fr/bundles/ripconsultation/securimage/securimage_show.php', headers=headers, cookies=cookies)

                with open("./captcha.png", 'wb') as f:
                    f.write(response.content)

                captcha_string = solve('./captcha.png')

                print(captcha_string)

                params = (
                    ('page', '{}'.format(page_number)),
                )

                data = {
                  'form[captcha]': captcha_string,
                  'form[_token]': '63Cr8KOGtdYZv-8b0J-StUhNMYpxxpMOjCjlQs3T-V8'
                }

                response = requests.post('https://www.referendum.interieur.gouv.fr/consultation_publique/8/{}'.format(url_data), headers=headers, params=params, cookies=cookies, data=data)
                html = BeautifulSoup(response.content, 'html.parser')
                fail = html.findAll("span", {"class": "help-block"})

                if len(fail) > 0:
                    print('Captcha failed, retrying')
                else:
                    # Detect if page found
                    panel_not_found = html.findAll("div", {"class": "panel-heading"})
                    if len(panel_not_found) > 0:
                        print('Page not found !')
                        print('Reseting page counter')
                        still_pages = False
                        break # break main while loop

                    table = html.find('table', attrs={'class':'table'})
                    table_body = table.find('tbody')

                    rows = table_body.find_all('tr')
                    for row in rows:
                        cols = row.find_all('td')
                        cols = [ele.text.strip() for ele in cols]
                        lastname = cols[0]
                        firstname = cols[1]
                        vote = cols[2]
                        with open('data.csv', 'a') as f:
                            f.write('{},{},{}\n'.format(lastname, firstname, vote))

                        print('{},{},{}\n'.format(lastname, firstname, vote))

                    break # Break main while loop







