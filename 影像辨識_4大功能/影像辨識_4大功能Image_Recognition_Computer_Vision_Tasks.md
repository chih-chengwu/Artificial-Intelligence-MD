# 影像辨識（Image Recognition）與電腦視覺任務

## 一、什麼是影像辨識？

影像辨識（Image Recognition）是利用電腦視覺（Computer Vision）與人工智慧技術，讓電腦能夠從影像中「看懂」或「辨識」其中的內容。

依照「電腦需要辨識到什麼程度」，常見的影像分析任務可以分成：

1. 分類（Classification）
2. 物體定位（Object Localization）
3. 物體偵測（Object Detection）
4. 影像分割（Image Segmentation）
   - 語義分割（Semantic Segmentation）
   - 實例分割（Instance Segmentation）

可以將它們理解成：

> **分類 → 這是什麼？**
>
> **定位 → 這是什麼？在哪裡？**
>
> **偵測 → 有哪些東西？各在哪裡？**
>
> **分割 → 每一個物件的精確輪廓在哪裡？**

---

# 二、四種影像辨識任務

## 1. 分類（Classification）

### 目的

判斷「整張圖片」屬於哪一個類別。

### 特徵

- 通常針對單一主要物件
- 只回答「這是什麼？」
- 不需要指出物件的位置
- 不需要畫框

### 例子

輸入一張圖片：

```text
        ┌───────────────┐
        │               │
        │      🐱       │
        │               │
        └───────────────┘
                 ↓
        Image Classification
                 ↓
               「貓」
```

例如：

```text
Input Image
     ↓
┌───────────────┐
│               │
│      🐱       │
│               │
└───────────────┘
     ↓
Class = Cat
```

### 電腦回答

> 「這張圖片是 **Cat（貓）**。」

### 重點

```text
Classification
      ↓
回答「是什麼？」
      ↓
Cat
```

---

# 2. 物體定位（Object Localization）

## 目的

除了判斷「這是什麼」之外，還要找出「物體在哪裡」。

通常假設圖片中只有**一個主要物體（Single Object）**。

因此可以理解為：

> **Object Localization = Classification + Localization**

### 例子

原始圖片：

```text
┌───────────────────────┐
│                       │
│         🐱            │
│                       │
└───────────────────────┘
```

經過 Object Localization：

```text
┌───────────────────────┐
│                       │
│      ┌─────────┐      │
│      │   🐱    │      │
│      │   Cat   │      │
│      └─────────┘      │
│                       │
└───────────────────────┘
```

電腦需要回答：

```text
物件類別：Cat
位置：     x, y
大小：     width, height
```

通常使用：

```text
Bounding Box（邊界框／外接框）
```

表示物體的位置。

### 重點

```text
Classification
      +
Localization
      ↓
Object Localization
      ↓
「這是什麼？」
「在哪裡？」
```

---

# 3. 物體偵測（Object Detection）

## 目的

當一張圖片中有**多個物體（Multiple Objects）**時，需要同時找出：

- 有哪些物體？
- 每個物體是什麼？
- 每個物體在哪裡？
- 每個物體有多大？

因此 Object Detection 可以看成：

> **Classification + Localization × Multiple Objects**

### 例子

原始圖片：

```text
┌─────────────────────────────┐
│                             │
│       🐱          🐶        │
│                             │
│              🚗             │
│                             │
└─────────────────────────────┘
```

經過 Object Detection：

```text
┌─────────────────────────────┐
│                             │
│    ┌──────┐    ┌──────┐    │
│    │ Cat  │    │ Dog  │    │
│    │  🐱  │    │  🐶  │    │
│    └──────┘    └──────┘    │
│                             │
│          ┌────────┐         │
│          │  Car   │         │
│          │   🚗   │         │
│          └────────┘         │
│                             │
└─────────────────────────────┘
```

電腦可能得到：

```text
Object 1 → Cat → Bounding Box
Object 2 → Dog → Bounding Box
Object 3 → Car → Bounding Box
```

### 常見輸出

每個物件通常包含：

```text
Class       → 類別
Confidence  → 信心分數
Bounding Box → 位置與大小
```

例如：

```text
Cat   0.95   (x, y, w, h)
Dog   0.91   (x, y, w, h)
Car   0.88   (x, y, w, h)
```

### 常見應用

- 人員偵測
- 車輛偵測
- 人臉偵測
- 瑕疵偵測
- 醫療影像病灶偵測
- X-ray 牙齒／蛀牙偵測

例如醫療影像：

```text
X-ray
  ↓
Object Detection
  ↓
┌──────────┐
│ Caries   │
│  病灶     │
└──────────┘
```

---

# 4. 影像分割（Image Segmentation）

影像分割的目的比 Object Detection 更進一步。

Object Detection 是：

> 「把物體框起來。」

Segmentation 則是：

> 「把物體的像素精確分出來。」

也就是從：

```text
Bounding Box
```

進一步做到：

```text
Pixel-level Segmentation
```

影像分割主要可以分成：

1. 語義分割（Semantic Segmentation）
2. 實例分割（Instance Segmentation）

---

# 4.A 語義分割（Semantic Segmentation）

## 目的

將圖片中的**每一個像素（Pixel）**分配到某一個類別。

也就是：

> **Pixel → Class**

### 例子

假設圖片中有：

```text
🐱 貓
🌳 樹
🏠 房子
```

Semantic Segmentation 會將每個 Pixel 分類：

```text
┌──────────────────────────┐
│ 樹 樹 樹 │  天空 天空    │
│ 樹 樹 樹 │  天空 天空    │
│──────────┼───────────────│
│ 貓 貓 貓 │  房子 房子    │
│ 貓 貓 貓 │  房子 房子    │
└──────────────────────────┘
```

重點是：

```text
每一個 Pixel
      ↓
判斷它屬於哪一個 Class
```

例如：

```text
Pixel 1 → Cat
Pixel 2 → Cat
Pixel 3 → Background
Pixel 4 → Tree
Pixel 5 → House
...
```

### 特別注意

Semantic Segmentation **不區分同一類別的不同個體**。

例如圖片中有兩隻貓：

```text
🐱       🐱
Cat      Cat
```

Semantic Segmentation 只會知道：

```text
這些 Pixel 都屬於 Cat
```

但是不一定知道：

```text
Cat 1
Cat 2
```

是兩個不同的個體。

---

# 4.B 實例分割（Instance Segmentation）

## 目的

Instance Segmentation 不只是知道：

> 「這個 Pixel 是 Cat。」

還要知道：

> 「這些 Pixel 是 Cat #1，那些 Pixel 是 Cat #2。」

也就是：

> **Pixel + Class + Instance**

### 例子

圖片中有兩隻貓：

```text
       🐱          🐱
      Cat #1      Cat #2
```

Instance Segmentation 會將兩隻貓分開：

```text
┌──────────────────────────┐
│                          │
│    ╭─────╮      ╭─────╮ │
│    │ Cat │      │ Cat │ │
│    │ #1  │      │ #2  │ │
│    ╰─────╯      ╰─────╯ │
│                          │
└──────────────────────────┘
```

而且不是使用矩形框，而是可以使用：

```text
Polygon（多邊形）
```

或像素遮罩：

```text
Mask
```

精確描述物體的輪廓。

---

# 三、Object Detection 與 Instance Segmentation 的差異

假設圖片中有一顆蘋果：

## Object Detection

只需要畫出矩形框：

```text
┌─────────────────────┐
│                     │
│      ┌────────┐     │
│      │  🍎    │     │
│      │ Apple  │     │
│      └────────┘     │
│                     │
└─────────────────────┘
```

它知道：

```text
Apple
位置
大小
```

但是框框裡面可能包含背景。

---

## Instance Segmentation

則會沿著蘋果真正的輪廓：

```text
┌─────────────────────┐
│                     │
│        ╭────╮       │
│       ╱ 🍎   ╲      │
│       ╲      ╱      │
│        ╰────╯       │
│                     │
└─────────────────────┘
```

因此可以得到更精確的：

```text
Object Mask
```

---

# 四、四種方法的比較

| 方法 | 中文 | 主要回答的問題 | 物件數量 | 是否有位置 | 是否到 Pixel |
|---|---|---|---|---|---|
| Classification | 分類 | 這是什麼？ | 通常單一 | ❌ | ❌ |
| Object Localization | 物體定位 | 這是什麼？在哪裡？ | 單一 | ✅ | ❌ |
| Object Detection | 物體偵測 | 有哪些物體？在哪裡？ | 多個 | ✅ | ❌ |
| Semantic Segmentation | 語義分割 | 每個 Pixel 屬於哪一類？ | 多個 | ✅ | ✅ |
| Instance Segmentation | 實例分割 | 每個物體的 Pixel 屬於哪個個體？ | 多個 | ✅ | ✅ |

---

# 五、由簡單到複雜的理解方式

```text
                    Image Recognition
                           │
                           ▼
                 ┌───────────────────┐
                 │ Classification    │
                 │     這是什麼？     │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Object            │
                 │ Localization      │
                 │ 這是什麼？在哪裡？ │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Object Detection  │
                 │ 有哪些？在哪裡？   │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   Segmentation    │
                 │ 精確到 Pixel      │
                 └─────────┬─────────┘
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
          Semantic              Instance
          Segmentation          Segmentation
          語義分割               實例分割
```

---

# 六、最簡單的口訣

## Classification

> **「這是什麼？」**

```text
🐱 → Cat
```

---

## Object Localization

> **「這是什麼？在哪裡？」**

```text
🐱 → Cat + Bounding Box
```

---

## Object Detection

> **「有哪些東西？各在哪裡？」**

```text
🐱 → Cat + Box
🐶 → Dog + Box
🚗 → Car + Box
```

---

## Semantic Segmentation

> **「每一個 Pixel 是什麼類別？」**

```text
Pixel → Cat / Dog / Car / Background
```

---

## Instance Segmentation

> **「每一個 Pixel 屬於哪一個物體？」**

```text
Cat #1 → Mask
Cat #2 → Mask
Dog #1 → Mask
```

---

# 七、醫療影像中的應用

以上四種技術也廣泛應用於醫療影像。

例如牙科 X-ray：

### Classification

```text
X-ray
  ↓
是否有蛀牙？
  ↓
Yes / No
```

### Object Detection

```text
X-ray
  ↓
找出蛀牙位置
  ↓
┌──────────┐
│  Caries  │
└──────────┘
```

### Semantic Segmentation

```text
X-ray
  ↓
將每一個 Pixel 分類
  ↓
Caries / Tooth / Background
```

### Instance Segmentation

```text
X-ray
  ↓
找出每一個蛀牙的精確輪廓
  ↓
Caries #1 → Mask
Caries #2 → Mask
Caries #3 → Mask
```

因此，在醫療影像研究中：

```text
Classification
       ↓
Object Detection
       ↓
Segmentation
       ↓
Pixel-level Analysis
```

通常可以看到模型從「判斷有沒有病灶」逐漸發展到「找出病灶位置」，再進一步做到「精確描繪病灶輪廓」。

---

# 八、重要觀念：Image Recognition ≠ Image Processing

嚴格來說：

**Image Processing（影像處理）**與**Image Recognition（影像辨識）**並不是完全相同的概念。

## Image Processing

主要是：

> 對影像本身進行處理。

例如：

- Resize
- Crop
- Rotate
- Noise Reduction
- Contrast Enhancement
- CLAHE
- Image Filtering

## Image Recognition / Computer Vision

主要是：

> 從影像中「理解」或「辨識」資訊。

例如：

- Classification
- Object Detection
- Segmentation
- Face Recognition
- OCR

因此，在課程教材中建議寫成：

> **電腦視覺（Computer Vision）中的常見影像辨識任務**

會比把 Classification、Detection、Segmentation 全部稱為「影像處理」更加精確。

---

# 九、一張圖理解四大任務

```text
                 一張圖片
                     │
                     ▼
          ┌──────────────────┐
          │ Classification   │
          │    這是什麼？     │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Localization     │
          │ 這是什麼？在哪裡？│
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Object Detection │
          │ 有哪些？在哪裡？  │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │  Segmentation    │
          │ 精確到 Pixel     │
          └────────┬─────────┘
                   │
             ┌─────┴─────┐
             ▼           ▼
        Semantic      Instance
        Segmentation  Segmentation
        語義分割       實例分割
```

## 一句話總結

> **Classification 是「辨識是什麼」；**
>
> **Localization 是「辨識是什麼＋在哪裡」；**
>
> **Detection 是「辨識多個物體是什麼＋各在哪裡」；**
>
> **Segmentation 則進一步做到 Pixel Level，精確描述物體的範圍與輪廓。**

---

# 十、補充：Object Detection 與 Image Captioning

「Object Detection 可以作到 Image Captioning」建議在教材中**分開來講**。

Object Detection 的框上標籤，例如：

```text
Cat
Dog
Car
```

是「物體類別標註」。

而 **Image Captioning（影像描述生成）**是進一步由模型產生自然語言句子，例如：

> **A cat is sitting on a chair.**

兩者是不同的 Computer Vision 任務。

可以簡單理解：

```text
Object Detection
       ↓
找出物體
       ↓
Cat / Dog / Car
       ↓
Bounding Box
```

而：

```text
Image Captioning
       ↓
理解整張圖片
       ↓
產生自然語言描述
       ↓
"A cat is sitting on a chair."
```

因此：

> **Object Detection ≠ Image Captioning**

但 Object Detection 所得到的物體資訊，可以作為某些更複雜影像理解系統的輸入資訊。
