import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = int(entry1.get())  # 入力値を取得
    if num1 <= 1911:
        num2 = int(num1) - 1867
        label1.config(text="明治" + str(num2) + "年")  # 画面に出力
    elif num1 <= 1925:
        num3 = int(num1) - 1911
        label1.config(text="大正" + str(num3) + "年")
    elif num1 <= 1988:
        num4 = int(num1) - 1925
        label1.config(text="昭和" + str(num4) + "年")
    elif num1 <= 2018:
        num5 = int(num1) - 1988
        label1.config(text="平成" + str(num5) + "年")
    else:
        num6 = int(num1) - 2018
        label1.config(text="令和" + str(num6) + "年")


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="和暦に変換", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
