#steps 
#1_Open the chat on whatsapp, export the chat via email or any file sharing method (which will be in .txt file) 
#2_Download that text file in your system 
#3_Copy the respective path for that file 


#python 3.7
import re
with open(r"C:\Users\Arther\Desktop\contentMafia/_chat.txt", "r", encoding="utf8") as file: 
           #here on above in double Quotation marks write the whole path for where the chats text file are being saved 

    chat_content = file.read()
    
    
link_regex = r"(http[s]?://\S+)"
links = re.findall(link_regex, chat_content)
output_file = open(r"C:\Users\Arther\Documents\links.txt", "w")
                    #here on above in double Quotation marks write the whole path for where the linkfile to be saved 
    
output_file.write('\n'.join(links))

output_file.close()

#after running this code find the file with name links or just navigate through the path you have given.