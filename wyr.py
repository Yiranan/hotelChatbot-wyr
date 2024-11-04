import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess  # 导入 subprocess 模块

# 点击按钮时运行 Streamlit 应用并关闭窗口
def open_streamlit_app():
    # 使用 subprocess 运行 Streamlit 应用
    subprocess.Popen(["streamlit", "run", "hotelChatbot_wyr.py"])
    start_window.destroy()  # 关闭主窗口


# 创建启动窗口
start_window = tk.Tk()
start_window.title("Warwick Conference Chatbot")
start_window.geometry("500x400")
start_window.configure(bg="#4CAF50")

# 欢迎标签
welcome_label = tk.Label(start_window, text="Welcome to Al Chatbot!\nYou can ask me any questiones\nabout Warwick Conference!", font=("Arial", 18), bg="#4CAF50", fg="white", pady=20)
welcome_label.pack(pady=50)

# 启动按钮
start_button = tk.Button(start_window, text="Start Chat", font=("Arial", 14), bg="white", fg="#4CAF50", 
                         width=15, height=2, relief="flat", command=open_streamlit_app)
start_button.pack(pady=20)

# 启动窗口的主循环
start_window.mainloop()
