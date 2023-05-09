# HoYoLab每日自動簽到 + Telegram簽到結果回報機器人
* **將telegrram_bot部屬至fly.io，並於簽到完成後回傳結果**
* **適用於多帳號自動簽到**
* **可回傳簽到結果至多個telegram帳號**
* **可自訂簽到時間(hsr_sign.py檔)**

### 1.Cookie獲取方式(以Chrome為例)
1. 打開Chrome瀏覽器至首頁並登入
https://www.hoyolab.com/home
2. 按下 F12 或是 右鍵>檢查 開啟開發者工具
3. 開發者工具最上方欄位切換到 NetWork (網路)，中間欄位選擇 All 並且按下重新整理
4. Name(名稱) 最上面找一下 home ，點選後往下滑至 Request Header (要求標頭)， cookie 就在裡面請全部複製下來貼至 fly.toml 檔案中對應位置
5. ![image](https://github.com/Pikao777/hsr_auto_sign/blob/main/md_photo/cookie_01.jpg)

### 2.Telegram_bot設置
1. 搜尋BotFather(有藍勾勾的)並加入好友
2. 創建機器人，輸入 /newbot
3. 幫機器人取名(名稱最後需要加上bot)
4. 完成後會獲得一組API token，請複製下來貼至 fly.toml 檔案中對應位置
5. 加入自己的機器人為好友
6. 獲取自己的 CHAT_ID： https://api.telegram.org/bot【你的token】/getUpdates ，請複製下來貼至 fly.toml 檔案中對應位置以利機器人將簽到成功的結果回傳至你的聊天室

### 3.fly.io免費方案-部屬(Windows版)
1. 打開終端機(CMD)至該資料夾位址

    ```
    # 假設存放在下載資料夾，username請更換為電腦的使用者名稱
    cd C:/Users/username/Downloads/hsr_auto_sign
    ```
2. 終端機輸入以下指令，安裝flyctl至Windows

    ```
    iwr https://fly.io/install.ps1 -useb | iex
    ```
3. 註冊帳號

    ```
    flyctl auth signup
    ```
4. 登入帳號

    ```
    flyctl auth login
    ```
5. 開啟專案，可參考下列選項

    ```
    flyctl launch
    # Overwrite(Yes)
    # Choose an app name(輸入你想設定的app名稱)
    # 選擇地區(可以選擇離自己較近的地點作為伺服器位置)
    # database相關(No)
    ```
6. 部屬

    ```
    flyctl deploy
    ```
