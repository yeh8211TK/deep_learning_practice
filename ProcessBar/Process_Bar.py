
# coding: utf-8

# In[ ]:

import sys, time

class ShowProcess():
    """
    顯示處理進度的類別
    調用該類別的相關函數可以實現處理進度的顯示
    """    
    # 初始化函數，需要知道總共的處理次數
    def __init__(self, max_steps, infoDone = 'Done'):
        # 進度條的長度
        self.max_arrow = 50
        # 總共需要處理的次數
        self.max_steps = max_steps
        # 當前的處理進度
        self.i = 0
        self.infoDone = infoDone

    # 顯示函數，根據當前的處理進度 i 顯示進度
    # 效果為[∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎]100.00%
    def show_process(self, i = None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        
        #計算顯示多少個 ' ∎ '
        num_arrow = int(self.i * self.max_arrow / self.max_steps)
        
        #計算顯示多少個 ' - '
        num_line = self.max_arrow - num_arrow 
        
        #計算完成進度，格式為 xx.xx%
        percent = self.i * 100.0 / self.max_steps 
        
        #輸出的字符串，'\r' 表示不換行回到最左邊
        process_bar = '[' + '∎' * num_arrow + '-' * num_line + ']'                      + '%.2f' % percent + '%' + '\r'
        
        #這兩句打印字符到終端
        sys.stdout.write(process_bar) 
        sys.stdout.flush()
        
        if self.i >= self.max_steps:
            self.close()

    def close(self):
        print('')
        print(self.infoDone)
        self.i = 0

