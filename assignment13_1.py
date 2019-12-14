'''Design automation script which performs following task.
Accept Directory name from user and delete all duplicate files from the specified directory by
considering the checksum of files.
Create one Directory named as Marvellous and inside that directory create log file which
maintains all names of duplicate files which are deleted.
Name of that log file should contains the date and time at which that file gets created.
Accept duration in minutes from user and perform task of duplicate file removal after the specific
time interval.
Accept Mail id from user and send the attachment of the log file.
Mail body should contains statistics about the operation of duplicate file removal.
Mail body should contains below things :
Starting time of scanning
Total number of files scanned
Total number of duplicate files found
Consider below command line options for the gives script
DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
- DuplicateFileRemoval.py
Name of python automation script
- E:/Data/Demo
Absolute path of directory which may contains duplicate files
- 50
Time interval of script in minutes
- marvellousinfosystem@gmail.com
Mail ID of the receiver'''
import sys
import os
import schedule
import time
import mailcheck
import MailSender
import Conn
import MarvellousChecksum

def ProcessLog(ListofFile,scannfile_count,Starting_time,mailId,path="Marvellous"):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except:
            pass
    filename=os.path.join(path,"logfile%s.log"%(time.time()))
    D_count = 0
    
    line = "-"*80
    fobj = open(filename,'w')
        
    fobj.write(line+"\n")
    fobj.write("Marvellous names of duplicate files\n") 
    fobj.write(line+"\n")
    for outer in ListofFile:
        icnt = 0;
        for inner in outer:
            icnt+=1;
            if icnt >= 2:
                D_count+=1
                fobj.write(inner+"\n")
                os.remove(inner)
    
    #print("Total Duplicate files ",D_count);
    if D_count==0:
        str="NOt found duplicate file in Directory"
        fobj.write(str+"\n")
    T=time.ctime()
    fobj.write("\nProcessing time:"+T)
    fobj.close()
    MailSender.Send(filename,mailId,scannfile_count,D_count,Starting_time)
    
def DirectoryDusplicate(path,mailId):
    flag = os.path.isabs(path)
    if flag ==False:
        path=os.path.abspath(path)
        
    exists = os.path.isdir(path)
    data = {}
    scannfile_count=0
    if exists :
        Starting_time=time.time()
        for foldername,subfolder,filname in os.walk(path):

            for filen in filname:
                filen=os.path.join(foldername,filen)
                checksum=MarvellousChecksum.hashfile(filen)
                if checksum in data:
                    scannfile_count+=1;
                    data[checksum].append(filen)
                else:
                    scannfile_count+=1;
                    data[checksum] = [filen]

        newdata = []
        newdata = list(filter(lambda x: len(x)>1,data.values()))
        
        ProcessLog(newdata,scannfile_count,Starting_time,mailId)
        #MailSender.send(filename,sys.argv[2],scannfile_count,time)
        #print("total scannfile file=",scannfile_count)
        
    else:
        print("Invalid path ")


def main():
    print("Marvellous Infosystems : Python Automation and Machine Learing ")
    print("\n\t\t Application name:",sys.argv[0])
    
    
    if(len(sys.argv)<=2):

        if(len(sys.argv)==1):
            print("Error :invalid number of arguments")
            exit()
        if(sys.argv[1]=='-h') or(sys.argv[1]=='-H'):
            print("This script Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files.\
Create one Directory named as Marvellous and inside that directory create log file which maintains all names of duplicate files which are deleted.\
Name of that log file should contains the date and time at which that file gets created.\
Accept duration in minutes from user and perform task of duplicate file removal after the specific time interval.\
Accept Mail id from user and send the attachment of the log file.")
            exit()
        if(sys.argv[1]=='-u') or (sys.argv[1]=='-U'):
            print("Usage : DuplicateFileRemoval.py  E:/Data/Demo 50  marvellousinfosystem@gmail.com\n\
- DuplicateFileRemoval.py\n\
Name of python automation script\n\
- E:/Data/Demo\n\
Absolute path of directory which may contains duplicate files\n\
- 50\n\
Time interval of script in minutes\n\
- marvellousinfosystem@gmail.com\n\
Mail ID of the receiver")
            exit()
        else:
            print("Error :invalid number of arguments")
            exit()
    try:
        if mailcheck.check(sys.argv[2]):
            connected=Conn.is_connected()
            if connected:
                schedule.every(1).minute.do(DirectoryDusplicate,path=sys.argv[1],mailId=sys.argv[2])
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            else:
                print("Interent connection is not Found")
        else:
            print("Invalied email please enter the valied email")
    except ValueError:
            print("Error : Invalied datatype of input ")
    except Exception:
            print("Error : Invalid input ")
    finally:
            print("Thank You  !!!!!")
    
if __name__=="__main__":
    main()