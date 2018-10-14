# -*- coding: utf-8 -*-
import xlwt


def write_excel(path, data):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('test_excel', cell_overwrite_ok=True)

    # 表头
    sheet.write(0, 0, 'key')  # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
    sheet.write(0, 1, 'value')

    # 具体写值
    count = 0
    for k, v in data.items():
        count += 1
        sheet.write(count, 0, k)
        sheet.write(count, 1, v)
    book.save(path)

def test_excel():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('test_excel', cell_overwrite_ok=True)
    sheet.write(0, 0, 'EnglishName')  # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
    sheet.write(0, 1, '中文名字')  # 此处需要将中文字符串解码成unicode码，否则会报错
    sheet.write(1, 0, 'Marcovaldo')
    sheet.write(1, 1, '马可瓦多')
    book.save(r'test1.xls')

if __name__ == '__main__':
    data = {'北京': 21, '上海': 23}
    write_excel(r'test3.xls', data)