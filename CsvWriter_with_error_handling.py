import os
import csv
import time
import sys


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# [parameters]
csv_file_path = r'c:\tmp\New folder'  # csv output path
event = "E20_07_12_08_49_25"  # event to validate
start_fgc = 1
end_fgc = 6
# █████████████████████████████████████████████████████ #


def printer():
    """

    :return:
    """
    global T_GREEN , T_blue, T_red, T_underline, ENDC, start_time

    T_GREEN = '\033[32;1m'  # green text
    T_blue = '\033[34;4m'  # blue text
    T_red = '\033[91m'  # blue text
    T_underline = '\033[34;4m'  # underline text
    ENDC = '\033[m'

    start_time = time.time()
    print(T_blue + "\n\t\tH264 list to .CSV : filename_and_File Size\t\t" + ENDC)
    time.sleep(0.7)
    print("\n")
    print("Please wait....")
    print('Writing file names and file size to csv:' + T_underline + '"' + csv_file_path + '"' + ENDC)


def progress_bar():
    """

    :return:
    """
    sys.stdout.write(T_GREEN + "Progress Bar\n" + ENDC)
    toolbar_width = 20
    sys.stdout.write("| %s" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.1)
        sys.stdout.write(T_GREEN +"██" + ENDC)
        sys.stdout.flush()
    sys.stdout.write(T_GREEN + "|     100% done \n\n" + ENDC)
    time.sleep(0.7)


def insert_filenames_into_csv_1():
    """
    insert_filenames_into_csv
    :output: csv file filled with filename and size data
    """
    csv_filename = csv_file_path + r"\summary_{}__fgc{}-{}.csv".format(event, start_fgc, end_fgc)
    if not os.path.exists(csv_file_path):
        os.makedirs(csv_file_path)
    with open(csv_filename, 'a') as csv_file:  # open csv for writing
        fieldnames = ['path', 'size']  # write csv headers
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for fgc in range(start_fgc, end_fgc + 1):  # run loop on fgcs
            # path to h264 folder in each fgc
            fgc_path = r'c:\fgc{:02d}\d\Events\{}\C{:02d}\H264'.format(fgc, event, fgc)
            if not os.path.exists(fgc_path):
                try:
                    print(T_underline + '"' + fgc_path[0:37] + '...."' + ENDC
                          + T_red + ' Not found, fgc might be down, or has an empty folder' + ENDC)

                except Exception as error:
                    print(error)
                continue
            file_path = os.listdir(fgc_path)
            for one_file_path in file_path:
                one_file = (os.path.join(fgc_path, one_file_path))
                head, tail = os.path.split(one_file)  # split path to filename only
                file_size = os.stat(one_file).st_size  # find file size
                if one_file.endswith('.ini'):  # filter files that end with specific extension
                    writer.writerow({'path': tail, 'size': file_size})  # fill csv file with data

        print(T_GREEN + "\nFinished Successfully \n\n" + ENDC)
        print("\t--- process took %s seconds ---" % (time.time() - start_time))  # extract how much time the process took
        test_passed =\
            """
        
         /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$$       /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$                                                                                                                                                                   
        |__  $$__/| $$_____/ /$$__  $$|__  $$__/      | $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$_____/| $$__  $$                                                                                                                                                                  
           | $$   | $$      | $$  \__/   | $$         | $$  \ $$| $$  \ $$| $$  \__/| $$  \__/| $$      | $$  \ $$                                                                                                                                                                  
           | $$   | $$$$$   |  $$$$$$    | $$         | $$$$$$$/| $$$$$$$$|  $$$$$$ |  $$$$$$ | $$$$$   | $$  | $$                                                                                                                                                                  
           | $$   | $$__/    \____  $$   | $$         | $$____/ | $$__  $$ \____  $$ \____  $$| $$__/   | $$  | $$                                                                                                                                                                  
           | $$   | $$       /$$  \ $$   | $$         | $$      | $$  | $$ /$$  \ $$ /$$  \ $$| $$      | $$  | $$                                                                                                                                                                  
           | $$   | $$$$$$$$|  $$$$$$/   | $$         | $$      | $$  | $$|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$$$$$$/                                                                                                                                                                  
           |__/   |________/ \______/    |__/         |__/      |__/  |__/ \______/  \______/ |________/|_______/                                                                                                                                                                   
                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                    
               ▐▒▒░▄                                                                                                                                                                                                                                                                
               ▒▒▒▒▒▒▒▒▄                                                                                                                                                                                                                                                            
               ▐▒▒▒▒▒▒▒▒▒▒▒▄                                                                         ▄▄▒▒                                                                                                                                                                           
                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▄                                                               ▄▄▒▒▒▒▒▒▒▒                                                                                                                                                                           
                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄                                                       ▄▒▒▒▒▒▒▒▒▒▒▒▒▒▌                                                                                                                                                                           
                 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄                                               ▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                            
                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                        ▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░                                                                                                                                                                            
                   ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄                                ▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                             
                     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                              
                      ▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀                                                                                                                                                                               
                        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                 
                          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                   
                            ▀▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀                                                                                                                                                                                     
                               ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▀                                                                                                                                                                                        
                             ▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░                                                                                                                                                                                           
                             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                          
                            ▒▒▒▒▒▒▒▒▒▒░▄▄▄  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▄▄▄  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                         
                           ▒▒▒▒▒▒▒▒▒▒▒ ▀█▀   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▐██▀   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░                                                                                                                                                                                        
                          ▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                        
                         ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▄   ▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄   ▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                       
                         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                       
                        ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄  ▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                      
                        ▒▒░░░░░░░░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░▒▒▒▒▒▒▒▒                                                                                                                                                                                     
                       ▐▒░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▐▒▒▒▒▒▒                                                                                                                                                                                     
                       ▒▒░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀░░░░▄░░░▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▐▒▒▒▒▒▒▒                                                                                                                                                                                    
                       ▐▒▒░░░░░░░▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░▒▒▒▒▒▒▒▒                                                                                                                                                                                    
                        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒▒░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                   
                        ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                   
                         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄░▀▒▒▒▒▀░▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                  
                          ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                                                                                                                  
                           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░
        
        """
        time.sleep(1.7)
        print(T_GREEN + test_passed + ENDC)

        # os.startfile(csv_file_path)  # open csv file to the screen for validation
        # os.startfile(csv_filename)  # open output folder to the screen for validation


if __name__ == "__main__":
    printer()
    progress_bar()
    insert_filenames_into_csv_1()
