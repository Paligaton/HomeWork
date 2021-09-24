from requests import get, utils
import datetime


def currency_rates(name_val):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    date = content[59:71]
    date_datetime = datetime.datetime.strptime(date, '"%d.%m.%Y"')
    val = content[content.find('<Value>', content.find(name_val)) + 7:content.find('</Value>', content.find(name_val))]
    val = format(round(float(val.replace(',', '.')), 2), '.2f')
    print(str(val) + ', ' + str(date_datetime.date()))