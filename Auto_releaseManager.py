import os
import os.path
import sys
import glob
import time
import shutil
import webbrowser
import configparser
import pandas as pd
from tqdm import tqdm
from time import sleep
from pathlib import Path


# TODO: Add log instead of print, log to txt file


config_path = sys.argv[1]
if len(sys.argv) != 2:
    print("\nERROR: no config.ini was given \n"
          "Usage:\n"
          "  to run this program, copy to cmd the .py as the first argument\n"
          "  and the config.ini path as the second argument \n"
          "  example: \n"
          "     C:\Desktop\Auto_releaseManger C:\desktop\config.ini")
    sys.exit(1)


config = configparser.ConfigParser()
config.read(config_path)
base_folder_path = str(config["parameters"]["base_folder_path"])
Internal_Workdir_Path = str(config["parameters"]["Internal_Workdir_Path"])
delivered_Workdir_Path = str(config["parameters"]["delivered_Workdir_Path"])
Version_VIT_number = str(config["parameters"]["Version_VIT_number"])
Chrome_destination = str(config["parameters"]["Chrome_destination"])
dirname = str(config["parameters"]["dirname"])
gz_dirname = str(config["parameters"]["gz_dirname"])
MailAddress = str(config["parameters"]["MailAddress"])
checksum_exe_path = str(config["parameters"]["checksum_exe_path"])
Internal_bin_Path = str(config["parameters"]["Internal_bin_Path"])

# base_folder_path = r"\\dfs\mobileye\production\EyeQ5\Magna-Audi-MFK5"
# Internal_Workdir_Path = r"\\dfs\mobileye\production\EyeQ5\Magna-Audi-MFK5\X-ME-C-100\Internal\CAF\2021-10-05_X100.03\overlay\\"
# delivered_Workdir_Path = r"\\dfs\mobileye\production\EyeQ5\Magna-Audi-MFK5\X-ME-C-100\Delivered\Bin\Partial_Flashing"
# Version_VIT_number = 'MAGMFK5-1751'
# Chrome_destination = "C://Program Files//Google//Chrome//Application//chrome.exe"
# dirname = r"C:\PythonScriptTest\\"
# gz_dirname = r"C:\PythonScriptTest\\"


logFile = None
output_folder = None

splitted_Internal_Workdir_Path = (Internal_Workdir_Path.split("\\"))
version_folder_path = splitted_Internal_Workdir_Path[5]

internal_folder_path = splitted_Internal_Workdir_Path[6]
CAF_folder_path = splitted_Internal_Workdir_Path[7]
CAF_version_number_folder_path = splitted_Internal_Workdir_Path[8]
overlay_folder_path = splitted_Internal_Workdir_Path[9]

splitted_delivered_Workdir_Path = (delivered_Workdir_Path.split("\\"))
delivered_folder_path = splitted_delivered_Workdir_Path[6]
bin_folder_path = splitted_delivered_Workdir_Path[7]
partialFlashing_folder_path = splitted_delivered_Workdir_Path[8]


full_overlay_folder_path = os.path.join(base_folder_path, version_folder_path, internal_folder_path,
                                        CAF_folder_path, CAF_version_number_folder_path, overlay_folder_path)

full_partialFlashing_folder_path = os.path.join(base_folder_path, version_folder_path, delivered_folder_path,
                                                bin_folder_path, partialFlashing_folder_path)

full_bin_folder_path = os.path.join(base_folder_path, version_folder_path, delivered_folder_path, bin_folder_path)
full_delivered_folder_path = os.path.join(base_folder_path, version_folder_path, delivered_folder_path)

dbc_folder_path = os.path.join(full_delivered_folder_path, "dbc")
documents_folder_path = os.path.join(full_delivered_folder_path, "Documents")
ffs_folder_path = os.path.join(full_delivered_folder_path, "ffs")

xz_dirname = full_overlay_folder_path


def make_folder_tree():
    # os.makedirs('c:\mobileye\production\EyeQ5\Magna-Audi-MFK5\X-ME-C-100\Delivered\Bin\Partial_Flashing')
    # os.makedirs(r'c:\mobileye\production\EyeQ5\Magna-Audi-MFK5\X-ME-C-100\Internal\CAF\2021-10-05_X100.03\overlay')
    os.makedirs(r'c:\mobileye\production\EyeQ5\Magna-Audi-MFK5\X-ME-C-100\Internal\4QA/2021_10_12_15_08_MAGNA_SSNT-21_08-873_X-ME-C-100-MFK120_B100/Delivered/Bin')


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
    print(T_blue + "\n\t\t  Auto Release Manager Automation\t\t" + ENDC)
    time.sleep(0.1)
    print("\n")
    print("Please wait....")


def progress_bar():
    for i in tqdm(range(100)):
        sleep(0.001)


# TODO:
def copy_internal_bin_files():
    pass


def remove_low_vcc_files():

    for filename in glob.glob(os.path.join(dirname, "*low*.bin")):
        try:
            # Trying to remove a current file
            os.remove(os.path.join(dirname, filename))
            print("\n\nremoved all low vcc files from bin folder,",
                  "\n", "removed file:", dirname, filename)
        except EnvironmentError:
            # You don't have permission to do it
            pass
        print("removed all low vcc files from bin folder")


def rename_tar_gz_files():

    pattern = delivered_Workdir_Path + "*SSNT" + "*.gz"
    result = glob.glob(pattern)
    # Iterating the list with the count
    count = 1
    for file_name in result:
        splittedFileName = (file_name.split("_"))
        old_name = file_name
        new_name = delivered_Workdir_Path + splittedFileName[-1]
        try:
            os.rename(old_name, new_name)
            count = count + 1
            print("finished renaming tar.gz files (removing prefix)",
                  "\n", "original name:", old_name,
                  "\n", "new name:", new_name)
        except EnvironmentError:
            pass


def copy_CAFxz_file():

    pattern = full_overlay_folder_path + "\\" + "*.xz"
    result = (glob.glob(pattern))
    for file_name in result:
        try:
            shutil.copy(file_name, full_partialFlashing_folder_path)
            print("finished copying CAFxz_file to delivered",
                  "\n", "source path:", file_name,
                  "\n", "destination path:", full_partialFlashing_folder_path)
        except EnvironmentError:
            pass


# TODO:
def erase_grab():
    pass


def rename_CAFxz_file():

    pattern = full_partialFlashing_folder_path + "\\" + "*.xz"
    result = glob.glob(pattern)
    # Iterating the list with the count
    count = 1
    for file_name in result:
        splittedFileName = (file_name.split("_"))
        old_name = file_name
        new_name = full_partialFlashing_folder_path + "\\" + splittedFileName[-1]
        try:
            os.rename(old_name, new_name)
            count = count + 1
            print("finished renaming CAF.xz files (removing prefix)",
                  "\n", "original name:", old_name,
                  "\n", "new name:", new_name)
        except EnvironmentError:
            pass


# TODO:
def move_TAPI_bin_and_rename_to_Low_Res_image():
    pass


# TODO:
def rename_secure_bin():
    pass


def rename_bin_files():

    pattern = dirname + "*X-ME" + "*.bin"
    result = glob.glob(pattern)
    # Iterating the list with the count
    count = 1
    for file_name in result:
        splittedFileName = (file_name.split("_"))
        old_name = file_name
        new_name = dirname + splittedFileName[-1]
        try:
            os.rename(old_name, new_name)
            count = count + 1
            print("finished renaming bin files (removing prefix)",
                  "\n", "original name:", old_name,
                  "\n", "new name:", new_name)
            # printlog ( " does not exist! please check it .." , bcolors.RED, True)
        except EnvironmentError:
            pass


# TODO:
def move_json_to_documents_and_rename():
    pass


# TODO:
def copy_ffs_etc_files():
    pass


def validate_dbc_folder():
    number_of_dbc_files = (len([name for name in os.listdir(dbc_folder_path) if os.path.isfile(os.path.join(dbc_folder_path, name))]))
    print("Currently there are", number_of_dbc_files, "dbc files in dbc folder: ", dbc_folder_path)
    print("make sure dbc folder is full")
    # open dbc folder:
    os.startfile(dbc_folder_path)


def validate_documents_folder():

    number_of_document_files = (len([name for name in os.listdir(documents_folder_path) if os.path.isfile(os.path.join(documents_folder_path, name))]))
    print("Currently there are", number_of_document_files, "document files in documents folder: ", documents_folder_path)
    print("update all docs that need an update (mostly not needed) ")
    print("add Release Notes (should be in Sharepoint\ deliverables \ version)")    # open dbc folder:
    os.startfile(documents_folder_path)
    # open documents folder



def Calc_Hash_on_bins_With_CheckSum():

    print("\n Started Calculating Hash on Bins, this takes 2 minutes.")
    print("\n   Please Wait.................")
    full_cmd_line = (checksum_exe_path + ".exe" + " -d " + Internal_bin_Path + " -o " + checksum_exe_path)
    os.system(full_cmd_line)
    print("\nCalc_Hash_on_bins_With_CheckSum finished")

    print("\n Started Calculating Hash on Dev Folder, this takes 2 minutes.")
    print("\n   Please Wait.................")
    os.system(checksum_exe_path + ".exe" + " -d " + Internal_bin_Path + "\Dev" + " -o " + checksum_exe_path)
    print("\nCalc_Hash_on_bins_With_CheckSum finished")


# TODO:
def combine_hashed_text_to_one():
    pass


# TODO:
def copy_hashed_Text_output_to_delivered():
    pass


def zip_Delivered_folder():
    print("\n Started Zipping Delivered Folder, this takes 2 minutes.")
    print("\n   Please Wait.................")
    zipped_file_name = os.path.join(full_delivered_folder_path, version_folder_path )
    shutil.make_archive(zipped_file_name, 'zip', gz_dirname)
    print("\n zip delivered  finished!")


def create_mail():
    print("\n\ndelivery e-mail to Magna:")
    e_mail_subject = version_folder_path + " SW version for MFK5 has been uploaded to the collaboration platform"
    e_mail_Message = (version_folder_path, """
     SW Version for MFK5 has been uploaded to the collaboration platform:
    https://magna.sharepoint.com/:u:/r/teams/Electronics-EXT-Collab/Audi%20Collaboration/ama/KP03_ProductEngineering/40_Software/40_Release/20_Mobileye/{nameOfVersion}.zip
    Version information can be found under:  {nameOfVersion}.zip->Documents->{nameOfVersion}-Release notes.pdf
    Thanks in advance,
    Asaf Kaslassy""")
    # full_email_message = e_mail_Message.format(version_folder_path)
    print(e_mail_subject)
    print(e_mail_Message)

    df = pd.DataFrame([e_mail_Message])
    df.to_clipboard(index=False, header=False)
    return e_mail_Message, e_mail_subject


# TODO:
def emailer(e_mail_Message, e_mail_subject, recipient):
    import win32com.client as win32
    import os

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = e_mail_subject
    mail.HtmlBody = e_mail_Message
    attachment1 = os.getcwd() + "\\hash_output.ini"
    mail.Attachments.Add(attachment1)
    mail.Display(True)


def generate_Jira_comment():
    print("""\n\n
     Jira comment on""", Version_VIT_number, """VIT: 
     SW delivered to Magna,
     @Rachel Borochov \ @Shay Morag please finalize
     CC:@Yoel Fink
         """)
    url = 'https://jira.mobileye.com/browse/'
    full_url = url + Version_VIT_number
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(Chrome_destination))
    webbrowser.get('chrome').open_new(full_url)
    df = pd.DataFrame(["""SW delivered to Magna,
     @Rachel Borochov \ @Shay Morag please finalize
     
     CC:@Yoel Fink"""])
    df.to_clipboard(index=False, header=False)


def release_Jira_version():
    print(""" Go to releases in JIRA -> release """)
    url = 'https://jira.mobileye.com/projects/MAGMFK5?selectedItem=com.atlassian.jira.jira-projects-plugin:release-page&status=unreleased'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(Chrome_destination))
    webbrowser.get('chrome').open_new(url)


def main():
    global logFile
    global output_folder
    # make_folder_tree()
    # logFile = open("log_prepare.txt", 'w')
    # logFilePath = os.path.realpath("log_prepare.txt")
    # printer()
    # progress_bar()
    # remove_low_vcc_files()
    # rename_bin_files()
    # rename_tar_gz_files()
    # copy_CAFxz_file()
    # rename_CAFxz_file()
    # validate_dbc_folder()
    # validate_documents_folder()
    # Calc_Hash_on_bins_With_CheckSum()
    # zip_Delivered_folder()
    # create_mail()
    # emailer(MailInput, MailSubject, MailAddress )
    # generate_Jira_comment()
    # release_Jira_version()
    # logFile.close()
    # os.system("mv " + logFilePath + " " + output_folder + "/info/log.txt")


if __name__ == "__main__":
    main()

print("finished successfully")
