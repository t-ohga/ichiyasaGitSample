import math

def process_data(data_list):
  """
  数値リストを受け取り、その合計、平均、最大値を計算して表示する。
  """
  print(f"処理対象データ: {data_list}")

  # --- ↓↓↓ この下の計算ブロックを選択して関数化を試してください ↓↓↓ ---

  total, average, maximum, valid_calculation = practice(data_list)

  # --- ↑↑↑ この上の計算ブロックを選択してください ↑↑↑ ---

  # 計算結果の表示
  if valid_calculation:
    print("\n--- 処理結果詳細 ---")
    print(f"  合計値: {total}")
    print(f"  平均値: {average:.2f}")
    print(f"  最大値: {maximum}")
    print("--------------------")
  else:
    print("有効な計算は行われませんでした。")

def practice(tomoki):
    if not tomoki: # リストが空かチェック
      print("エラー: データリストが空です。")
      total = 0
      average = 0
      maximum = None
      valid_calculation = False
    else:
      total = sum(tomoki)
      average = total / len(tomoki)
      maximum = max(tomoki)
      print(f"計算結果: 合計={total}, 平均={average:.2f}, 最大値={maximum}")
      valid_calculation = True
    return total,average,maximum,valid_calculation


# --- メインの処理 ---
my_data = [15, 8, 22, 10, 3, 18, 5]
empty_list = []

print("=== 最初のデータ処理 ===")
process_data(my_data)

print("\n=== 空リストの処理 ===")
process_data(empty_list)

print("\n=== 処理完了 ===")