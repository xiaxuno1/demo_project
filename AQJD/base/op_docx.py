# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: create_test_report
# Author: xiaxu
# DATA: 2023/12/4
# Description:docx文档操作封装
# ---------------------------------------------------
from docx import Document


class Singleton:
    #单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance

class DOCXOP(Singleton):
    def __init__(self,path):
        """
        打开docx文件
        :param sheet_name: 数据表名
        """
        self.doc = Document(path)

    #替换关键字
    def replace_paragraphs_by_run(self,replace_keyword_dic):
        for p in self.doc.paragraphs:
            runs = p.runs
            #这里主要是runs会随意分割一段，导致关键字无法找到，因此合并组合，然后替换
            for i ,run in enumerate(runs):#记录关键字分割的位置，方便替换
                #print(run.text)
                if "#" in run.text: #关键字标记
                    count = i  #记录关键字起始位置
                    pre_partial = run.text[:run.text.find("#")]
                    tmp = run.text[run.text.find("#"):]  #找出关键字的部分，可能全，可能不全，可能超出
                    while tmp not in list(replace_keyword_dic.keys()):
                        count = count+1
                        if count+1>len(runs):  #超出段落分割数量，没有匹配到关键字，退出循环
                            #判断是否是第一次找到的关键字就超出真正关键字长度
                            unmatch_count = 0  #记录未匹配次数，判断是否满足条件
                            for key in replace_keyword_dic.keys():
                                if key in tmp:
                                    runs[i].text = runs[i].text.replace(runs[i].text,pre_partial+replace_keyword_dic[key]+
                                                                        tmp[tmp.find("key")+len(key)+1:]) #runs[i]= 前缀+关键字+后缀
                                    break
                                unmatch_count = unmatch_count+1
                            if unmatch_count>=len(replace_keyword_dic.keys()): #没有匹配到，提示
                                print("关键字没有在传入key找到，所在内容为：",tmp)
                            break
                        tmp = tmp+runs[count].text
                        runs[count].clear()  #这里有问题是如果关键字没有找到也会执行清空
                    if count+1<=len(runs):  #超过了分割数量还没有匹配上关键字，就替换
                        runs[i].text = runs[i].text.replace(runs[i].text,pre_partial+replace_keyword_dic[tmp])

    #通过段落替换，会丢失样式
    def replace_paragraphs(self,keyword,replace_keyword):
        for p in self.doc.paragraphs:
            if keyword in p.text:
                p.text = p.text.replace(keyword,replace_keyword)

    #指定内容填入表格
    def fill_in_table(self,table_index,content_list):
        # 读取指定表里面的数据
        table = self.doc.tables[table_index] #获取指定索引表格
        row = 0  #行号，从0开始
        for content in content_list[1:]: #不要表头
            table.add_row()  #增加单行
            row = row+1
            col = 0  # 列号，每新行从0开始
            for cell in content:
                table.cell(row,col).text = cell
                col = col + 1

    #在指定行列填写内容
    def fill_cell(self,table_index,loc,cell):
        table = self.doc.tables[table_index] #获取指定索引表格
        table.cell(loc[0],loc[1]).text = cell
        table.cell(loc[0],loc[1]).text = cell

    # 按照行遍历表内容
    def table_contents_row(self,table_index):
        """
        根据表索引，按照行的方式遍历，返回list
        :param table_index:
        :return: 行组成的list
        """
        contents = [] #全体内容
        table = self.doc.tables[table_index] #获取指定索引表格
        for row in table.rows:
            content = []  #行内容列表
            for cell in row.cells:
                content.append(cell.text)
            contents.append(content)
        return contents

    # 按照列遍历表内容
    def table_contents_col(self,table_index):
        """
        根据表索引，按照列的方式遍历，返回list
        :param table_index:
        :return: 行组成的list
        """
        contents = [] #全体内容
        table = self.doc.tables[table_index] #获取指定索引表格
        for col in table.cols:
            content = []  #列内容列表
            for cell in col.cells:
                content.append(cell.text)
        return contents

    # 打印docx内容
    def print_docx(self):
        for p in self.doc.paragraphs:
            for run in p.runs:
                print(run.text)

    # 保存新文件
    def save_docx(self,save_path):
        self.doc.save(save_path)


if __name__ == '__main__':
    #create_table()
    doc = DOCXOP("..\\data\\test_reporter.docx")
    doc.print_table(4)
    #doc.print_docx()
    doc.replace_paragraphs_by_run({"#时间段":"2023-11-28"})
    #doc.fill_cell(4,(3,1),"测试结论要附加方式放在这")
    doc.save_docx("..\\data\\修改时间段关键字.docx")
        # print(d)