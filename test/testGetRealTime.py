import controller.getRealTimeData as grd
import xlrd
import xlwt
if __name__ == '__main__':

    resultList = grd.parse(grd.get_real_time_data(['sz002307', 'sh600928']))
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('test')

    for i in range(len(resultList) ):

        for j in range(1 + len(resultList[i]['data'] )):
            if j== 0:worksheet.write(i,0,resultList[i]['id'])
            else:
                worksheet.write(i,j,resultList[i]['data'][j-1])
    workbook.save('excelwrite.xls')
