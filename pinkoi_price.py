# 請使用者輸入淨利目標
target_profit = float(input("請輸入淨利目標："))


freight= float(input("請輸入運費："))


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

# 打印所需的商品金額
print(f"為了達到淨利目標 {target_profit} 元，商品金額需設定為 {product_amount} 元。")
print(f"商店抽取費用為{store_fee}元")
