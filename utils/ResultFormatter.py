import json
from model.ScanInfo import ScanInfo
class ResultFormatter:
    result:ScanInfo = None
    def __init__(self,result:ScanInfo) -> None:
        self.result = result
        
    def with_scan_meta_data(self,scan_meta_data)->object:
        self.scan_meta_data = scan_meta_data
        return self
    
    def format(self):
        result_str = ""
        if self.result is None:
            return result_str
        result_data:dict = self.result.__dict__
        scan_meta_data = self.scan_meta_data
        keys = list(scan_meta_data)
        
        if  keys is None or len(keys) == 0:
            return result_str
        result_str += "Found result:\n"
        for key in keys:
            result_str += f"{scan_meta_data[key]} : {result_data[key]}\n"
        return result_str    