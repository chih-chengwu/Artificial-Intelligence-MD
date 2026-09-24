# Python 套件匯入方式：`from ... import ...` 與 `import ... as ...`

## 一、兩種匯入方式有什麼不同？

Python 中常見的套件匯入方式有：

```python
from 套件 import 成員
```

以及：

```python
import 套件 as 別名
```

兩者的**主要差別在於「匯入的對象」以及「之後如何使用」**。

---

## 二、`from ... import ...`

### 1. 基本語法

```python
from 套件 import 成員
```

意思是：

> 從某個套件（module / package）中，直接匯入指定的「函式、類別或其他成員」。

例如：

```python
from sklearn.model_selection import train_test_split
```

這裡：

- `sklearn`：套件
- `model_selection`：`sklearn` 底下的模組
- `train_test_split`：要匯入的函式

匯入之後，可以直接使用：

```python
train_test_split(...)
```

不需要再寫：

```python
sklearn.model_selection.train_test_split(...)
```

### 2. 優點

程式碼通常比較簡潔：

```python
train_test_split(X, y, test_size=0.2)
```

而不是：

```python
sklearn.model_selection.train_test_split(X, y, test_size=0.2)
```

---

## 三、`import ... as ...`

### 1. 基本語法

```python
import 套件 as 別名
```

意思是：

> 將整個模組或套件匯入，並幫它取一個較簡短的名稱。

例如：

```python
import numpy as np
```

表示：

> 匯入 `numpy`，並將它簡稱為 `np`。

因此後面可以寫：

```python
np.array([1, 2, 3])
np.mean([10, 20, 30])
```

而不必寫：

```python
numpy.array([1, 2, 3])
numpy.mean([10, 20, 30])
```

---

## 四、兩者可以互相替換嗎？

### 答案：通常「不能直接互換」

例如：

```python
from sklearn.model_selection import train_test_split
```

與：

```python
import sklearn.model_selection as train_test_split
```

**不是同一件事。**

第一種：

```python
from sklearn.model_selection import train_test_split
```

取得的是：

```text
train_test_split 函式
```

所以可以直接：

```python
train_test_split(X, y)
```

第二種：

```python
import sklearn.model_selection as train_test_split
```

取得的是：

```text
sklearn.model_selection 模組
```

因此應該使用：

```python
train_test_split.train_test_split(X, y)
```

這通常不是我們想要的寫法。

---

## 五、但是有些情況可以達到類似效果

例如：

```python
from numpy import array
```

之後：

```python
array([1, 2, 3])
```

也可以寫成：

```python
import numpy as np
```

之後：

```python
np.array([1, 2, 3])
```

兩者都可以使用 `numpy` 的 `array` 功能，但**匯入方式與名稱空間不同**。

可以簡單理解成：

| 寫法                | 匯入什麼       | 使用方式  |
| ------------------- | -------------- | --------- |
| `from A import B` | A 裡面的 B     | `B()`   |
| `import A`        | 整個 A         | `A.B()` |
| `import A as C`   | 整個 A，取名 C | `C.B()` |

---

# 六、以下程式碼逐行說明

原始程式：

```python
from sklearn.model_selection import train_test_split

import numpy as np

# 1121107改成如下
# import keras.utils as np_utils

import tensorflow.keras.utils as np_utils
```

---

## 1. `from sklearn.model_selection import train_test_split`

```python
from sklearn.model_selection import train_test_split
```

這是從 Scikit-learn 中匯入資料切分函式。

### 結構

```text
sklearn
   └── model_selection
          └── train_test_split
```

其中：

- `sklearn`：Scikit-learn 機器學習套件
- `model_selection`：模型選擇相關功能
- `train_test_split`：將資料切分成訓練資料與測試資料的函式

例如：

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

代表將資料分成：

```text
80% → Training Data
20% → Test Data
```

### 為什麼使用 `from ... import ...`？

因為我們通常只需要使用這一個函式：

```python
train_test_split()
```

所以直接匯入它即可。

---

# 七、`import numpy as np`

```python
import numpy as np
```

這是 Python 非常常見的寫法。

`numpy` 是 Python 中非常重要的數值運算套件，常用於：

- 陣列（Array）
- 矩陣
- 數值運算
- 線性代數
- 科學計算

例如：

```python
np.array([1, 2, 3, 4])
```

建立 NumPy 陣列。

也可以：

```python
np.mean([10, 20, 30])
```

計算平均值。

---

## 為什麼使用 `as np`？

因為 `numpy` 很常使用，所以 Python 社群長期形成慣例：

```python
import numpy as np
```

之後：

```python
np.array()
np.mean()
np.max()
np.min()
```

而不是：

```python
numpy.array()
numpy.mean()
numpy.max()
numpy.min()
```

因此：

```python
np
```

就是 `numpy` 的**別名（alias）**。

---

# 八、`keras.utils` 與 `tensorflow.keras.utils`

原始程式中有：

```python
# import keras.utils as np_utils
```

這一行前面有 `#`，所以目前是：

> **註解（comment），不會執行。**

後面改成：

```python
import tensorflow.keras.utils as np_utils
```

這一行才會真正執行。

---

## 1. 原本的寫法

```python
import keras.utils as np_utils
```

意思是：

```text
keras
 └── utils
```

將 `keras.utils` 匯入，並取名為：

```text
np_utils
```

因此後面可以寫：

```python
np_utils.to_categorical(...)
```

---

## 2. 修改後

```python
import tensorflow.keras.utils as np_utils
```

意思是：

```text
tensorflow
   └── keras
        └── utils
```

將 `tensorflow.keras.utils` 匯入，並同樣取名為：

```text
np_utils
```

因此後面的程式仍然可以使用：

```python
np_utils.to_categorical(...)
```

---

# 九、為什麼明明是 `tensorflow.keras.utils`，卻叫 `np_utils`？

這裡容易讓初學者感到疑惑。

```python
import tensorflow.keras.utils as np_utils
```

最後的：

```python
np_utils
```

只是**自己取的別名**。

它並不是說：

```text
np_utils = numpy
```

也不是說：

```text
np_utils 一定是 NumPy
```

例如下面三種寫法都是合法的：

```python
import numpy as np
```

```python
import tensorflow.keras.utils as np_utils
```

```python
import tensorflow.keras.utils as abc
```

只是我們通常依照程式或教材原本的命名習慣，繼續使用：

```python
np_utils
```

所以舊程式即使從：

```python
import keras.utils as np_utils
```

改成：

```python
import tensorflow.keras.utils as np_utils
```

後面的程式碼通常不需要跟著修改。

---

# 十、這裡最重要的觀念

可以把兩種寫法想成：

### `from ... import ...`

```python
from sklearn.model_selection import train_test_split
```

像是：

> 「我只要這個東西，直接拿來用。」

因此：

```python
train_test_split(...)
```

---

### `import ... as ...`

```python
import numpy as np
```

像是：

> 「我要使用這個套件，並幫它取一個簡短的名字。」

因此：

```python
np.array(...)
np.mean(...)
np.max(...)
```

---

# 十一、最簡單的比較

```python
# 方法一
from sklearn.model_selection import train_test_split

train_test_split(X, y)
```

可以理解為：

```text
直接把 train_test_split 拿出來使用
```

---

```python
# 方法二
import numpy as np

np.array([1, 2, 3])
```

可以理解為：

```text
把 numpy 整個匯入，並取名為 np
```

---

# 十二、三種常見寫法整理

| Python 寫法                 | 意義                          | 使用方式          |
| --------------------------- | ----------------------------- | ----------------- |
| `import numpy`            | 匯入整個`numpy`             | `numpy.array()` |
| `import numpy as np`      | 匯入`numpy` 並取別名 `np` | `np.array()`    |
| `from numpy import array` | 只匯入`array`               | `array()`       |

---

# 十三、實際教學時可以這樣記

可以把它記成一句話：

> **`import` 是「把模組帶進來」，`as` 是「幫它取別名」；`from ... import ...` 則是「從模組裡直接拿出指定的功能」。**

### `import ... as ...`

```python
import numpy as np
```

```text
numpy
  ↓
取別名
  ↓
 np
```

使用：

```python
np.array()
np.mean()
```

### `from ... import ...`

```python
from sklearn.model_selection import train_test_split
```

```text
sklearn.model_selection
          ↓
取出
          ↓
train_test_split
```

使用：

```python
train_test_split()
```

---

# 十四、對本範例程式的總整理

```python
from sklearn.model_selection import train_test_split

import numpy as np

# 舊寫法
# import keras.utils as np_utils

# 新寫法
import tensorflow.keras.utils as np_utils
```

可以理解成：

```text
① train_test_split
   ↓
從 sklearn 中直接取出函式
   ↓
train_test_split()


② numpy
   ↓
整個匯入，取別名 np
   ↓
np.array()
np.mean()


③ tensorflow.keras.utils
   ↓
整個 utils 模組匯入
   ↓
取別名 np_utils
   ↓
np_utils.to_categorical()
```

因此，這三行其實示範了 Python 中非常重要的兩種套件匯入觀念：

```python
from ... import ...
```

與

```python
import ... as ...
```

**兩者不是單純的寫法不同，而是「匯入的對象」和「使用時的名稱空間」不同。**
