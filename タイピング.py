import tkinter as tk
import random

# 例文のリスト（ここでは4つの例文を用意）
example_sentences = [
    "君では私を殺せない",
    "自分を憐れめば、人生は終わりなき悪夢だ",
    "正しさとは武器だ",
    "2度目はなくってよ！",
]

window = tk.Tk()
window.title("Typing Practice App")
window.geometry("600x400")

bg_color = "#333333"
fg_color = "#FFFFFF"
window.configure(bg=bg_color)


def select_random_sentence():
    return random.choice(example_sentences)


# グローバル変数として宣言
current_sentence = select_random_sentence()


def button_action():
    global current_sentence  # グローバル変数を参照
    user_input = entry1.get().strip()  # 入力値を取得して前後の空白を除去
    if user_input == current_sentence:
        label1.config(text="正解！", fg="green")
    else:
        label1.config(text="不正解。正しい文は:\n" + current_sentence, fg="red")

    # 新しい例文を選択して表示する
    current_sentence = (
        select_random_sentence()
    )  # 新しい例文を選択してグローバル変数を更新
    label_sentence.config(text=current_sentence)
    entry1.delete(0, tk.END)  # 入力フィールドをクリア


label_sentence = tk.Label(
    window,
    text=current_sentence,
    bg=bg_color,
    fg=fg_color,
    wraplength=500,
    justify="center",
)
label_sentence.pack(pady=20)

entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

button1 = tk.Button(window, text="チェック", command=button_action)
button1.pack(pady=10)

label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

window.mainloop()
