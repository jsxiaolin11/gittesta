import tkinter as tk
import random
from tkinter import messagebox


class GuessNumberGame:
    def __init__(self, root):
        # 主窗口基础配置
        self.root = root
        self.root.title("数字炸弹游戏")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # 游戏核心变量初始化
        self.target_num = random.randrange(1, 100)
        self.guess_count = 0
        self.range_min = 1
        self.range_max = 99

        # 构建界面元素
        self.build_ui()

    def build_ui(self):
        # 标题标签
        tk.Label(
            self.root,
            text="🎲 数字炸弹游戏",
            font=("微软雅黑", 22, "bold")
        ).pack(pady=20)

        # 提示标签
        self.tip_label = tk.Label(
            self.root,
            text="系统已生成1-99之间的整数，请输入你的猜测：",
            font=("微软雅黑", 12)
        )
        self.tip_label.pack(pady=5)

        # 输入框
        self.input_entry = tk.Entry(
            self.root,
            font=("微软雅黑", 16),
            width=15,
            justify="center"
        )
        self.input_entry.pack(pady=10)

        # 结果反馈标签
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("微软雅黑", 14)
        )
        self.result_label.pack(pady=10)

        # 次数统计标签
        self.count_label = tk.Label(
            self.root,
            text=f"已猜测次数：{self.guess_count}",
            font=("微软雅黑", 12)
        )
        self.count_label.pack(pady=5)

        # 按钮区域
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        self.submit_btn = tk.Button(
            btn_frame,
            text="提交猜测",
            command=self.check_guess,
            font=("微软雅黑", 12),
            width=10,
            #height=2,
            bg="#87CEEB"
        )
        self.submit_btn.grid(row=0, column=0, padx=10,pady=5)

        tk.Button(
            btn_frame,
            text="重新开始",
            command=self.restart_game,
            font=("微软雅黑", 12),
            width=10,
            #height=2,
            bg="#90EE90"
        ).grid(row=0, column=1, padx=10,pady=5)

    def check_guess(self):
        # 输入合法性校验
        try:
            guess = int(self.input_entry.get())
        except ValueError:
            #messagebox.showwarning("输入错误", "请输入有效的整数！")
            self.result_label.config(text="输入错误, 请输入有效的整数！", fg="red")
            self.input_entry.delete(0, tk.END)
            return

        # 范围校验
        if guess < 1 or guess > 99:
            #messagebox.showwarning("范围错误", "请输入1到99之间的数字！")
            self.result_label.config(text="范围错误, 请输入1到99之间的数字！", fg="red")
            self.input_entry.delete(0, tk.END)
            return

        # 计数 +1
        self.guess_count += 1
        self.count_label.config(text=f"已猜测次数：{self.guess_count}")

        # 核心判断逻辑
        if guess < self.target_num:
            #self.result_label.config(text="❄️ 猜小了，再大一点！", fg="#FF8C00")
            if guess < self.range_min:
                self.result_label.config(text=f"❄️ 猜小了，请输入{self.range_min}到{self.range_max}之间的数字！", fg="#FF8C00")
            else:
                self.range_min = guess + 1
                self.result_label.config(text=f"❄️ 猜小了，请输入{self.range_min}到{self.range_max}之间的数字！", fg="#FF8C00")
        elif guess > self.target_num:
            #self.result_label.config(text="🔥 猜大了，再小一点！", fg="#DC143C")
            if guess > self.range_max:
                self.result_label.config(text=f"🔥 猜大了，请输入{self.range_min}到{self.range_max}之间的数字！", fg="#00BFFF")
            else:
                self.range_max = guess - 1
                self.result_label.config(text=f"🔥 猜大了，请输入{self.range_min}到{self.range_max}之间的数字！", fg="#00BFFF")
        else:
            self.result_label.config(text=f"🎉 恭喜你，{self.guess_count}次后你被炸死了！", fg="#228B22")
            self.submit_btn.config(state="disabled")   # 👈 禁用提交按钮
            self.input_entry.delete(0, tk.END)
            return   # 👈 提前结束，不继续清空
           
        # 清空输入框，方便继续输入
        self.input_entry.delete(0, tk.END)

    def restart_game(self):
        # 重置游戏状态
        self.target_num = random.randrange(1, 100)
        self.guess_count = 0
        self.range_min = 1
        self.range_max = 99
        self.result_label.config(text="")
        self.count_label.config(text=f"已猜测次数：{self.guess_count}")
        self.input_entry.delete(0, tk.END)
        self.submit_btn.config(state="normal")    # 👈 重新启用提交按钮
        self.input_entry.focus_set()               # 👈 输入框自动获得焦点


if __name__ == "__main__":
    app = tk.Tk()
    game = GuessNumberGame(app)
    app.mainloop()