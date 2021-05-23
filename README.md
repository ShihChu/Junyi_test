# 2021 實習計畫-軟體 QA 實習生筆試
考試時間: 5/23 22:00~22:45
加分題: 額外花費40分鐘撰寫與修改

## Q1. 反轉字串
Run `Q1.py`
unit test: Run `Test_Q1.py`

## Q2. 扣除3和5倍數
Run `Q2.py`
unit test: Run `Test_Q2.py`


## Q3. 判斷筆種類問題
1. 選擇貼有標籤「混合」的袋子抽出一枝筆
2. 若抽出的筆為原子筆，則貼有「混合」標籤的為`原子筆`，貼有「原子筆」為`鉛筆`，而貼有「鉛筆」為`混合`
3. 反之，若抽出的筆為鉛筆，則貼有「混合」標籤的為`鉛筆`，貼有「原子筆」為`混合`，而貼有「鉛筆」為`原子筆`

解題關鍵在於袋子貼的標籤都是錯的，因此貼有「混合」標籤的筆袋，一定是單一筆種(不是鉛筆就是原子筆)。
一旦確認「混合」真正為哪一種筆之後，那貼有另一個筆種的袋子，就能直接判斷為混合。(例如抽出來的是鉛筆，那貼有原子筆的筆袋一定為混合比袋)。而最後的袋子就能直接對應判斷了。

| 原先貼有標籤 | 混合 | 鉛筆 | 原子筆 |
| ----------- | ---- | ---- | ---- |
| 可能筆的種類 | 鉛/原 | 混合/原 | 混合/鉛 |
| 假設抽出「原子筆」後的可能情形 | 原子筆 | 混合 | 鉛筆 |

## Q4. 金額找零問題
題目描述有問題的地方在於「加上人服務生私吞的 60 元」。
正確的描述應該為`(300-30)*3-750 = 60`
題目中的810元為顧客總共支付的金額，而750元為真正的付款金額。
顧客除了付了餐費750，還額外被服務生從中拿走了60元，因此總共付出去的錢為810元。

若涵蓋完整的付費金額應該為:
`300*3-750-60 = 30*3`