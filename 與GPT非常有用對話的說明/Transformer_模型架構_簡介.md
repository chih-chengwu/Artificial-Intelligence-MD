# Transformer 模型架構

註: [延伸閱讀](https://ithelp.ithome.com.tw/m/articles/10321437)

## 1. 什麼是 Transformer？

**Transformer** 是一種以 **Attention（注意力機制）** 為核心的深度學習模型架構，最早用於自然語言處理（NLP），現在也廣泛應用於：

- ChatGPT 等大型語言模型（LLM）
- 機器翻譯
- 文字生成
- 影像辨識
- 語音處理
- 多模態 AI

Transformer 的重要特色是：**不需要像 RNN 一樣依序處理資料，而是可以透過 Attention 同時考慮整段資料中不同位置之間的關係。**

---

## 2. Transformer 的核心：Attention

Transformer 最重要的概念是：

> **Attention：讓模型學習「目前這個詞，應該注意其他哪些詞」。**

例如：

> 「小明把書放在桌子上，因為**它**很乾淨。」

模型需要判斷「它」比較可能指的是「桌子」。

Attention 可以計算不同詞之間的關聯程度，讓模型知道：

```text
小明 ─────┐
書 ───────┤
桌子 ─────┼──→ Attention → 「它」與哪些詞關聯較大？
乾淨 ─────┘
```

---

## 3. Transformer 的主要結構

原始 Transformer 主要由兩大部分組成：

```text
輸入文字
   ↓
Embedding
   ↓
Positional Encoding
   ↓
┌─────────────────┐
│     Encoder     │
│                 │
│ Self-Attention  │
│       ↓         │
│ Feed Forward    │
└─────────────────┘
   ↓
┌─────────────────┐
│     Decoder     │
│                 │
│ Self-Attention  │
│       ↓         │
│ Cross-Attention │
│       ↓         │
│ Feed Forward    │
└─────────────────┘
   ↓
輸出文字
```

### Encoder

主要負責：

> **理解輸入資料的內容與上下文關係。**

### Decoder

主要負責：

> **根據已理解的資訊，一步一步產生輸出結果。**

---

## 4. 一個 Transformer Block 包含什麼？

Transformer 的 Encoder 或 Decoder 都是由多個 Block 堆疊而成。

一個基本 Block 可以簡化表示為：

```text
輸入
 ↓
Multi-Head Self-Attention
 ↓
Feed Forward Network
 ↓
輸出
```

實際架構還包含：

- Residual Connection（殘差連接）
- Layer Normalization（層正規化）

---

## 5. Multi-Head Attention 是什麼？

Transformer 不只使用一個 Attention，而是使用多個 Attention，稱為：

**Multi-Head Attention（多頭注意力）**

不同的 Head 可以學習不同類型的關係，例如：

```text
Head 1 → 語法關係
Head 2 → 主詞與動詞關係
Head 3 → 遠距離詞語關係
Head 4 → 語意關係
```

最後再將多個 Head 的結果整合。

---

## 6. Positional Encoding

Attention 本身不具有「先後順序」的概念。

例如：

```text
我 喜歡 吃 蘋果
```

與

```text
蘋果 吃 喜歡 我
```

如果只看詞本身，可能缺少順序資訊。

因此 Transformer 使用 **Positional Encoding（位置編碼）**，讓模型知道每個詞在序列中的位置。

---

## 7. Transformer 與 CNN、RNN 的簡單比較

| 模型                  | 主要特色                                | 常見應用                       |
| --------------------- | --------------------------------------- | ------------------------------ |
| CNN                   | 擅長學習局部特徵                        | 影像辨識                       |
| RNN                   | 依序處理序列資料                        | 文字、語音                     |
| LSTM                  | 改良 RNN，可處理較長期關係              | 文字、時間序列                 |
| **Transformer** | **以 Attention 建立資料間的關係** | **LLM、NLP、影像、語音** |

---

## 8. 一句話理解 Transformer

> **Transformer 是一種以 Attention 為核心，透過學習資料中不同位置之間的關係來理解與產生資料的深度學習模型架構。**

可以把它簡單記成：

```text
Transformer
    ↓
Attention
    ↓
學習資料彼此之間的關係
    ↓
理解 / 分析 / 產生資料
```

---

## 9. 與 ChatGPT 的關係

ChatGPT 所使用的 GPT 類模型，是建立在 **Transformer 架構**上的大型語言模型。

簡單來說：

```text
Transformer
     ↓
GPT 架構
     ↓
大型語言模型（LLM）
     ↓
ChatGPT
```

因此：

> **Transformer 是架構（Architecture），GPT 是建立在 Transformer 架構上的模型家族。**
