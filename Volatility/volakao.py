# Volatility Volakao plugin
#
# Copyright (C) 2015 Digitalis (https://www.facebook.com/digitalisx) 
#
# Thanks to MaJ3stY (saiwnsgud@naver.com)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details. 
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 

import os
import sys
import re
import volatility.utils as utils
import volatility.plugins.taskmods as taskmods

class Volakao(taskmods.MemDump):
    """Find User Info of KakaoTalk Windows version"""

    def __init__(self, config, *args, **kwargs):
        taskmods.MemDump.__init__(self, config, *args, **kwargs)

    def render_text(self, outfd, data):

        info_list = []

        print "\n====================================================="
        print "[!] Found Process & Analysis on Kakaotalk Memory Area"
        print "====================================================="
        print "\n[+] User Info"

        for pid, task, pagedata in data:
            
            task_space = task.get_process_address_space()
            
            if pagedata:
                
                for p in pagedata:
                    
                    data = task_space.read(p[0], p[1])
                    
                    if data == None:
                        
                        if self._config.verbose:
                            outfd.write("[!] Memory Not Accessible: Virtual Address: 0x{0:x} Size: 0x{1:x}\n".format(p[0], p[1]))
                    
                    else:
                        profile_string = re.search('("emailAddress.+?.[a-z]")|("formattedNsnNumber.+?.[1-z]")', data)
                        
                        if profile_string is None:
                            continue
                        
                        else:
                            info_list.append(profile_string.group())
                            
                        for info in info_list:

                            mail = re.search(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)",info)
                            
                            if not mail == None:
                                print "[-] User E-Mail : %s" % str(mail.group())
                                info_list = []

                            else:
                                phone_number = re.search(r"\d+-(\d+)-(\d+)", info)
                                print "[-] User Phone Number : %s" % str(phone_number.group())
                                info_list = []
        
        print "\n====================================================="
        print "[!] Analysis is finished"
        print "====================================================="
