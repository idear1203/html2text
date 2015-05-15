'''
    Created on Sep 19, 2014
    
    @author: liu.chunming
    '''
#!/usr/bin/env python
#coding=utf-8

import os
import html2text
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class ScanFile(object):
    def __init__(self,directory,prefix=None,postfix=None):
        self.directory=directory
        self.prefix=prefix
        self.postfix=postfix
    
    def scan_files(self):
        files_list=[]
        
        for dirpath,dirnames,filenames in os.walk(self.directory):
            '''
                dirpath is a string, the path to the directory.
                dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..').
                filenames is a list of the names of the non-directory files in dirpath.
                '''
            for special_file in filenames:
                if self.postfix:
                  if special_file.endswith(self.postfix):
                    files_list.append(os.path.join(dirpath,special_file))
                elif self.prefix:
                  if special_file.startswith(self.prefix):
                    files_list.append(os.path.join(dirpath,special_file))
                else:
                  files_list.append(os.path.join(dirpath,special_file))
    
        return files_list

    def scan_subdir(self):
        subdir_list=[]
        for dirpath,dirnames,files in os.walk(self.directory):
            subdir_list.append(dirpath)
        return subdir_list

if __name__=="__main__":
    #dir=r"/Users/wangdongwei/Documents/homework/machinelearning/html2txt/html2text4raw/test"
    #dir=r"/Users/wangdongwei/Documents/homework/machinelearning/html2txt/html2text4raw/test/index"
    #dir = r"/Users/wangdongwei/Documents/homework/machinelearning/homework/weps2007_data_1.1/traininig/web_pages/John_Kennedy/raw"
    dir = r"/Users/wangdongwei/Documents/homework/machinelearning/homework/weps2007_data_1.1/traininig/web_pages"
    scan=ScanFile(dir,postfix="index.html")
    #subdirs=scan.scan_subdir()
    files=scan.scan_files()
    
    '''
    print "The subdirs scaned are:"
    for subdir in subdirs:
        print subdir
        '''
    
    txt = ".txt"
    #print "The files scaned are:"
    for file in files:
        s = file
        pos = s.rfind(".")
        news = s[:pos] + txt
        if os.path.isfile(news) is False:
          print ('Processing ' + file)
          data = open(file, 'rb').read()
          encoding = None
          try:
            from chardet import detect
          except ImportError:
            detect = lambda x: {'encoding': 'utf-8'}
          encoding = detect(data)['encoding']
          if encoding is None:
            encoding = 'utf-8'
          data = data.decode(encoding, errors='ignore')
          h = html2text.HTML2Text(baseurl=file)
          h.ignore_links = True
          h.ignore_images = True
          pt =  h.handle(data)
          writefile = open(news, 'wb')
          writefile.write(pt)
          writefile.close()
        else :
          print ('Skip ' + file)
        #print news
