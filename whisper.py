import openai
import json
from keys_private import API_KEY,WHISPER_BASE

openai.api_key = API_KEY
openai.api_base = WHISPER_BASE

def audio_transcriptions(file_name):
    with open(file_name, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)
        json_str = json.dumps(response, ensure_ascii=False)
        return json_str


def send_text_to_gpt(text):
  # 向GPT发送文本，并获取是否为繁体中文的判断以及转换后的简体中文
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "这是一个将繁体中文转换为简体中文的任务,如果输入的不是中文，则直接输出原文。"},
      {"role": "user", "content": text},
    ],
    temperature=0.3,
  )
  return response['choices'][0]['message']['content'].strip()



if __name__ == '__main__':
    audio_file_path = input("请输入音频文件路径：(注意格式)")

    transcription = audio_transcriptions(audio_file_path)

    transcription_text = json.loads(transcription)['text']


    simplified_chinese_text = send_text_to_gpt(transcription_text)
    print({simplified_chinese_text})
