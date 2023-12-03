import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import filedialog
import os

class QQSpaceCrawler:
    def __init__(self, root):
        self.root = root
        self.root.title("QQ空间爬虫")
        self.root.geometry("1280x720")  # 设置界面大小为720p
        self.root.option_add("*Font", "Helvetica 20")  # 设置字体大小

        self.output_folder = ""
        self.friends_data = {}

        self.create_ui()

    def create_ui(self):
        # 创建界面组件
        self.label = Label(self.root, text="QQ空间爬虫", font=("Helvetica", 30))
        self.label.pack(pady=20)

        self.output_folder_label = Label(self.root, text="选择输出文件夹:")
        self.output_folder_label.pack(pady=10)

        self.output_folder_button = Button(self.root, text="选择文件夹", command=self.choose_output_folder)
        self.output_folder_button.pack(pady=10)

        self.crawl_button = Button(self.root, text="开始爬取", command=self.crawl_qq_space)
        self.crawl_button.pack(pady=20)

    def choose_output_folder(self):
        self.output_folder = filedialog.askdirectory()
        self.output_folder_label.config(text=f"选择输出文件夹: {self.output_folder}")

    def crawl_qq_space(self):
        # 在这里添加爬取 QQ 空间的代码
        import requests
from bs4 import BeautifulSoup

class QQSpaceScraper:
    def __init__(self, qq_number):
        self.qq_number = qq_number

    def scrape_qq_space(self):
        url = f"https://user.qzone.qq.com/{self.qq_number}/311"
        
        # 伪装成浏览器发送请求，防止被阻止
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 在这里解析 HTML 页面，提取你需要的信息
            # 以下是一个简单的例子，假设空间内容在 class 为 "content" 的 div 中
            content_divs = soup.find_all('div', class_='content')
            for content_div in content_divs:
                content = content_div.text.strip()
                print(content)

    def run(self):
        self.scrape_qq_space()

if __name__ == "__main__":
    qq_scraper = QQSpaceScraper("你的QQ号码")
    qq_scraper.run()

        # 使用 requests 发送 HTTP 请求，BeautifulSoup 解析 HTML
        # 将爬取的数据保存到本地文件夹，并按好友名字分类

        # 示例代码
       # fake_data = {"friend1": "这是好友1的空间内容", "friend2": "这是好友2的空间内容"}
        self.friends_data = fake_data

        # 保存到本地文件夹
        self.save_to_local()

        # 显示爬取结果
        self.display_result()

    def save_to_local(self):
        for friend, data in self.friends_data.items():
            friend_folder = os.path.join(self.output_folder, friend)
            os.makedirs(friend_folder, exist_ok=True)

            with open(os.path.join(friend_folder, "空间内容.txt"), "w", encoding="utf-8") as f:
                f.write(data)

    def display_result(self):
        # 在这里添加显示爬取结果的代码，可以使用 Tkinter 的其他组件，比如 Text 组件

        # 示例代码
        result_text = Text(self.root, wrap=WORD)
        result_text.insert(INSERT, "爬取结果：\n")
        for friend, data in self.friends_data.items():
            result_text.insert(INSERT, f"{friend}:\n{data}\n\n")
        result_text.pack(pady=20)

if __name__ == "__main__":
    root = Tk()
    app = QQSpaceCrawler(root)
    root.mainloop()
