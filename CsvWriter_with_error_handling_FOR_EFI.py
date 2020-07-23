import csv
import os
import sys
import time
import configparser


config_path = sys.argv[1]
if len(sys.argv) != 2:
    print("\nERROR: no config.ini was given \n"
          "Usage:\n"
          "  to run this program, copy to cmd the .exe as the first argument\n"
          "  and the config.ini path as the second argument \n"
          "  example: \n"
          "     d:\work\CsvWriter.exe d:\work\config.ini")
    sys.exit(1)


config = configparser.RawConfigParser()
config.read(config_path)
start_fgc = int(config["parameters"]["start_fgc"])
end_fgc = int(config["parameters"]["end_fgc"])
csv_file_path = config["parameters"]["csv_file_path"]
event = config["parameters"]["event"]                    # event to validate
file_extension = config["parameters"]["file_extension"]  # '.h264'
mode = str(config["parameters"]["mode"])
server = config["parameters"]["server"]
drive = config["parameters"]["drive"]
team_name = config["parameters"]["team_name"]


def printer():
    """

    :return:
    """
    global T_GREEN, T_blue, T_red, T_underline, ENDC, start_time

    T_GREEN = ' '  # green text
    T_blue = ' '  # blue text
    T_red = ' '  # red text
    T_underline = ' '  # underline text
    ENDC = ' '

    start_time = time.time()
    print(T_blue + "\n\t\t  H264 list to .CSV : filename_and_File Size\t\t" + ENDC)
    time.sleep(0.5)
    print("\n")
    print("Please wait....")
    print('Writing file names and file size to csv:' + T_underline + '"' + csv_file_path + '"' + ENDC)


def progress_bar():
    """

    :return:
    """
    sys.stdout.write(T_GREEN + "\t\tProgress Bar\n" + ENDC)
    toolbar_width = 10
    sys.stdout.write("| %s" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))

    for i in range(toolbar_width):
        time.sleep(0.1)
        sys.stdout.write("--")
        sys.stdout.flush()
    sys.stdout.write(T_GREEN + "|     100% done \n\n" + ENDC)
    time.sleep(0.7)


def insert_filenames_into_csv():
    """
    insert_filenames_into_csv
    :output: csv file filled with filename and size data
    """
    csv_filename = csv_file_path + r"\summary_{}__fgc{}-{}.csv".format(event, start_fgc, end_fgc)
    if not os.path.exists(csv_file_path):
        os.makedirs(csv_file_path)
    # with open(csv_filename, 'wb') as csv_file:  # open csv for writing
    with open(csv_filename, 'a', newline='') as csv_file:  # open csv for writing
        fieldnames = ['path', 'size']  # write csv headers
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for fgc in range(start_fgc, end_fgc + 1):  # run loop on fgcs
            # path to h264 folder in each fgc
            cases = {
                'from_fgc': r'\\fgc{:02d}\d$\Events\{}\C{:02d}\H264'.format(fgc, event, fgc),
                'debug': r'c:\\fgc{:02d}\d\Events\{}\C{:02d}\H264'.format(fgc, event, fgc),
                'event_from_backup_path': r'\\{}\{}$\FreeD Backup\{}\{}\fgc{:02d}\C{:02d}\H264'.format(
                                            server, drive, team_name, event, fgc, fgc)
            }
            search_path = cases.get(mode, 'from_fgc')
            # print(search_path)
            if not os.path.exists(search_path):
                try:
                    print(T_red + search_path + "  - Not found ! fgc might be down, or has an empty folder" + ENDC)
                except Exception as error:
                    print(error)
                continue
            else:
                pass

            file_path = os.listdir(search_path)
            for one_file_path in file_path:
                one_file = (os.path.join(search_path, one_file_path))
                head, tail = os.path.split(one_file)  # split path to filename only
                file_size = os.stat(one_file).st_size  # find file size
                if one_file.endswith(file_extension):  # filter files that end with specific extension
                    writer.writerow({'path': tail, 'size': file_size})  # fill csv file with data

        print(T_GREEN + " \n  Process Finished Successfully \n " + ENDC)
        print("\t--- process took %d seconds ---" % (time.time() - start_time))

        os.startfile(csv_file_path)  # open csv file to the screen for validation
        # os.startfile(csv_filename)  # open output folder to the screen for validation


if __name__ == "__main__":

    printer()
    progress_bar()
    insert_filenames_into_csv()
