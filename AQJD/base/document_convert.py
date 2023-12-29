# --------------------------------------------------
# coding=utf8
# Description:文档转换功能
# ---------------------------------------------------
from win32com import client
import os,time,docx2pdf

#两个方法耗时差不多
def docx2pdf_win32com(src_filename,dst_path = None):
    """
    将word文档转换为pdf,调用系统word，需要office支持
    :param src_filename:待转换的目标文档
    :param dst_filename: 转换后的文档保存地址
    :return: 成功1 ，失败-1
    """
    word = client.Dispatch("Word.Application")
    docx = word.Documents.Open(src_filename)
    path_file = os.path.split(src_filename)  #分离路径和文件
    file_name = os.path.splitext(path_file[-1]) #分离文件和后缀
    if dst_path == None:
        dst_path = path_file[0] #没有指定路径，默认放在同一目录
    docx.SaveAs("{}\\{}.pdf".format(dst_path,file_name[0]),17)  #17表示另存为pdf
    docx.Close()
    word.Quit()

def docx2pdf_docx2pdf(src_filename,dst_path = None):
    """
    将word文档转换为pdf,调用系统word，需要office支持
    :param src_filename:待转换的目标文档
    :param dst_filename: 转换后的文档保存地址
    :return: 成功1 ，失败-1
    """
    path_file = os.path.split(src_filename)  #分离路径和文件
    file_name = os.path.splitext(path_file[-1]) #分离文件和后缀
    if dst_path == None:
        dst_path = path_file[0] #没有指定路径，默认放在同一目录
    if file_name[1] == ".docx":
        docx2pdf.convert(src_filename,"{}\\{}.pdf".format(dst_path,file_name[0]))
    else:
        print("文件类型不是docx",file_name[1])

def excel2pdf(src_filename,dst_path = None):
    """
    excel转换为pdf
    :param src_filename:
    :param dst_path:
    :return:
    """
    try:
        xl = client.DispatchEx("Excel.Application")
        xl.Visible = False  #后台运行
        xl.DisplayAlerts = 0  #忽略报警
        path_file = os.path.split(src_filename)  #分离路径和文件
        file_name = os.path.splitext(path_file[-1]) #分离文件和后缀
        if dst_path == None:
            dst_path = path_file[0] #没有指定路径，默认放在同一目录
        workbooks = xl.Workbooks.Open(src_filename,False)
        workbooks.ExportAsFixedFormat(0,"{}\\{}.pdf".format(dst_path,file_name[0]))  #参数0表示转换为pdf
        workbooks.Close(False)
    except Exception as ec:
        print(ec)
    finally:
        xl.Quit()

if __name__ == '__main__':
    src_filename = "E:\\配置文件过程库\\10型以前车站\\10型增加安全监督\\输出配置文件\\AD\\Release" \
                   "\\测试报告\\埃岱-测试大纲.xlsx"
    dst_path = "E:\\配置文件过程库\\10型以前车站\\10型增加安全监督\\输出配置文件\\AD\\Release"
    t1 = time.perf_counter()
    #docx2pdf_win32com(src_filename)  #耗时4.445s
    #docx2pdf_docx2pdf(src_filename)   #耗时 4.59s
    excel2pdf(src_filename)
    t2 = time.perf_counter()
    print("耗时",t2-t1)

