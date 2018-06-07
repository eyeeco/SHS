from django.urls import reverse_lazy, reverse
from django.conf import settings
import os.path as osp

import pdfkit
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

'''
def MergePDF(filepath, filehead, outfile):
    output = PdfFileWriter()
    outputPages = 0
    # 加封皮
    input = PdfFileReader(open(filehead, "rb"))
    pageCount = input.getNumPages()
    outputPages += pageCount
    for iPage in range(0, pageCount):
        output.addPage(input.getPage(iPage))
    # 添加内容
    for each in filepath:
        # 读取源pdf文件
        pdf_path = osp.join(settings.MEDIA_ROOT, str(each.file_field))
        input = PdfFileReader(open(pdf_path, "rb"))
        # 获得源pdf文件中页面总数
        pageCount = input.getNumPages()
        outputPages += pageCount
        # 分别将page添加到输出output中
        for iPage in range(0, pageCount):
            output.addPage(input.getPage(iPage))
    # 最后写pdf文件
    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()
'''


def MergePDF(filepath, filehead, outfile):
    output = PdfFileMerger(strict=True)
    output.append(open(filehead, "rb"))
    for each in filepath:
        pdf_path = osp.join(settings.MEDIA_ROOT, str(each.file_field))
        output.append(open(pdf_path, "rb"))
    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()


def export_homework(request, homework, student):

    # 下载封面
    url_head = str(request.META.get('HTTP_HOST'))
    url_foot = reverse("tools:profile", args=(student.user_info.uid,))
    url = url_head + url_foot
    fname = '{}_cover.pdf'.format(student.user_info.id)
    save_path = osp.join(settings.TMP_FILES_ROOT, fname)
    pdfkit.from_url(url, save_path)

    # 拼接作业
    fname2 = '{}.pdf'.format(student.user_info.id)
    save_path_content = osp.join(settings.TMP_FILES_ROOT, fname2)
    MergePDF(homework, save_path, save_path_content)
    return save_path_content


def export_allhomework(request, temp, student):
    output = PdfFileWriter()
    outputPages = 0
    for stu in student:
        homework = stu.user_info.user.upload_set.all()
        url_path = export_homework(request, homework, stu)
        # 读取源pdf文件
        pdf_path = osp.join(url_path)
        input = PdfFileReader(open(pdf_path, "rb"))
        # 获得源pdf文件中页面总数
        pageCount = input.getNumPages()
        outputPages += pageCount
        # 分别将page添加到输出output中
        for iPage in range(0, pageCount):
            output.addPage(input.getPage(iPage))
    # 最后写pdf文件
    fname = 'all.pdf'
    save_path = osp.join(settings.TMP_FILES_ROOT, fname)
    outputStream = open(save_path, "wb")
    output.write(outputStream)
    outputStream.close()
    return save_path
