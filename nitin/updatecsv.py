#CODE to update a CSV file

import os
import csv
from tempfile import NamedTemporaryFile
import shutil



def logfolder():
    path = os.getcwd()
    print(path)
    
    isDirectory = os.path.isdir(path)
    
    list_of_log_files_in_folder=[]
    #For listing all the files .log extension from the folder
    #Check if directory or folder exists or not
    if isDirectory != True :
        print("Directory doesnot exist")
        
    else:
        print("Directory_present")
        
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.log'):
                list_of_log_files_in_folder.append(file)
    return list_of_log_files_in_folder
    


#Function for creating CSV File template:
def csvFileCreation():

    header = ["Tables" ,"Schedule" ,"Start Time" ,"End Time" ,"Execution Time" ,"Execution Status" ,"Remarks"]
    
    rows_data = [["inview_clients"],["inview_managers"],["inview_holdings"],["inview_clients_delegated_link"]]
    
    
    with open('report.csv','w', newline='') as f:
        writer = csv.writer(f)
        
        #write the header
        writer.writerow(header)
        
        #writing the columns
        for data in rows_data :
            writer.writerow(data)
            

def search_multiple_strings_in_file(file_name,list_of_strings):
    
    list_of_results = []
    
    
    #Here I am opening the file many times.
    #Dont know how to open the file once and search at once all the keywords in a go
    #But the below code serves the purpose
    
    for string_to_search in list_of_strings:
        with open(file_name,'r') as read_obj :
            for line in read_obj :
                if string_to_search in line:
                    keyword = string_to_search
                    #String partitioning
                    keyword_before,keyword,keyword_after = line.partition(keyword)
                    list_of_results.append(keyword_after.strip())
                    
    return list_of_results
        

def updationOfCsv(all_files_data):
    filename = 'report.csv'
    tempfile = NamedTemporaryFile(mode='w+t',newline='' ,delete=False)
    
    fields = ['Tables','Schedule','Start Time','End Time','Execution Time','Execution Status','Remarks']
    
    with open(filename,'r',newline='') as csvfile,tempfile:
        reader = csv.DictReader(csvfile,fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        
        for row in reader:
            if row['Tables'] == 'Tables':
                writer.writerow(row)
            else:
                for list in all_files_data :
                    if row['Tables'] in list :
                        row['Schedule'],row['Start Time'] ,row['End Time'] ,row['Execution time'],row['Execution Status'] = list [1] ,list[2], list[3], list[4] , list[5]
                           
                    row = {'Tables' : row['Tables'] ,'Schedule' :row['Schedule'],'Start Time':row['Start Time'],
                            'End Time':row['End Time'] ,'Execution Time':row['Execution Time'] ,'Execution Status':row['Execution Status']}
                    writer.writerow(row)
                    
    shutil.move(tempfile.name, filename)



def main():
   list_of_files = logfolder()
   print(list_of_files)
   #Checking if there is any .log file present in the folder or not
   if list_of_files is None:
      sys.exit()
   
   else :
       list_of_strings_to_search = ["The table name is :","Scheduled Time :","Start Time :","End Time :","Execution_Time :","Job Status :"]
       
       os.chdir('C:/Users/Nitin Sharma/Desktop/coder/log_files')
       print(os.getcwd())
       all_files_data = []
       
       for file_name in list_of_files :
          print(file_name)
          #caling the function to search for the set of strings in the file
          
          result = search_multiple_strings_in_file(file_name,list_of_strings_to_search)
          all_files_data.append(result)
       
       #result after the pattern matched from the file
       print("The data in the list: ", all_files_data)
       
       #Creating the CSV according to existing template
       csvFileCreation()
       
       #Update the CSVCreated report.csv
       updationOfCsv(all_files_data)
   
        
   
   
   
   
   
if __name__== "__main__" :
    main()