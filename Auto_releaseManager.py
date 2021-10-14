import os
import glob
import printlog
import webbrowser
import pandas as pd
import sys
import time
import kivy
import shutil
import subprocess
import configparser
from optparse import OptionParser
import simplejson


logFile = None
crc_path = None
output_folder = None
globalFailedIndicator = False;
fldrname = ""
version_info = {}
version_configuration = {}


class bcolors:
    RED        = '\033[91m'
    GREEN      = '\033[92m'
    YELLOW     = '\033[93m'
    BLUE       = '\033[94m'
    TOURQUOISE = '\033[96m'
    ENDC       = '\033[0m'


# TODO:
# TODO: add variable for CAF_Version and make xz_path irrelevant
# TODO: add variable for CAF_Version and make xz_path irrelevant
# TODO: add variable for CAF_Version and make xz_path irrelevant


base_folder_path = r"\\dfs\mobileye\production\EyeQ5\Magna-Audi-MFK5"
Internal_Workdir_Path = r"\\dfs\mobileye\production\EyeQ5\Magna-Audi-MFK5\X-ME-C-100\Internal\CAF\2021-10-05_X100.03\overlay\\"
delivered_Workdir_Path = r"\\dfs\mobileye\production\EyeQ5\Magna-Audi-MFK5\X-ME-C-100\Delivered\Bin\Partial_Flashing"
Version_VIT_number = 'MAGMFK5-1751'
Chrome_destination = "C://Program Files//Google//Chrome//Application//chrome.exe"

splitted_Internal_Workdir_Path = (Internal_Workdir_Path.split("\\"))
version_folder_path = splitted_Internal_Workdir_Path[7]
internal_folder_path = splitted_Internal_Workdir_Path[8]
CAF_folder_path = splitted_Internal_Workdir_Path[9]
CAF_version_number_folder_path = splitted_Internal_Workdir_Path[10]
overlay_folder_path = splitted_Internal_Workdir_Path[11]

splitted_delivered_Workdir_Path = (delivered_Workdir_Path.split("\\"))
delivered_folder_path = splitted_delivered_Workdir_Path[8]
bin_folder_path = splitted_delivered_Workdir_Path[9]
partialFlashing_folder_path = splitted_delivered_Workdir_Path[10]

full_overlay_folder_path = os.path.join(base_folder_path, version_folder_path, internal_folder_path,
                                        CAF_folder_path, CAF_version_number_folder_path, overlay_folder_path)

full_partialFlashing_folder_path = os.path.join(base_folder_path, version_folder_path, delivered_folder_path,
                                                bin_folder_path, partialFlashing_folder_path)

xz_dirname = full_overlay_folder_path
dirname = r"C:\PythonScriptTest\\"
gz_dirname = r"C:\PythonScriptTest\\"


def copy_internal_bin_files():
    pass


def copy_ffs_etc_files():
    pass


def remove_low_vcc_files():

    for filename in glob.glob(os.path.join(dirname, "*low*.bin")):
        try:
            # Trying to remove a current file
            os.remove(os.path.join(dirname, filename))
            print("removed all low vcc files from bin folder,",
                  "\n", "removed file:", dirname, filename)
        except EnvironmentError:
            # You don't have permission to do it
            pass
    print("removed all low vcc files from bin folder")


def rename_bin_files():

    pattern = dirname + "*X-ME" + "*.bin"
    result = glob.glob(pattern)
    # Iterating the list with the count
    count = 1
    for file_name in result:
        splittedFileName = (file_name.split("_"))
        old_name = file_name
        new_name = dirname + splittedFileName[-1] + str(count) + ".bin"
        try:
            # os.rename(old_name, new_name)
            count = count + 1
            print("finished renaming bin files (removing prefix)",
                  "\n", "original name:", old_name,
                  "\n", "new name:", new_name)
            # printlog ( " does not exist! please check it .." , bcolors.RED, True)


        except EnvironmentError:
            pass


def rename_tar_gz_files():

    pattern = gz_dirname + "*X-ME" + "*.gz"
    result = glob.glob(pattern)
    # Iterating the list with the count
    count = 1
    for file_name in result:
        splittedFileName = (file_name.split("_"))
        old_name = file_name
        new_name = gz_dirname + splittedFileName[-1] + str(count) + ".gz"
        try:
            # os.rename(old_name, new_name)
            count = count + 1
            print("finished renaming tar.gz files (removing prefix)",
                  "\n", "original name:", old_name,
                  "\n", "new name:", new_name)
        except EnvironmentError:
            pass


def copy_CAFxz_file():

    pattern = xz_dirname + "\\" + "*.xz"
    result = (glob.glob(pattern))
    for file_name in result:
        try:
            # shutil.copy(file_name, full_partialFlashing_folder_path)
            print("finished copying CAFxz_file to delivered",
                  "\n", "source path:", file_name,
                  "\n", "destination path:", full_partialFlashing_folder_path)
        except EnvironmentError:
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
            # os.rename(old_name, new_name)
            count = count + 1
            print("finished renaming CAF.xz files (removing prefix)",
                  "\n", "original name:", old_name,
                  "\n", "new name:", new_name)
        except EnvironmentError:
            pass


def Calc_Hash_on_bins_With_CheckSum():

    # start C:\CheckSum\Checksum_v3\Check_output_checksum.exe
    # - d \\dfs\mobileye\production\EyeQ5\[version_number]\Internal\4QA\[version_number\Delivered\Bin
    # - o C:\CheckSum\Checksum_v3

    print("\nCalc_Hash_on_bins_With_CheckSum finished")


def zip_Delivered_folder():

    # cd / mobileye / production / EyeQ5 / Magna - Audi - MFK5 / X - ME - C - 100 / Delivered /
    # zip - r X - ME - C - 100.zip *
    print("\nzip delivered  finished")


def create_mail():
    e_mail_Message = ("""
    Hi all,
    X-ME-{nameOfVersion} SW for MFK5 has been uploaded to the collaboration platform:
    https://magna.sharepoint.com/:u:/r/teams/Electronics-EXT-Collab/Audi%20Collaboration/ama/KP03_ProductEngineering/40_Software/40_Release/20_Mobileye/{nameOfVersion}.zip
    
    Version information can be found under:  {nameOfVersion}.zip->Documents->{nameOfVersion}-Release notes.pdf
    
    Thanks in advance,
    Asaf Kaslassy""")
    print("""\n\ndelivery e-mail to Magna:
    TO: [take from previous delivery e-mail]""", e_mail_Message)
    df = pd.DataFrame([e_mail_Message])
    df.to_clipboard(index=False, header=False)


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
    logFile = open("log_prepare.txt", 'w')
    logFilePath = os.path.realpath("log_prepare.txt")
    remove_low_vcc_files()
    rename_bin_files()
    rename_tar_gz_files()
    copy_CAFxz_file()
    rename_CAFxz_file()
    Calc_Hash_on_bins_With_CheckSum()
    zip_Delivered_folder()
    create_mail()
    generate_Jira_comment()
    release_Jira_version()

# logFile.close()
# os.system("mv " + logFilePath + " " + output_folder + "/info/log.txt")

if (__name__ == "__main__"):
    main()

print("finished successfully")
