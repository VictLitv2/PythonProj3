
from model.ScanInfo import ScanInfo
from scanner.Scanner import Scanner
from utils.ScanMetaDataStorage import ScanMetaDataStorage
from utils.ResultFormatter import ResultFormatter
from utils.InputProcessor import InputProcessor

def handle(host,port):
                
        scanner = Scanner(str(host),str(port))
        result = scanner.collect_scan_info()
        formatter = ResultFormatter(result).with_scan_meta_data(scan_meta_data)
        print(formatter.format())

if __name__ == "__main__":

    input_processor = InputProcessor()

    host_strs:list = input_processor.process_hosts()
    ports_strs:list = input_processor.process_ports()
    
    hosts_by_user = host_strs
   
    if len(ports_strs) == 2:
        ports_by_user = [x for x in range(int(ports_strs[0]),int(ports_strs[1])+1)]
    else:
        ports_by_user = ports_strs
   
    
    storage = ScanMetaDataStorage() 
    scan_meta_data = storage.process_meta_data()
    for host in hosts_by_user:
        for port in ports_by_user:
            handle(host,port)
            
            pass
        pass        
    
   