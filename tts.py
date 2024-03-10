import requests
import json
from keys_private import API_KEY,TTS_API_BASE

headers = {
    'Authorization': f'Bearer {API_KEY}', 
    'Content-Type':'application/json'
}
url = TTS_API_BASE

input_text = input("请输入需要转换成语音的文本: ")
query = {
            "model":"tts-1",
            "input":input_text,
            "voice":"echo",# 人物角色
            "response_format":"mp3",
            "speed":1,
        }
"""现阶段支持的人物角色：
alloy
echo
fable
onyx
nova
shimmer
具体效果可以自行尝试
"""
#
"""
现阶段支持的返回格式：
默认格式为mp3
opus：用于互联网流媒体和通信，延迟低。
aac：用于数字音频压缩，被YouTube、Android和iOS青睐。
flac：用于无损音频压缩，音频发烧友用于存档。
wav：无压缩的WAV音频，适用于需要低延迟的应用以避免解码开销。
pcm：类似于WAV，但包含24kHz（16位有符号，低端字节序）的原始样本，没有头部。
"""

response = requests.post(url=url, data=json.dumps(query), headers=headers)
print("Status Code:", response.status_code)
print("Response Content:", response.content[:100])  # 打印前100个字节以检查

filename = input("请输入预期的文件名: ")
f = open(filename+'.mp3', "wb")#这里需要根据上面的格式自行修改后缀名
f.write(response.content)
f.close()