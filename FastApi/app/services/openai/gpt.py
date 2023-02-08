import re

import openai
import os
from datetime import datetime, timedelta


class Openai:
    def __init__(self):
        pass

    def test(self):
        openai.api_key = ''
        city = "New York"
        topic = f"Top 10 Restaurants you must visit when traveling to {city}"
        category = "travel"
        print(topic)
        prompt = f"Write blog posts in markdown format.Write the theme of your blog as {topic}.Highlight, bold, or italicize important words or sentences.Please include the restaurant's address, menu recommendations and other helpful information(opening and closing hours) as a list style.Please make the entire blog less than 10 minutes long.The audience of this article is 20-40 years old.Create several hashtags and add them only at the end of the line.Add a summary of the entire article at the beginning of the blog post."
        response = self.generate_blog(topic, prompt)
        # 생성된 글 출력
        print(response.choices[0].text)
        hashtag_pattern = r'(#+[a-zA-Z0-9(_)]{1,})'

        re.findall(hashtag_pattern, response['choices'][0]['text'])
        hashtags = [w[1:] for w in re.findall(hashtag_pattern, response['choices'][0]['text'])]
        tag_string = ""
        for w in hashtags:
            # 3글자 이상 추출
            if len(w) > 3:
                tag_string += f'{w}, '
        print(tag_string)
        tag_string = re.sub(r'[^a-zA-Z, ]', '', tag_string)
        tag_string = tag_string.strip()[:-1]
        print(tag_string)

        page_head = f'''---
                layout: single
                title:  "{topic}"
                categories: {category}
                tag: [{tag_string}]
                toc: false
                author_profile: false
                sidebar:
                    nav: "counts"
                ---
                '''
        print(page_head)

        body = '\n'.join(response['choices'][0]['text'].strip().split('\n')[1:])
        output = page_head + body
        print(output)
        yesterday = datetime.now() - timedelta(days=1)
        print(yesterday)
        timestring = yesterday.strftime('%Y-%m-%d')
        print(timestring)
        filename = f"{timestring}-{'-'.join(topic.lower().split())}.md"
        print(filename)
        #blog_directory = r"C:\Users\AIA\project\FastApi\app\services\translator\save"
        path = os.getcwd()
        filepath = os.path.join(path, filename)
        print(filepath)
        with open(filepath, 'w') as f:
            f.write(output)
            f.close()
    def generate_blog(self,topic, prompt):
        # 모델 엔진 선택
        model_engine = "text-davinci-003"

        # 맥스 토큰
        max_tokens = 2048

        # 블로그 생성
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.3,      # creativity
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return completion

if __name__ == '__main__':
    Openai().test()