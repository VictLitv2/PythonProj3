import nmap,os 
from model.ScanInfo import ScanInfo
class Scanner:
    def __init__(self,host_str,port_str) -> None:
        self.host_str = host_str
        self.port_str = port_str
        self.proto = "tcp"
        pass
    
    def collect_scan_info(self)->ScanInfo:
        nm = nmap.PortScanner()
        host = self.host_str
        port = self.port_str
        

        try:
            details:dict = self.__process_details(nm)
            return ScanInfo(details)
        except Exception as err:
            print (f"Error:{err}")    

        return None
    

    def __process_details(self,nm) ->dict:
        
            details = dict()
            scan_result = nm.scan(self.host_str, self.port_str)            
            all_hosts = nm.all_hosts()
            ip_addr = all_hosts[0]
            
            details["user_host"] = self.host_str
            details["user_port"] = self.port_str

            details["ip_address"] = ip_addr

            details["host"] = nm[ip_addr]['hostnames']
            
            details["ip_status"] = nm[ip_addr].state()
                        
            open_ports_dic:dict = nm[ip_addr][self.proto]
            
            
            details["port_status"] = open_ports_dic[int(self.port_str)]["state"]
            details["service_name"] = f"{nm[ip_addr][self.proto][int(self.port_str)]['name']}"
            
            details["detected_os"] = self.handle_os_detection(nm)
            
            return details
    def __handle_by_address_resolving(self,cmd_res,ip_addr):
        if cmd_res == None or cmd_res[ip_addr] == None or cmd_res[ip_addr]['osmatch'] == None or len(cmd_res[ip_addr]['osmatch']) == 0: 
                    return "Unknown" 
                
        return cmd_res[ip_addr]['osmatch'][0]["name"]       
    
    def handle_os_detection(self,nm):
            
            if (os.getuid() != 0):#if not privileged user
                return "Unknown" 
            all_hosts = nm.all_hosts()
            ip_addr = all_hosts[0]
            try:
               
                cmd_res = nm.scan(self.host_str, self.port_str, arguments="-O")['scan']
                
                for addr in [ip_addr,self.host_str]:    
                     try:
                        result = self.__handle_by_address_resolving(cmd_res,addr)
                        if (result!= None and result!="Unknown"):
                            return result       
                     except:
                          pass
            except Exception as error:
                print(f"error:{error}")
                return "Unknown"
            return "Unknown"          