import tkinter as tk

# 　メッセージを表示できるようにする
from tkinter import messagebox

# お約束のコード
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)

# プレイヤーの設定
player1 = "罪"
player2 = "罰"

# current_playerは、現在プレイしているプレイヤーを示す変数
current_player = player1

# ボタンのリスト
buttons = []
# ループ処理
for i in range(9):
    button = tk.Button(
        window, text="", command=lambda i=i: button_action(i), width=3, height=3
    )
    buttons.append(button)

# リストのボタン
buttons[0].place(x=200, y=100)
buttons[1].place(x=270, y=100)
buttons[2].place(x=340, y=100)
buttons[3].place(x=200, y=170)
buttons[4].place(x=270, y=170)
buttons[5].place(x=340, y=170)
buttons[6].place(x=200, y=240)
buttons[7].place(x=270, y=240)
buttons[8].place(x=340, y=240)


# ボタンが押された時の場合分け
# indexは、選んだマスがボタンのリストの中でどの位置にあるかを示す
def button_action(index):
    # globalは、関数の外で定義された変数を使える
    global current_player

    # 選んだマスが空の時
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player

        # 勝った時
        if is_winner(current_player):
            # 情報を表示するダイアログボックス
            messagebox.showinfo("勝利", f"{current_player} の勝利です。おめでとう。")
            # 閉じる
            window.quit()

        # マスが全て埋まった時
        elif all(button["text"] != "" for button in buttons):
            messagebox.showinfo(
                "引き分け", "引き分けですね。今日の夕食はピロシキにしましょう。"
            )
            window.quit()

        # 交代する時
        else:
            current_player = player2 if current_player == player1 else player1

    # 選んだマスが埋まっていた時
    else:
        # 警告を表示するダイアログボックス
        messagebox.showwarning("無効", "そのマスはもう選べません。")


# 勝利条件
# 横、縦、斜めのいずれかが揃えば勝ち


# symbolは、プレイヤーの記号
def is_winner(symbol):
    # winning_combinationsは、勝利条件となる組み合わせを示すタプルのリスト
    # タプルは、Pythonのデータ構造の一つで、複数の要素を1つのまとまりとして扱うことができるコンテナ型
    winning_combinations = [
        # 横
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        # 縦
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        # 斜め
        (0, 4, 8),
        (2, 4, 6),
    ]

    # comboは,リストから取り出された各タプル
    for combo in winning_combinations:
        if (
            buttons[combo[0]]["text"] == symbol
            and buttons[combo[1]]["text"] == symbol
            and buttons[combo[2]]["text"] == symbol
        ):
            return True

    # 揃ってない
    return False


label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

window.mainloop()
