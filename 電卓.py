import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button1_action():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = 
     # 入力値を取得
    num2 = int(entry2.get())
    num3 = int(num1) + int(num2)  # 画面に出力
    label1.config(text=int(num3))


def button2_action():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    num4 = int(num1) - int(num2)
    label1.config(text=int(num4))


def button3_action():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    num5 = int(num1) * int(num2)
    label1.config(text=int(num5))


def button4_action():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    num6 = int(num1) / int(num2)
    label1.config(text=int(num6))


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)
entry2 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry2.pack(pady=10)


# ボタンの作成
button1 = tk.Button(window, text="+", command=button1_action)
button1.pack(pady=10)
button2 = tk.Button(window, text="-", command=button2_action)
button2.pack(pady=10)
button3 = tk.Button(window, text="×", command=button3_action)
button3.pack(pady=10)
button4 = tk.Button(window, text="÷", command=button4_action)
button4.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
