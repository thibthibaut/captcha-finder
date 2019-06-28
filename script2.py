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



def is_captcha_valid(strung):
    valid = '123456789abcdefghijklmnprstuvwxyzABCDEFGHIJKLMNPRSTUVWXYZ'
    for c in strung:
        if not c in valid:
            return False
    return True

#############################################
# Header data
#############################################
cookies = {
    'PHPSESSID': 'im94nqo48865gg1f3c45d6m1c4',
    'rxVisitor': '1561627858362O8PN3MU6169DJ2S4ORR40UJJ726SNIGA',
    'incap_ses_466_2043128': '28pLRlpMEEtDRIopK5N3BmWsFF0AAAAAnm6YVY+MKnLmx4ApsWMETw==',
    'nlbi_2043128': '5HtZFgs6MT9RXmNHqtI6oAAAAADIZ3I5xL6/2jAiWAtbyshx',
    'visid_incap_651915': '9UE3OI2KSz+Y4yaM6ytYP8C8FF0AAAAAQUIPAAAAAABVPzeX7xMx9010y8EpofS7',
    'incap_ses_729_651915': 'vL91akpUK2gO2jBfo+4dCsC8FF0AAAAA6EWj+bUpNbWVPM2YLK1iYw==',
    'incap_ses_770_2043128': 'KWQeOVuv0FK2q6fYupevCvDRFF0AAAAANfZSxK0NESjM+MWpDD+Vsw==',
    'incap_ses_868_651915': 'TFctQoKaoVtRONjtNcILDCnMFV0AAAAA8TxHEzylW3bk508YjJx0VA==',
    'incap_ses_1177_651915': '8kVqdO/E8jv0eEvDkotVECrMFV0AAAAAdqYO1Y1LzVYV3INbQ61QrQ==',
    'incap_ses_764_2043128': '5HPEd1080CmkCdT8wkaaCu/xFV0AAAAAvWrQaOhByMnxPkQ5vyCTdA==',
    'A10_Insert-20480': 'ANAFOJAKFAAA',
    'visid_incap_2043128': 'b/GX5d/WTyaoFZ2iZqWvWu2HE10AAAAAR0IPAAAAAACAbiqNAU2IKsTh4ozTAGyPT814yL/xBFUj',
    'dtLatC': '3',
    'dtPC': '1$519296889_561h-vCOEHPBOAWOOIAIMKHHHSONAPMAPGDCLN',
    'rxvt': '1561721102989|1561718688624',
    'dtSa': 'true%7CC%7C-1%7CValider%7C-%7C1561719304473%7C519296889_561%7Chttps%3A%2F%2Fwww.referendum.interieur.gouv.fr%2Fconsultation_5Fpublique%2F8%2FT%2FTQ%7CR%C3%A9f%C3%A9rendum%20d%27initiative%20partag%C3%A9e%7C1561719302990%7C',
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
    'Referer': 'https://www.referendum.interieur.gouv.fr/consultation_publique/8/T/TQ',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
}


with open('last_cmd', 'r') as ff:
    main = ff.readline().strip()
    second = ff.readline().strip()
    page = int(ff.readline().strip())

print('Last stop: ')
print(main)
print(second)
print(page)

main_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
do_once1 = True
do_once2 = True

for ml in main_letters:
    if ml < main:
        print('Skipping {}'.format(ml))
        continue
    for sl in main_letters:
        if do_once1:
            if sl < second:
                print('Skipping {}/{}{}'.format(ml,ml,sl))
                continue
        do_once1 = False
        url_data = ml + '/' + ml+sl
        if do_once2:
            page_number = page
            do_once2 = False
        else:
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

                if not is_captcha_valid(captcha_string):
                    print('Invalid characters in captcha, retrying')
                    continue

                print(captcha_string)

                params = (
                    ('page', '{}'.format(page_number)),
                )

                data = {
                  'form[captcha]': captcha_string,
                  'form[_token]': 'm6QNLFA1YZNo6j0UGhoBpJDklht0090b_XIy3gFfKh4'
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

                    # Detect if aucun soutin
                    mess = html.find('h2')
                    if mess != None:
                        if 'Aucun soutien' in mess.text:
                            print('No signature detected !')
                            still_pages = False
                            break

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
                        with open('last_cmd', 'w') as ff:
                            ff.write('{}\n{}\n{}\n'.format(ml, sl, page_number))

                    break # Break main while loop







