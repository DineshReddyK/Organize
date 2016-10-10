'''
Created on 05-Oct-2016

@author: Dinesh Reddy
'''

import os, sys
import shutil
from find_duplicate import check_for_duplicates

#import magic
#magic is not detecting mkv files & others correctly as video formats.

video_formats = ["3gp", "3g2", "asf", "amv", "avi", "divx", "drc", "flv", "flv", "flv", "f4v", "f4p", "f4a", "f4b", "gif", "m4v", "mxf", "mkv", "mpg", "mp2", "mpeg", "mpe", "mpv", "mpg", "mpeg", "m2v", "mp4", "m4p", "m4v", "mod", "mng", "mpeg", "mpg", "nsv", "ogv", "ogg", "mov", "qt", "yuv", "rm", "rmvb", "roq", "svi", "gifv", "vob", "webm", "wmv"]
audio_formats = ["aa", "aac", "aax", "act", "aiff", "amr", "ape", "au", "awb", "dct", "dss", "dvf", "flac", "gsm", "iklax", "ivs", "m4a", "m4b", "m4p", "mmf", "mp3", "mpc", "msv", "ogg", "oga", "mogg", "opus", "ra", "rm", "raw", "sln", "tta", "vox", "wav", "wma", "wv", "webm"]
image_formats = ["arw", "bmp", "cr2", "crw", "dcm", "dds", "djvu", "dmg", "dng", "exr", "fpx", "gif", "hdr", "icns", "ico", "ithmb", "jp2", "jpeg", "jpg", "nef", "nrw", "orf", "pcd", "pcx", "pict", "png", "psd", "sfw", "tga", "tif", "tiff", "wbmp", "webp", "xcf", "yuv"]
executable_formats = ["action", "apk", "app", "bat", "bin", "cmd", "com", "command", "cpl", "csh", "exe", "gadget", "inf1", "ins", "inx", "ipa", "isu", "job", "jse", "ksh", "lnk", "msc", "msi", "msp", "mst", "osx", "out", "paf", "pif", "prg", "ps1", "reg", "rgs", "run", "scr", "sct", "shb", "shs", "u3p", "vb", "vbe", "vbs", "vbscript", "workflow", "ws", "wsf", "wsh"]
spreadsheet_formats = [ "csv", "ods", "xls", "xlsb", "xlsm", "xlsx"]
presentation_formats = ["key", "odp", "pps", "ppsx", "ppt", "pptm", "pptx"]
documentation_formats = ["doc", "docm", "docx", "dot", "dotx"] 
doc_formats = ["chm", "eml", "hwp", "log", "m3u", "msg", "odt", "pages", "pdf", "pub", "rtf", "sxw", "tex", "txt", "wpd", "wps", "xml", "xps"]

videopath = ""
audiopath = ""
exepath = ""
docpath = ""
imgpath =""
others = ""
 
def create_dirs(basedir):
    global videopath, audiopath, exepath, docpath, imgpath, others
    
    videopath = os.path.join(basedir, "Video")
    audiopath = os.path.join(basedir, "Audio")
    exepath = os.path.join(basedir, "Executable")
    docpath = os.path.join(basedir, "Documents")
    imgpath = os.path.join(basedir, "Images")
    others = os.path.join(basedir, "Others")
    
    if not os.path.exists(videopath): os.mkdir(videopath)
    if not os.path.exists(audiopath): os.mkdir(audiopath)
    if not os.path.exists(exepath):   os.mkdir(exepath)
    if not os.path.exists(docpath):   os.mkdir(docpath)
    if not os.path.exists(imgpath):   os.mkdir(imgpath)
    if not os.path.exists(others):   os.mkdir(others)

def clean_empty_dirs():
    if not os.listdir(videopath): os.rmdir(videopath)
    if not os.listdir(audiopath): os.rmdir(audiopath)
    if not os.listdir(exepath): os.rmdir(exepath)
    if not os.listdir(docpath): os.rmdir(docpath)
    if not os.listdir(imgpath): os.rmdir(imgpath)
    if not os.listdir(others): os.rmdir(others)

def files(path):
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            yield f

def organize(main_dir):   
    for filename in files(main_dir):
        ext = filename.split('.')[-1].lower()
        if ext in video_formats:
            shutil.move(os.path.join(main_dir, filename), os.path.join(videopath, filename))
            
        elif ext in audio_formats:
            shutil.move(os.path.join(main_dir, filename), audiopath)
        
        elif ext in image_formats: 
            shutil.move(os.path.join(main_dir, filename), imgpath)
            
        elif ext in executable_formats:
            shutil.move(os.path.join(main_dir, filename), exepath)
            
        elif ext in spreadsheet_formats:
            shutil.move(os.path.join(main_dir, filename), docpath)
            
        elif ext in presentation_formats:
            shutil.move(os.path.join(main_dir, filename), docpath)
            
        elif ext in documentation_formats:
            shutil.move(os.path.join(main_dir, filename), docpath)
            
        elif ext in doc_formats:
            shutil.move(os.path.join(main_dir, filename), docpath)
        
        else:
            shutil.move(os.path.join(main_dir, filename), others)


if __name__ == '__main__':
    main_dir = raw_input("Directory to be organized: ") or "D:\My_Data\Others\test"    
    #recursive = raw_input("Should I do it recursively (Y|N)?: ")
    if not os.path.exists(main_dir):
        print ("Path does not exist.")
        sys.exit(1)
    
    create_dirs(main_dir)
    organize(main_dir)
    clean_empty_dirs()

    print "Organized ", main_dir
    print "Checking for duplicates: "
    check_for_duplicates(main_dir)
