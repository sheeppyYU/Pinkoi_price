import tkinter as tk
from tkinter import messagebox

# 函數：計算商品金額
def calculate_product_amount():
    try:
        # 取得使用者輸入的淨利目標和運費
        target_profit = float(target_profit_entry.get())
        freight = float(freight_entry.get())
        
        # 定義商店抽取的費用計算函數
        def calculate_store_fee(product_amount):
            return (product_amount + freight) * 0.15 + 15

        # 初始化商品金額
        product_amount = 0

        # 計算商品金額，直到達到淨利目標
        while True:
            store_fee = calculate_store_fee(product_amount)
            net_profit = product_amount - store_fee

            if net_profit >= target_profit:
                break

            product_amount += 1

        # 顯示結果在文字框中
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"總價: {product_amount} 元。\n")
        result_text.insert(tk.END, f"運費: {freight} 元。\n")
        result_text.insert(tk.END, f"Pinkoi抽取費用: {round(store_fee)} 元。")
        result_text.config(state="disabled")
    
    except ValueError:
        # 處理輸入無效的情況
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "請輸入有效的數字。")
        result_text.config(state="disabled")

# 函數：計算器按鈕點擊事件
def calculate_button_click(event):
    try:
        # 獲取計算器輸入
        calculator_input = calculator_entry.get()
        
        # 計算表達式並顯示結果
        result = eval(calculator_input)
        calculator_result.config(text=f"結果：{result}")
    
    except Exception as e:
        messagebox.showerror("錯誤", "計算錯誤。請輸入有效的表達式。")

# 創建主視窗
window = tk.Tk()
window.title("pinkoi商品金額計算")

# 創建淨利目標輸入框
tk.Label(window, text="淨利目標：").pack()
target_profit_entry = tk.Entry(window)
target_profit_entry.pack()

# 創建運費輸入框
tk.Label(window, text="運費：").pack()
freight_entry = tk.Entry(window)
freight_entry.pack()

# 創建計算按鈕
calculate_button = tk.Button(window, text="計算", command=calculate_product_amount)
calculate_button.pack()

# 創建結果文字框
result_text = tk.Text(window, height=6, width=40)
result_text.config(state="disabled")
result_text.pack()

# 計算器部分
tk.Label(window, text="計算機").pack()
calculator_entry = tk.Entry(window)
calculator_entry.bind("<Return>", calculate_button_click)
calculator_entry.pack()

calculator_result = tk.Label(window, text="結果：")
calculator_result.pack()

# 啟動主視窗的事件循環
window.mainloop()
