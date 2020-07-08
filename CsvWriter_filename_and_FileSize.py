import os
import csv
import time

start_time = time.time()

# ________________________________________
# [parameters]
csv_file_path = r"D:\tmp\New folder\new"
event = "E20_07_05_08_53_47"
# ________________________________________

print " writing filenames and file size into csv ", csv_file_path
print "please wait..."

def insert_filenames_into_csv_1():

    """
    insert_filenames_into_csv
    :return:
    """
    start_fgc = 1
    end_fgc = 38
    csv_filename = csv_file_path + r"\summary_{}___fgc{}-{}.csv".format(event, start_fgc, end_fgc)

	
    with open(csv_filename, 'wb') as csv_file:
        fieldnames = ['path', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for fgc in range(start_fgc, end_fgc + 1):
            fgc_path = r'\\fgc{:02d}\d$\Events\{}\C{:02d}\H264'.format(fgc, event, fgc)
            file_path = os.listdir(fgc_path)
            for one_file_path in file_path:
                one_file = (os.path.join(fgc_path, one_file_path))
                head, tail = os.path.split(one_file)
                file_size = os.stat(one_file).st_size
                if one_file.endswith('.h264'):
                    writer.writerow({'path': tail, 'size': file_size})
                    #print(one_file, file_size)	
					            
	print("--- process took %s seconds ---" % (time.time() - start_time))
			
			
if __name__ == "__main__":
    insert_filenames_into_csv_1()

