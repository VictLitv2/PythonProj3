class ScanInfo:
    def __init__(self,scan_info_dict:dict) -> None:
        self.__dict__=scan_info_dict
        

    def __str__(self) -> str:
        return f"{self.__dict__}"   
