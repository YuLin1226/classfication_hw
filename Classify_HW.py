import os
import shutil
import zipfile


src_dirname = "C:\\Users\\Yulin\\Downloads"
des_dirname = "C:\\Users\\Yulin\\Desktop\\工程圖學109-1"

hw = input("Input the HW file:")
hw_dir = des_dirname + "\\" + hw
if not os.path.exists(hw_dir):
    os.makedirs(hw_dir)

        



list_hw = os.listdir(src_dirname)

for doc in list_hw:
    if "_b0" in doc:
        pos = doc.find('_b0')
        id_str = doc[pos+1:pos+10]
        # print("Student ID: %s"%id_str)
        src_doc = src_dirname + "\\" + doc
        des_dir = hw_dir + "\\"+ id_str

        if not os.path.exists(des_dir):
            os.makedirs(des_dir)

        shutil.move(src_doc, des_dir)

        zip_name = des_dir + "\\" + doc
        file_dir = des_dir 

        if ".zip" in doc:
            with zipfile.ZipFile(zip_name, 'r', compression=zipfile.ZIP_DEFLATED) as myzip:
                for file in myzip.namelist():
                    myzip.extract(file, file_dir)
        else:
            pass




