import re
class InputProcessor:
    
    def __init__(self) -> None:
        host_pattern = "[a-zA-Z0-9\-\.]+"       
        #host_list_re_pattern = f"{host_pattern}((\s),)+{host_pattern}"
        #host_range_re_pattern = "([0-9].)*\-([0-9].)"

        port_pattern = "[0-9]{1,5}"
        #port_range_pattern = f"({port_pattern}\-{port_pattern})"
        patterns = \
        [
         host_pattern,        
         port_pattern         
         ]
        self.regex_patterns = {}
        for count, ptrn in enumerate(patterns):
            self.regex_patterns[count] = ptrn
        
        

        pass
    def process_hosts(self):
        user_input = input("Please enter hostname -URL or ip (list of hostames separated by commas): ")
        
        return self._process_inner([0],user_input)
        
   
    def _process_inner(self,indexes,user_input):
        parts = None
        for i in indexes:
            try:
               parts = self._parse(user_input,i)               
               if parts != None and len(parts) != 0: 
                   return parts   
            except Exception as error:
                pass
        return parts
    def process_ports(self):
        user_input = input("Please enter port or range of ports separated by hyphen: ")
        return self._process_inner([1],user_input)
        
    def _parse(self,user_input:str,re_type):
        regex_pattern = self.regex_patterns[re_type]
        
        parts = re.findall(regex_pattern,user_input)
       
        result = []
        for part in parts:
            if len(part)!=0:
                result.append(part)
        return result


