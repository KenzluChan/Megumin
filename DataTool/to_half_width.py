import unicodedata
import yaml

def fullwidth_to_halfwidth(text):
    return ''.join(
        unicodedata.normalize('NFKC', char) if unicodedata.east_asian_width(char) in ['F', 'W'] else char
        for char in text
    )

def convert_yaml_fullwidth_to_halfwidth(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    
    def convert_dict(data):
        if isinstance(data, dict):
            return {convert_dict(key): convert_dict(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [convert_dict(item) for item in data]
        elif isinstance(data, str):
            return fullwidth_to_halfwidth(data)
        else:
            return data
    
    converted_data = convert_dict(data)

    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(converted_data, file, allow_unicode=True)
    
    print("轉換完成，檔案已更新。")

# 使用範例
convert_yaml_fullwidth_to_halfwidth(r'C:\Users\kenzl\AppData\Local\Programs\Python\Python312\Lib\site-packages\chatterbot_corpus\data\tc\Customize.yml')