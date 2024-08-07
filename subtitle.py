import re

def parse_srt(data):
    pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\n|\n$)', re.DOTALL)
    matches = pattern.findall(data)
    
    srt_list = []
    for match in matches:
        index, time_start, time_end, text = match
        text = text.replace('\n', ' ')  
        srt_list.append({
            "index": int(index),
            "time_start": time_start,
            "time_end": time_end,
            "text": text
        })
    
    return srt_list

def convert_srt_to_array(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    
    srt_list = parse_srt(data)
    return srt_list


file_path = 'example.srt'
srt_list = convert_srt_to_array(file_path)


print(srt_list)
