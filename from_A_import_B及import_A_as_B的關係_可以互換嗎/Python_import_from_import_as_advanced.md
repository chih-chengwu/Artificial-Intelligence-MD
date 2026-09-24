# Python `from ... import ...` 與 `import ... as ...`：可以互換嗎？

## 一、先看原本的 3 行程式

```python
from sklearn.model_selection import train_test_split

import numpy as np

import tensorflow.keras.utils as np_utils
```

這三行其實代表三種不同的匯入概念。

---

# 二、第 1 行可以改成這樣嗎？

原本：

```python
from sklearn.model_selection import train_test_split
```

提問：

```python
import sklearn.model_selection.train_test_split as split
```

## 答案：❌ 不可以

原因是：

> `import ...` 的右邊主要是用來指定「模組（module）或套件（package）」；不能把一般函式 `train_test_split` 當成模組來這樣匯入。

`train_test_split` 是一個**函式（function）**，不是一個 module。

原本的結構是：

```text
sklearn
└── model_selection
    └── train_test_split   ← 函式
```

因此正確方式是：

```python
from sklearn.model_selection import train_test_split
```

匯入後：

```python
train_test_split(X, y)
```

---

## 三、第 1 行如果想取別名，應該怎麼寫？

如果希望把：

```python
train_test_split
```

改成較短的名字，例如：

```python
split
```

可以這樣寫：

```python
from sklearn.model_selection import train_test_split as split
```

這才是正確的寫法。

之後就可以：

```python
X_train, X_test, y_train, y_test = split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

也就是：

```text
train_test_split
       ↓
    取別名
       ↓
      split
```

### 比較

原本：

```python
from sklearn.model_selection import train_test_split

train_test_split(X, y)
```

改成：

```python
from sklearn.model_selection import train_test_split as split

split(X, y)
```

兩者功能相同，只是函式名稱不同。

---

# 四、第 3 行可以改成這樣嗎？

原本：

```python
import tensorflow.keras.utils as np_utils
```

提問：

```python
from tensorflow.keras import utils
```

## 答案：✅ 可以

但是：

> **匯入方式改變之後，下面使用 `np_utils` 的程式也要跟著修改。**

---

# 五、原本的寫法

```python
import tensorflow.keras.utils as np_utils
```

這表示：

```text
tensorflow.keras.utils
          ↓
       取別名
          ↓
       np_utils
```

所以如果下面有：

```python
np_utils.to_categorical(y)
```

就可以直接使用。

例如：

```python
y = np.array([0, 1, 2, 1, 0])

y = np_utils.to_categorical(y)

print(y)
```

---

# 六、改成 `from tensorflow.keras import utils`

如果改成：

```python
from tensorflow.keras import utils
```

那麼下面就不能再寫：

```python
np_utils.to_categorical(y)
```

而應該改成：

```python
utils.to_categorical(y)
```

完整範例：

```python
from tensorflow.keras import utils

y = np.array([0, 1, 2, 1, 0])

y = utils.to_categorical(y)

print(y)
```

---

# 七、所以第 3 行有兩種寫法

## 寫法 A：`import ... as ...`

```python
import tensorflow.keras.utils as np_utils
```

使用：

```python
np_utils.to_categorical(y)
```

---

## 寫法 B：`from ... import ...`

```python
from tensorflow.keras import utils
```

使用：

```python
utils.to_categorical(y)
```

---

## 兩者的關係

可以想成：

```text
tensorflow.keras
       │
       └── utils
             │
             └── to_categorical()
```

### 寫法 A

```python
import tensorflow.keras.utils as np_utils
```

等於：

```text
把 utils 這個模組
        ↓
命名為 np_utils
```

所以：

```python
np_utils.to_categorical()
```

### 寫法 B

```python
from tensorflow.keras import utils
```

等於：

```text
從 tensorflow.keras
        ↓
取出 utils
        ↓
名稱仍然叫 utils
```

所以：

```python
utils.to_categorical()
```

---

# 八、如果一定要保留 `np_utils` 這個名稱呢？

也可以寫：

```python
from tensorflow.keras import utils as np_utils
```

這樣：

```python
from tensorflow.keras import utils as np_utils
```

之後仍然可以：

```python
np_utils.to_categorical(y)
```

這和：

```python
import tensorflow.keras.utils as np_utils
```

在這個使用情境下，可以得到相同的使用效果。

---

# 九、第 2 行 `import numpy as np` 呢？

原本：

```python
import numpy as np
```

這是很典型的：

```python
import 模組 as 別名
```

`numpy` 是一個 module/package，可以使用：

```python
np.array()
np.mean()
np.max()
```

---

## 如果改成 `from ... import ...`

例如：

```python
from numpy import array
```

那麼就只能直接使用：

```python
array([1, 2, 3])
```

而不是：

```python
np.array([1, 2, 3])
```

因為這時候根本沒有建立：

```python
np
```

這個名稱。

---

# 十、最重要的觀念：`import` 不能隨便取代 `from`

可以用下面這個規則理解。

## 情況 1：我要「整個模組」

使用：

```python
import numpy as np
```

使用：

```python
np.array()
np.mean()
```

---

## 情況 2：我要「模組裡面的某個函式」

使用：

```python
from sklearn.model_selection import train_test_split
```

使用：

```python
train_test_split()
```

---

## 情況 3：我要「模組裡面的某個東西」，而且想取別名

使用：

```python
from sklearn.model_selection import train_test_split as split
```

使用：

```python
split()
```

---

# 十一、三個問題放在一起比較

| 原始程式 | 可以改成？ | 說明 |
|---|---|---|
| `from sklearn.model_selection import train_test_split` | ❌ `import sklearn.model_selection.train_test_split as split` | `train_test_split` 是函式，不是 module |
| `from sklearn.model_selection import train_test_split` | ✅ `from sklearn.model_selection import train_test_split as split` | 可以替函式取別名 |
| `import numpy as np` | ✅ 可改成其他適當的 `from numpy import ...` | 但使用方式要跟著改 |
| `import tensorflow.keras.utils as np_utils` | ✅ `from tensorflow.keras import utils` | 使用時改成 `utils.xxx()` |
| `import tensorflow.keras.utils as np_utils` | ✅ `from tensorflow.keras import utils as np_utils` | 使用時仍可 `np_utils.xxx()` |

---

# 十二、以你的程式來看，推薦的兩種寫法

## 寫法 A：維持原本程式

```python
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow.keras.utils as np_utils
```

下面：

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

x = np.array([1, 2, 3])

y = np_utils.to_categorical(y)
```

---

## 寫法 B：自己取比較短的名稱

```python
from sklearn.model_selection import train_test_split as split
import numpy as np
from tensorflow.keras import utils
```

下面就要配合修改：

```python
X_train, X_test, y_train, y_test = split(
    X, y, test_size=0.2
)

x = np.array([1, 2, 3])

y = utils.to_categorical(y)
```

---

# 十三、最值得記住的一張圖

```text
Python 匯入
│
├── import 模組
│      │
│      └── import numpy as np
│             ↓
│          np.array()
│
└── from 模組 import 成員
       │
       ├── from sklearn.model_selection import train_test_split
       │       ↓
       │   train_test_split()
       │
       └── from sklearn.model_selection import train_test_split as split
               ↓
             split()
```

另外：

```text
tensorflow.keras
       │
       └── utils
             │
             └── to_categorical()
```

可以：

```python
import tensorflow.keras.utils as np_utils
```

使用：

```python
np_utils.to_categorical()
```

也可以：

```python
from tensorflow.keras import utils
```

使用：

```python
utils.to_categorical()
```

甚至可以：

```python
from tensorflow.keras import utils as np_utils
```

使用：

```python
np_utils.to_categorical()
```

---

# 十四、一句話記憶

> **`import` 通常是把模組匯入；`from ... import ...` 是從模組中取出指定的成員。**

而：

```python
as
```

只是：

> **「幫匯入的東西取一個別名。」**

因此：

```python
from ... import 函式 as 別名
```

是可以的：

```python
from sklearn.model_selection import train_test_split as split
```

但不能把函式硬寫成：

```python
import sklearn.model_selection.train_test_split as split
```

因為這時候 Python 會把它當成要匯入一個叫做 `train_test_split` 的模組，而不是從 `model_selection` 中取出一個函式。
