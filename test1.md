# 人工智慧專案流程優化

## 1. 目標界定與績效指標
- 明確設定目標
- 設定可衡量指標（如：準確率、F1-score）
- 確認問題是否適合用 AI 解決

## 2. 資料收集（Data Collection）
- 公開資料集
- 實驗
- 感測器
- 網路

## 3. 資料前處理（Data Preprocessing）
- 清理（去除缺失值、異常值）
- 標記（如影像 segmentation）
- 特徵工程（Feature Extraction / Selection）
- 正規化 / 標準化

## 4. 模型建立（Model Development）
- 選擇合適演算法（ML / DL）
- 撰寫程式碼 / 使用框架（TensorFlow, PyTorch, Scikit-learn）

## 5. 模型訓練（Training）
- 調整超參數（Learning rate, Batch size, Epoch）
- 使用訓練集學習

## 6. 模型評估與測試（Evaluation & Testing）
- 驗證集（Validation）：超參數調整
- 測試集（Testing）：最終性能評估
- 評估指標（Precision, Recall, F1, mAP, ROC）

## 7. 部署前測試（Deployment & Stress Test）
- 壓力測試 / 系統整合測試（真實環境下穩定運行）
- 模型壓縮 / 加速（如量化、剪枝）

## 8. 正式上線（Production Deployment）
- API / App / Edge Device 部署
- 監控模型效能（MLOps，持續觀察與更新模型）