# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 14:23
# @Author  : Zcs
# @File    : out_excel.py

# 导入xlwt模块
import xlwt
import pymysql


#  该函数用于导出excel文件
def out_excel(row_list, columns_list, path):
    """
    :param row_list:excel中的列名
    :param columns_list:与列名相对应的dict的key
    :param path:excel文件保存路径
    exp：
    row_list = ['id', 'sid', '文件路径', '规则类型', '攻击类型', '备注', '告警信息', '处置建议', '优先级', '动作', '状态']
    columns_list = ['id', 'sid', 'file_path', 'rules_type', 'attack_type', 'msg', 'alarm_msg', 'advice', 'priority',
                    'actions', 'status']
    row_list 与 columns_list 一定要一一对应，顺序不能错
    :return: xxx.xls
    """
    config = {
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'cursorclass': pymysql.cursors.DictCursor,
        'charset': 'utf8',
        'db': 'test'
    }

    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM regular')
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    loops = len(data)
    # 创建一个Workbook对象，这就相当于创建了一个Excel文件
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # encoding参数让我们可以在excel中输出中文

    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
    # 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
    sheet = book.add_sheet('test', cell_overwrite_ok=True)
    # 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False
    # 向表test中添加数据

    # 设置表格边框
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN

    # 设置居中
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
    alignment.vert = xlwt.Alignment.VERT_TOP  # 垂直方向

    # 设置背景颜色
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 3  # 背景颜色

    # 创建样式
    style1 = xlwt.XFStyle()
    style1.borders = borders
    style1.alignment = alignment

    col_width = []
    # 将col_width全部初始化为9,9被用作后续判断，小于10的width都将使用excel单元格默认宽度
    for i in range(len(columns_list)):
        col_width.append(9)

    # 找到数据中每列宽度最大的值，用作设置单元格宽度
    for i in range(loops):
        j = 0
        for key in columns_list:
            if type(data[i][key]) == str:
                if len(data[i][key]) > col_width[j]:
                    col_width[j] = len(data[i][key])
                elif data[i][key].isupper():  # 如果字符串中英文全为大写,占位较多，初始化大一点的值
                    col_width[j] = 15
            j = j + 1
    print(col_width)

    # 根据col_width来设置每列单元格的宽度
    for i in range(len(col_width)):
        if col_width[i] > 10:
            sheet.col(i).width = 256 * (col_width[i] + 1)

    # 绘制列名
    x = 0
    for i in row_list:
        sheet.write(0, x, i, style1)  # 第一个参数为纵坐标，第二个参数是横坐标
        x = x + 1

    # 根据columns_list里面的字段来取从数据库取出的字典的值并插入到单元格中
    for i in range(1, loops+1):
        for j in range(len(columns_list)):
            sheet.write(i, j, data[i-1][columns_list[j]], style1)

    # 最后，将以上操作保存到指定的Excel文件中
    book.save(path)


if __name__ == '__main__':
    row_list = ['id', 'sid', '文件路径', '攻击类型', '备注', '告警信息', '处置建议', '优先级', '动作']
    columns_list = ['id', 'sid', 'file_path', 'attack_type', 'msg', 'alarm_msg', 'advice', 'priority',
                    'actions']
    out_excel(row_list, columns_list, r'C:\Users\admin-x\PycharmProjects\untitled\test1.xls')