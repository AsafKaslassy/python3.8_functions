
# logger
# ________________________________
logger = logging.getLogger('file_copy')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('file_copy.log')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO )
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)


# math
# ________________________________
def sumof(a,b):
  return a+b


def multiplyof(a,b):
  return a*b


def divide(a,b):
  return a/b


def differenceof(a,b):
  return a-b


class MathUtilsException(Exception):
  pass

import os
import logging
import shutil

# file_Copy
# ________________________________
def simple_files_copying(source,destination):
  """
  simple application that goes over all files
  in the current directory and copies all image files
  extension is 'jpg' or 'gif' or 'png') to a new subfolder,
  that its name is 'images'.
  """

  valid_extensions = [".jpg", ".jpeg", ".gif", ".png"]
  logger.info('valid_extensions = %s' % valid_extensions)
  logger.info('Source = %s' % source)
  logger.info('destination = %s' % destination)
  fileNames = os.listdir(source)
  for filename in fileNames:
    logger.info('\t %s' % filename)

  if not os.path.exists(destination):
    try:
      os.makedirs(destination+'\\images')
    except:
      raise OSError


  logger.info("Started copying")

  for file in fileNames:
    source_full_file_path = os.path.join(source, file)
    extension = os.path.splitext(file)[1]
    if extension.lower() in valid_extensions:
      logger.info("copying {}\{} to ---> {}\{}".format(source, file, destination, file))
      shutil.copy(source_full_file_path, destination)

    else:
      continue
  os.startfile(destination)
  logger.info('opening folder : %s' %destination)
  logger.info('finished successfully')
