import os
import csv
import time


# ________________________________________
# [parameters]
csv_file_path = r'c:\tmp\New folder'  # csv output path
event = "E20_07_12_08_49_25"  # event to validate
start_fgc = 1
end_fgc = 6
# ________________________________________


start_time = time.time()
print("\n\n___H264 list to .CSV : filename_and_File Size__")
time.sleep(0.7)
print("\n")
print('Writing file names and file size into csv "{}":'.format(csv_file_path))
print("\n")
print("please wait........................................")



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
                    print('{}.... Not found,\n fgc might be down\n or has an empty folder'.format(fgc_path[0:37]))

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

        print("finished\n")
        print("--- process took %s seconds ---" % (time.time() - start_time))  # extract how much time the process took
        os.startfile(csv_file_path)  # open csv file to the screen for validation
        os.startfile(csv_filename)  # open output folder to the screen for validation


if __name__ == "__main__":
    insert_filenames_into_csv_1()
