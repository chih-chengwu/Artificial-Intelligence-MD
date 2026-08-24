
# 人工智慧、機器學習與深度學習的關係及內容

## 一、三者的基本關係

人工智慧、機器學習與深度學習，可以用「由大到小」的包含關係來理解：

> **人工智慧 AI ⊃ 機器學習 ML ⊃ 深度學習 DL**

也就是：

```text
人工智慧 AI
└── 機器學習 Machine Learning
    └── 深度學習 Deep Learning
```

**深度學習是機器學習的一種，而機器學習又是人工智慧的一種。**

---

# 二、什麼是人工智慧 AI？

**人工智慧（Artificial Intelligence, AI）** 是一個最大的範圍。

它的目標是：

> **讓電腦或機器具備一些原本需要人類智慧才能完成的能力。**

例如：

* 👁️ **看懂影像** → 人臉辨識、X 光判讀
* 🗣️ **理解語言** → ChatGPT、語音助理
* ♟️ **做決策** → 下棋、遊戲 AI
* 🚗 **感知環境** → 自動駕駛
* 🤖 **與人互動** → 機器人
* 📊 **預測** → 房價預測、疾病風險預測

因此：

> **AI 是一個非常大的領域。**

而且 **AI 不一定要使用 Machine Learning**。

---

## 2.1 傳統 AI：規則式 AI

早期的 AI 可以使用：

> **規則（Rule）＋邏輯（Logic）**

例如：

```text
如果：

    溫度 > 38°C
    而且
    咳嗽 = 是

那麼：

    建議就醫
```

這也是一種 AI，但它不是 Machine Learning。

因為規則是：

> **由人類事先設計好的。**

---

# 三、什麼是機器學習 ML？

**機器學習（Machine Learning, ML）** 是 AI 裡面的一種方法。

核心概念是：

> **不要把所有規則都寫死，而是讓電腦從資料中學習規則。**

---

## 3.1 傳統程式設計 vs Machine Learning

### 傳統程式設計

人類直接告訴電腦規則：

```text
房價 = 100萬 × 房間數
     + 50萬 × 面積
     + ...
```

規則主要由人類設計。

---

### Machine Learning

Machine Learning 則是：

```text
大量資料
   ↓
Machine Learning
   ↓
學習資料中的規律
   ↓
建立模型
   ↓
輸入新的資料
   ↓
產生預測結果
```

例如房價預測：

|  面積 | 房間數 |  屋齡 |     房價 |
| ----: | -----: | ----: | -------: |
| 30 坪 |      3 | 10 年 |   800 萬 |
| 40 坪 |      3 |  5 年 | 1,100 萬 |
| 25 坪 |      2 | 15 年 |   650 萬 |
|   ... |    ... |   ... |      ... |

模型會從這些資料中學習：

> **面積、房間數、屋齡與房價之間的關係。**

---

# 四、Machine Learning 有哪些常見方法？

Machine Learning 包含許多不同的演算法。

---

## 4.1 Regression 回歸

主要用來預測：

> **數值型資料**

例如：

```text
房屋資料 → 預測房價

學生資料 → 預測成績

天氣資料 → 預測溫度
```

常見方法：

* Linear Regression
* Decision Tree Regression
* Random Forest Regression
* Support Vector Regression

---

## 4.2 Classification 分類

主要用來預測：

> **類別（Category）**

例如：

```text
Email → Spam / Not Spam

X-ray → Caries / Healthy

學生 → Pass / Fail
```

常見方法：

* Logistic Regression
* Decision Tree
* Random Forest
* KNN
* SVM

---

## 4.3 Clustering 分群

將資料自動分成不同群組。

例如：

```text
1000 位顧客
      ↓
   Clustering
      ↓
 ┌────┼────┐
 ↓    ↓    ↓
Group1 Group2 Group3
高消費  中消費  低消費
```

常見方法：

* K-Means
* Hierarchical Clustering
* DBSCAN

---

# 五、什麼是深度學習 DL？

**深度學習（Deep Learning, DL）** 是 Machine Learning 裡面的一種方法。

它主要使用：

> **人工神經網路（Artificial Neural Network, ANN）**

當神經網路具有多層結構時，就稱為：

> **Deep Neural Network → Deep Learning**

基本概念：

```text
Input
  ↓
Neural Network
  ↓
Hidden Layer
  ↓
Hidden Layer
  ↓
Hidden Layer
  ↓
Output
```

「Deep」主要就是指：

> **神經網路具有較多的層次。**

---

# 六、Deep Learning 的常見架構

## 6.1 CNN

**Convolutional Neural Network**

中文：

> **卷積神經網路**

主要應用於：

> **影像處理與電腦視覺**

例如：

```text
X-ray
  ↓
CNN
  ↓
學習影像特徵
  ↓
判斷是否有蛀牙
```

常見應用：

* 人臉辨識
* 物件偵測
* 影像分類
* 醫學影像分析
* X-ray 分析
* CT / MRI 分析

---

## 6.2 RNN / LSTM

**RNN（Recurrent Neural Network）**

**LSTM（Long Short-Term Memory）**

比較適合處理：

> **具有時間順序或序列關係的資料**

例如：

* 語音
* 股票時間序列
* 文字
* 感測器資料

---

## 6.3 Transformer

**Transformer** 是目前非常重要的 Deep Learning 架構。

廣泛應用於：

* ChatGPT
* 大型語言模型（LLM）
* 機器翻譯
* 文字生成
* 多模態 AI
* 語音與影像處理

---

# 七、三者的包含關係

可以用以下方式理解：

```text
                    人工智慧 AI
             ┌─────────────────────┐
             │                     │
             │   機器學習 ML         │
             │  ┌───────────────┐  │
             │  │               │  │
             │  │ 深度學習 DL    │  │
             │  │               │  │
             │  └───────────────┘  │
             │                     │
             └─────────────────────┘
```

也可以簡化成：

```text
AI
└── Machine Learning
    └── Deep Learning
```

---

# 八、為什麼現在常常把 AI、ML、DL 混在一起？

因為現在最熱門的 AI 技術，大部分都大量使用：

```text
AI
 ↓
Machine Learning
 ↓
Deep Learning
 ↓
CNN / Transformer / ...
```

例如 ChatGPT：

```text
Artificial Intelligence
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
Neural Network
        ↓
Transformer
        ↓
Large Language Model
        ↓
ChatGPT
```

所以我們說：

> **ChatGPT 是 AI**

沒有錯。

但是更精確地說：

> **ChatGPT 是基於深度學習技術的大型語言模型應用。**

---

# 九、用「學習方式」理解三者

這是非常適合課堂教學的一種理解方式。

### AI

> **我要讓電腦「像人一樣聰明」。**

↓

### Machine Learning

> **不要全部告訴電腦規則，讓電腦「從資料學習」。**

↓

### Deep Learning

> **使用「多層神經網路」從大量資料學習複雜特徵。**

因此可以簡化成：

| 名稱                       | 核心概念             | 例子                                          |
| -------------------------- | -------------------- | --------------------------------------------- |
| **AI**               | 讓機器具備智慧       | ChatGPT、自動駕駛                             |
| **Machine Learning** | 從資料學習規律       | Regression、Decision Tree、Random Forest、KNN |
| **Deep Learning**    | 使用多層神經網路學習 | CNN、RNN、Transformer                         |

---

# 十、三者的完整關係

```text
                 AI 人工智慧
                      │
          ┌───────────┴───────────┐
          │                       │
      規則式 AI              Machine Learning
                                  │
                     ┌────────────┴────────────┐
                     │                         │
                傳統 ML 方法              Deep Learning
                     │                         │
        ┌────────────┼────────────┐            │
        │            │            │            │
   Regression   Decision Tree    KNN     CNN / RNN / Transformer
        │            │            │
        └────────────┴────────────┘
```

---

# 十一、最重要的觀念

請特別注意：

> **不是所有 AI 都是 Machine Learning。**

例如：

```text
Rule-based AI
```

也是 AI，但不屬於 Machine Learning。

同樣地：

> **不是所有 Machine Learning 都是 Deep Learning。**

例如：

```text
Linear Regression
Decision Tree
Random Forest
KNN
SVM
```

都是 Machine Learning，但它們通常不被稱為 Deep Learning。

因此：

```text
AI
│
├── Rule-based AI
│
└── Machine Learning
    │
    ├── Linear Regression
    ├── Decision Tree
    ├── Random Forest
    ├── KNN
    ├── SVM
    │
    └── Deep Learning
        ├── CNN
        ├── RNN
        ├── LSTM
        └── Transformer
```

---

# 十二、一句話記住

> **AI 是「目標」，Machine Learning 是「讓機器從資料學習的方法」，Deep Learning 則是 Machine Learning 中使用深層神經網路的一類方法。**

最簡單的記法：

```text
AI
└── ML
    └── DL
```

**AI > Machine Learning > Deep Learning**

三者是：

> **大範圍 → 子領域 → 更具體的方法**
