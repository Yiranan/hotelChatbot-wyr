from zhipuai import ZhipuAI
import config

class LLMAPI:
    def __init__(self):
        self.api_key=config.api_key

    def QA(self,prompt):
        client = ZhipuAI(api_key=self.api_key) # 填写您自己的APIKey
        response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=[
                {"role": "user","content": prompt}
            ],
        )
        print(response.choices[0].message)
        
        return response.choices[0].message.content