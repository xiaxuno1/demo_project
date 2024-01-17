"""
配置文件测试报告批量修改需求：
1.修改日期、修改文档编号
2.修改文件的名称 国铁-JEC-金鹅池配置文件测试记录20to10V2.0.0.0.docx
3.转换为pdf
"""
from docx.oxml.ns import qn
from docx.shared import Pt

from AQJD.base.op_docx import DOCXOP
from AQJD.base.excel_op import ExcelOP
from AQJD.base.document_convert import docx2pdf_win32com
import time,os,shutil


class CFGTestReportModify:
    def __init__(self,file_path,sheet_name = "国铁2023"):
        self.cfg_infos=ExcelOP(file_path, sheet_name).get_rows() #获取配置文件信息

    #根据查找站码对应测试报告所在路径
    def get_file_path(self,cfg_path,station_code):
        for root,dirs,file_lists in os.walk(cfg_path):
            if root.endswith("配置文件制作"): #定位到配置文件制作下面
                if station_code in dirs:
                    #定位到测试报告所在位置
                    test_report_path = root[:-6]+"配置文件功能测试"
                    return test_report_path
        return False

    def modify_docx(self,file_path,cfg_info,tp=("20to10","V2.0.0.0")):
        doc = DOCXOP(file_path)
        if tp[1] == "V2.0.0.0":
            mad_date = str(cfg_info[9])
        elif tp[1] == "V3.0.0.0":
            mad_date = str(cfg_info[10])
        else:
            mad_date = str(cfg_info[10])
        date = mad_date[0:4]+"-"+mad_date[4:6]+"-"+mad_date[6:8] #制作日期
        num = cfg_info[8][-2:] #文档编号
        station = cfg_info[2]
        station_zh = cfg_info[1][cfg_info[1].find("线")+1:]
        version = tp[1]
        #修改模板信息
        if tp[0] =="20to10":
            doc.doc.paragraphs[0].text = "模板：WD/WP-RJ-09.1                          编号: WD/WP-RJ-09.1."+num
        elif tp[0] == "20to20":
            doc.doc.paragraph[0].text = "模板：WD/WP-RJ-07.2"
            doc.fill_cell(0,(1,3),"文档编号：WD/WP-RJ-07.2."+num)
        #修改页眉
        doc.page_header("2020型站机接入10中心配置文件测试报告")
        #修改测试报告名称
        doc.fill_cell(0,(0,0),"2020型站机接入10中心配置文件测试报告")
        #修改软件版本 20230801之前终端0100，之后终端0101
        contents1 = "站机V2.00.001.0100\n10中心：\n" \
                   "   应用服务器V1.02.000.0100\n" \
                   "   前置机V1.02.000.0100\n" \
                   "   网管服务器V1.02.000.0100\n" \
                   "   终端V1.02.002.0101\n" \
                   "   时钟服务器V2.07.174"
        contents2 = "站机V2.00.001.0100\n10中心：\n" \
                   "   应用服务器V1.02.000.0100\n" \
                   "   前置机V1.02.000.0100\n" \
                   "   网管服务器V1.02.000.0100\n" \
                   "   终端V1.02.002.0100\n" \
                   "   时钟服务器V2.07.174"
        if mad_date == "None" or int(mad_date)>=20230804:
            doc.fill_cell(0, (4, 1), contents1, aligned="LEFT")
        else:
            doc.fill_cell(0, (4, 1), contents2, aligned="LEFT")

        #修改配置版本
        doc.fill_cell(0, (5, 1), station  + "-" + version)
        #修改站名
        #获取第7行内容，并指定
        doc.fill_cell(0,(6,len(doc.table_content_row(0,6))-1), station_zh)
        #修改制作时间
        doc.fill_cell(0,(7,len(doc.table_content_row(0,7))-1), date)
        #检错提示
        if (doc.table_content_row(0,7)[1] == "杜波\n") or (doc.table_content_row(0,7)[1] == "杜波"):
            pass
        else:
            print(doc.table_content_row(0,7))
        if doc.table_content_row(0,8)[0] !="依据标准":
            print(doc.table_content_row(0,8))
        #重新生成 测试人等信息
        doc.create_test_data(0,(11,1),pic_path=[".\\data\\电子签名\\夏旭02.png",".\\data\\电子签名\\蒲国宇01.png",
                                                ".\\data\\电子签名\\邓永亮.png"],date=date)
        #导出为pdf
        save_path = os.path.split(file_path)[0] + "\\国铁-" + station + "-" + station_zh + "集中监测系统配置文件检验及测试报告" + tp[
                0] + version + ".docx"
        #print(save_path)
        #保存
        doc.save_docx(save_path)

def main(list_path,cfg_path):
    cfg =CFGTestReportModify(list_path)
    for cfg_info in cfg.cfg_infos[1:]:
        station_code = cfg_info[2]
        path = cfg.get_file_path(cfg_path, station_code) #测试文档的位置
        if path is not False:
            list_dir = os.listdir(path)
            modify_status = [0,0,0,0]  #记录是否修改的列表[20to10V2,20to10V3,20to20V2,20to20V3]

            for dir in list_dir:
                #批量修改生成测试报告
                if "测试报告20to10V2.0.0.0.docx" in dir:
                    if  dir.startswith("~$"): #排除word缓存文件
                        pass
                    else:
                        cfg.modify_docx(path+"\\"+dir,cfg_info,tp=("20to10","V2.0.0.0"))
                        docx2pdf_win32com(path+"\\"+dir)  #转换为pdf
                        modify_status[0]=modify_status[0]+1
                        time.sleep(2)
                elif "测试报告20to10V3.0.0.0.docx" in dir:
                    if  dir.startswith("~$"):
                        pass
                    else:
                        cfg.modify_docx(path+"\\"+dir,cfg_info,tp=("20to10","V3.0.0.0"))
                        docx2pdf_win32com(path+"\\"+dir) #转换为pdf
                        modify_status[1]=modify_status[1]+1
                        time.sleep(2)

            #导出到指定的位置
            for dir in list_dir:
                loc = "F:\\测试报告合集"
                if "测试报告20to10V2.0.0.0.pdf" in dir:
                    shutil.copy2(path+"\\"+dir,loc)
                    #modify_status[0] = modify_status[0] + 1
                elif "测试报告20to10V3.0.0.0.pdf" in dir:
                    shutil.copy2(path+"\\"+dir,loc)
                    #modify_status[1]=modify_status[1]+1

            print(path,modify_status)
        else:
            print("没有找到配置文件",cfg_info[1],cfg_info[2])

if __name__ == '__main__':
    list_path = "F:\\2020型车站配置\\CSM-WD-配置文件制作总清单-2023年.xlsx"
    cfg_path = "F:\\2020型车站配置"
    main(list_path,cfg_path)

