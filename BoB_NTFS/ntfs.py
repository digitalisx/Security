#!/usr/bin/python
#Reference : https://github.com/py4n6/pytsk/wiki/Development

import os
import sys
import datetime
import psutil
import pytsk3

top_area = '''
<!DOCTYPE html>
<html>
<head>
<title>HTML table demo</title>

<script src="./sorttable.js"></script>
<style>
/*Using CSS for table*/
.demotbl {
    border: 0px solid #69899F;
  }
.demotbl th{
    padding:15px;
    color:#fff;
    text-shadow:1px 1px 1px #568F23;
    border-bottom:3px solid #9ED929;
    background-color:#9DD929;
    background:-webkit-gradient(
        linear,
        left bottom,
        left top,
        color-stop(0.02, rgb(123,192,67)),
        color-stop(0.51, rgb(139,198,66)),
        color-stop(0.87, rgb(158,217,41))
        );
    background: -moz-linear-gradient(
        center bottom,
        rgb(123,192,67) 3%,
        rgb(139,198,66) 52%,
        rgb(158,217,41) 88%
        );
    -webkit-border-top-left-radius:5px;
    -webkit-border-top-right-radius:5px;
    -moz-border-radius:5px 5px 0px 0px;
    border-top-left-radius:5px;
    border-top-right-radius:5px;
  }
.demotbl td{
    width:100px;
    padding:10px;
    text-align:center;
    vertical-align: top;
    background-color:#DEF3CA;
    border: 1px solid #BED3AB;
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    border-radius:2px;
    color:#666;
    text-shadow:1px 1px 1px #fff;

  }

</style>
</head>
<body>
<p>KITRI BoB Stand Alone Parser v1.0</p>
<table class="demotbl sortable">
  <tr>
      <th>Number</th>
      <th>File Name</th>
      <th>Full Path</th>
      <th>M Time</th>
      <th>A Time</th>
      <th>C Time</th>
      <th>E Time</th>
  </tr>
'''

bottom_area = '''
</table>
</body>
</html>
'''

def directory_explorer(directory_object, parent_path ,top_area):

    count_num = 0

    for image_entry in directory_object:
        if image_entry.info.name.name in [".", ".."]:
            continue

        try:
            file_type = image_entry.info.name.type
            size = image_entry.info.meta.size

        except Exception as error:
            print "[!] No more files to read"
            exit()

        try:
            count_num += 1
            file_path = '%s/%s' % ('/'.join(parent_path),image_entry.info.name.name)

            if parent_path == []:
                full_path = '%s%s/%s' % (directory_path,'/'.join(parent_path),image_entry.info.name.name)#
                print "[-] file list in directory : " + str(full_path)

            else:
                full_path = '%s/%s/%s' % (directory_path,'/'.join(parent_path),image_entry.info.name.name)
                print "[-] file list in directory : " + str(full_path)

            # Convert name to file_path (/~/~/)

            modified_time = datetime.datetime.fromtimestamp(image_entry.info.meta.mtime)
            accessed_time = datetime.datetime.fromtimestamp(image_entry.info.meta.atime)
            created_time = datetime.datetime.fromtimestamp(image_entry.info.meta.crtime)
            edited_time = datetime.datetime.fromtimestamp(image_entry.info.meta.ctime)
            # Load original mace time

            cv_modified_time = modified_time.strftime('%Y/%m/%d %H:%M:%S (UTC/GMT +9:00)')
            cv_accessed_time = accessed_time.strftime('%Y/%m/%d %H:%M:%S (UTC/GMT +9:00)')
            cv_created_time = created_time.strftime('%Y/%m/%d %H:%M:%S (UTC/GMT +9:00)')
            cv_edited_time = edited_time.strftime('%Y/%m/%d %H:%M:%S (UTC/GMT +9:00)')
            # Convert mace time to adapt format (Timezone UTC)


            middle_area = '''
            <tr>
              <td>%s</td>
              <td><a href="%s">%s</a></td>
              <td>%s</td>
              <td>%s</td>
              <td>%s</td>
              <td>%s</td>
              <td>%s</td>
          </tr>
          '''%(count_num, full_path, file_path, full_path, cv_modified_time, cv_accessed_time, cv_created_time, cv_edited_time)
            top_area += middle_area

            if file_type == pytsk3.TSK_FS_NAME_TYPE_DIR:
                sub_directory = image_entry.as_directory()
                parent_path.append(image_entry.info.name.name)
                directory_explorer(sub_directory, parent_path, top_area)
                parent_path.pop(-1)

            elif file_type == pytsk3.TSK_FS_NAME_TYPE_REG and image_entry.info.meta.size != 0:
                offset = 0
                BUFF_SIZE = 1024 * 1024

                while offset < image_entry.info.meta.size:
                    available_to_read = min(BUFF_SIZE, image_entry.info.meta.size - offset)
                    file_data = image_entry.read_random(offset, available_to_read)
                    offset += len(file_data)

        except:
            continue

    return top_area

print "[!] KITRI BoB Stand Alone Parser v1.0"
directory_path = raw_input("[+] Put the name of the directory you want to explorer : ")
print "\n[+] Analyzing NTFS, Please waiting ...\n"

partition_list = psutil.disk_partitions()
#Load partiton_list

for partition in partition_list:
    #Input partition_list

      load_img = pytsk3.Img_Info('\\\\.\\'+partition.device.strip("\\"))
      #To load a file system via pytsk3

      if "NTFS" in partition.fstype:
          #Insfection NTFS Filesystem

        file_system = pytsk3.FS_Info(load_img)
        #To access a file system via pytsk3

        directory_object = file_system.open_dir(path=directory_path)

        top_area = directory_explorer(directory_object,[], top_area)

current_path = os.getcwd()

print "\n[!] Success create to HTML file in current directory (%s)" % (current_path)

f = open('viewer.html', 'w')
f.write(top_area + bottom_area)
f.close()
