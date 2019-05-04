### 使用深度學習的一些技術
#### 一、影響神經網路學習的因素
**1.更新參數的最佳化(Optimization)方法**
 - SGD
 - Momentum
 - AdaGrad
 - Adam

**2.權重參數(W)初始值的設定: 為了避免"權重變為均一值"，需設定隨機的初始值**
 
Example: 標準差為 0.01 的常態分佈

**(1) 權重參數(W)初始值對隱藏層活性化(Activation)分佈的影響 [Ref: CS231n]**

[活性化(Activation): 通過活化函數後的輸出資料]
 
a. 以 <font color="#dd0000">Sigmoid function</font> 為隱藏層的活化函數

<font color="#000066">不同權重參數(W)初始值造成的問題:</font><br /> 

(i) <font color="#dd0000">標準差為 1 的常態分佈</font>: 活性化分佈偏向 0 和 1 -> <font color="#dd0000">梯度消失(gradient vanishing)</font><br /> 

(ii) <font color="#dd0000">標準差為 0.01 的常態分佈</font>: 活性化分佈集中在 0.5 -> <font color="#dd0000">表現力受限</font><br /> 

<font color="#000066">解決方法: 各層需要有適當廣泛度的活性化分佈</font><br /> 

(i) 使用 <font color="#dd0000">Xavier 權重初始值</font>: (可以用 <font color="#dd0000">tanh</font> 取代 <font color="#dd0000">sigmoid</font> 進行改良)

假設上層節點有 n 個，使用具有 $ \frac{1}{\sqrt{n}} $ 標準差的常態分佈來初始化
    
b. 以 <font color="#dd0000">ReLU function</font> 為隱藏層的活化函數

(i) 使用 <font color="#dd0000">He 權重初始值</font>:

假設上層節點有 n 個，使用具有 $ \sqrt{\frac{2}{n}} $ 標準差的常態分佈來初始化

**(2) 強制性調整各層活性化分佈廣度的方法: <font color="#dd0000">Batch Normalization (Batch Norm)</font>**

a. <font color="#dd0000">Batch Normalization (Batch Norm) </font>的優點:
 - 可以快速學習
 - 不會過度依賴權重初始值
 - 可以控制過度學習

b. <font color="#dd0000">Batch Normalization (Batch Norm) </font>演算法: (正向傳播)

意義: 
 
    進行學習時，以小批次為單位，按照各個小批次進行資料分佈平均為 0、分散為 1 的正規化處理

正規化(Normalization)算式:

$$\mu _{B} \leftarrow \frac{1}{m}\sum_{i=1}^{m}x_{i}$$
$$\sigma  _{B}^{2} \leftarrow \frac{1}{m}\sum_{i=1}^{m}\left ( x_{i}-\mu _{B} \right )^{2}$$

$$\hat{x}_{i} \leftarrow \frac{x_{i}-\mu _{B}}{\sqrt{\sigma_{B}^{2}+\varepsilon }}$$

輸入資料為 m 個小批次的資料 B = {$x_{1}, x_{2}, ..., x_{m}$}，透過正規化(Normalization)轉換成平均為 0、分散為 1 的資料 {$\hat{x}_{1}, \hat{x}_{2}, ..., \hat{x}_{m}$}。$\varepsilon$為微小數值(Ex: 10e-7)，以避免除以零的情況。

正規化(Normalization)後的資料，再以原有的規模和移動進行轉換:

$$ y_{i}\leftarrow \gamma \hat{x}_{i}+\beta $$

參數 $\gamma$ 和 $\beta$ 由 $\gamma=1、\beta=0$ 開始進行調整至適當值。

c. <font color="#dd0000">Batch Normalization (Batch Norm) </font>層:

    可以在神經網路中插入此層(在活化函數之前或之後)來減少資料分佈的誤差

**3.超參數(Hyper-parameter)的設定: 人工設定的參數，它必須以各種數值進行測試，找出可以順利學習的結果**
 - 各層神經元數量(Input size、Hidden size、Output size)
 - 參數更新(Iteration)的次數
 - 批次(Batch)大小
 - 學習率(Learning rate)
 - 權重遞減(Weight decay)中控制正規化強度的參數 $\lambda $

**(1) 找出有效超參數的方法:**

a. 使用驗證資料(validation data)
 
註: 各種資料的用途
 
    訓練資料: 進行參數(權重、偏權值)的學習 

    驗證資料: 評估超參數的效能

    測試資料: 檢查神經網路一般化的能力

b. 執行超參數最佳化
 - 隨機取樣收尋 
 - 貝葉斯優化 (Bayesian optimization)

#### 二、解決過度學習(Overfitting)的方法
**原因:** 
  - 擁有大量參數，表現力非常好的模型
  - 訓練資料太少

**解決方法:**

**1.正規化(Normalization)**
   - 權重遞減(Weight decay): 以縮小權重參數值為目的進行學習，避免過度學習
   - Dropout: 一邊隨機消除神經元，一邊學習的手法
   
(1) 權重遞減(Weight decay)

    針對學習過程中有較大的權重部分，給與懲罰，藉此控制過度學習。

a. 種類:
- L2 norm: 對應各個權重的平方和
- L1 norm: 對應各個權重的絕對值和
- L$\infty$ norm (Max norm): 各個權重中，最大的絕對值

b. 處理方式: (以 L2 norm 為例)

- 針對全部的權重，把 $\frac{1}{2}\lambda \mathbf{W}^{2}$ 加入損失函數中，在計算梯度時將誤差反向傳播法的結果與 L2 norm 正規化的微分($\lambda\mathbf{W}$)相加

     ( $\mathbf{W}=\left \{w_{1}, w_{2}, ...,w_{n}\right \}$, $\lambda$: 控制正規化強度的超參數 )

(2) Dropout

a. 處理方式:

    神經網路訓練時，隨機選出隱藏層的神經元給予刪除，刪除後的神經元無法進行訊號傳遞。測試時，會傳遞全部神經元的訊號，但各個神經元的輸出必須乘上訓練時刪除神經元的比例再傳遞。

**2.Batch Normalization**
