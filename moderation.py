from keys_private import MODERATION_API_KEY
import openai
openai.api_key = MODERATION_API_KEY
# 要审查的文本

text_to_moderate =input("请输入要审查的文本：")

try:
    response = openai.Moderation.create(input=text_to_moderate)

    # 获取审查结果
    output = response["results"][0]

    # 打印是否含有违禁词
    print("Flagged:", output["flagged"])

    # 判断并打印违禁词的性质
    if output["flagged"]:
        print("Detected Categories:")
        for category, flagged in output["categories"].items():
            if flagged:
                print(f"- {category}")
    else:
        print("No prohibited content detected.")
except Exception as e:
    print(f"An error occurred: {e}")
