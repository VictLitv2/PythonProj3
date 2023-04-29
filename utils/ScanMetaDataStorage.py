import yaml
class ScanMetaDataStorage:
    def __init__(self,scan_meta_data_config_path="./config.yaml") -> None:
        self.scan_meta_data_config_path = scan_meta_data_config_path
        pass
    
    def process_meta_data(self):
                
        with open(self.scan_meta_data_config_path) as yaml_config_file:
            config_props = yaml.safe_load(yaml_config_file)

            app_config_items = []
            for app_config_item_key in config_props.keys():
                app_config_item_props = config_props.get(app_config_item_key)
                app_config_item = (app_config_item_key,app_config_item_props)
                app_config_items.append(app_config_item)
                
        return config_props


        pass
