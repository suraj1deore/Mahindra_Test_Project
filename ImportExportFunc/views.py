from django.shortcuts import render
from .models import ImportData
from django.contrib import messages
from .forms import ImportDataResources
from tablib import Dataset
import xlsxwriter

def index(request):

# Data from the input file is stored in the backend
    try:
        if request.method == "POST":
            Importdataresources = ImportDataResources()
            dataset = Dataset()
            file_data = request.FILES["myfile"]

            if not file_data.name.endswith('xlsx'):
                messages.info(request, "The file format is incorrect, please use .xlsx file")
                return render(request, "index.html")
            import_data = dataset.load(file_data.read(), format = "xlsx")      
            for dataset in import_data:
                Value = ImportData()
                if dataset[0] == "Total":
                    print("Total: skipped")
                else:    
                    Value.category = dataset[0]
                    Value.X = dataset[1]
                    Value.Y = dataset[2]
                    Value.save()    

# To write backend data to this file, create an output file

            book = xlsxwriter.Workbook("ImportExportFunc/output/output.xlsx")
            format1 = book.add_format({'bg_color': "#FFFF00",'border':2,'bold':True})
            format2 = book.add_format({'border':1})
            format3 = book.add_format({'bg_color': "#00ADF2",'border':2,'bold':True})
            
            format1.set_align('center')
            format2.set_align('center')
            format3.set_align('center')

            sw = book.add_worksheet("sales")

            row_no = 0
            column  = ["Category", "X", "Y"]

            for column_num in range(len(column)):
                sw.write(row_no,column_num, column[column_num], format1)
            rows = ImportData.objects.filter(category="A").values_list("category","X","Y")
            for row in rows:
                row_no +=1
                for column_num in range(len(row)):
                    sw.write(row_no, column_num, row[column_num], format2)   
            row_no += 1    
            startrow = 1         
            sw.write(row_no, 0, ' Total', format3)
            cellno='B{}:B{}'.format(startrow, row_no)
            print(cellno)
            new_startrow= row_no
            cellno1 = 'C{}:C{}'.format(startrow, row_no)
            print(cellno1)
            sw.write(row_no,1, '=SUBTOTAL(9,'+ cellno +')', format3)
            sw.write(row_no,2, '=SUBTOTAL(9,'+ cellno1 +')', format3)

            row_no +=2           
            for column_num in range(len(column)):
                sw.write(row_no, column_num, column[column_num], format1)
            rows = ImportData.objects.filter(category="B").values_list("category","X","Y")
            for row in rows:
                row_no +=1
                for column_num in range(len(row)):
                    sw.write(row_no, column_num, row[column_num], format2)
            row_no += 1   
            new_startrow +=1 
            startrow = new_startrow        
            sw.write(row_no, 0, ' Total',format3)
            cellno='B{}:B{}'.format(startrow, row_no)
            print(cellno)
            new_startrow = row_no
            cellno1='C{}:C{}'.format(startrow, row_no)
            print(cellno1)
            sw.write(row_no, 1, '=SUBTOTAL(9,'+cellno+')', format3)
            sw.write(row_no, 2, '=SUBTOTAL(9,'+cellno1+')', format3)        

            row_no +=2        
            for column_num in range(len(column)):
                sw.write(row_no, column_num, column[column_num], format1)
            rows = ImportData.objects.filter(category="C").values_list("category", "X", "Y")
            for row in rows:
                row_no +=1
                for column_num in range(len(row)):
                    sw.write(row_no, column_num, row[column_num], format2)
            row_no += 1   
            new_startrow += 1 
            startrow = new_startrow        
            sw.write(row_no, 0, ' Total',format3)
            cellno='B{}:B{}'.format(startrow, row_no)
            print(cellno)
            new_startrow = row_no
            cellno1='C{}:C{}'.format(startrow, row_no)
            print(cellno1)
            sw.write(row_no,1, '=SUBTOTAL(9,'+ cellno +')', format3)
            sw.write(row_no,2, '=SUBTOTAL(9,'+ cellno1 +')', format3)        
            messages.success(request, 'The file has been uploaded successfully')                
            book.close() 

    except Exception as e:
        print(e)         

    return render(request, "base.html")
