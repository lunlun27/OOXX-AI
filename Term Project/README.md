# Tic-tac-toe AI: A Python play tic-tac-toe with you

## (1) 程式的功能 Features

Tic-tac-toe AI provides the following functionalities:

- **製造棋盤**: 用簡單的符號與換行製造出棋盤
- **自動對戰**: 只需要在自己的回合輸入自己要下的旗子，AI就能自動與您對戰

## (2) 使用方式 Usage

1.啟動程式後，系統會製造出一個棋盤，並由自己先下第一步棋。
2.每下一步棋，程式就會判斷是否有勝利條件出現，若無，則遊戲繼續，反之則公布結果。
3.若棋盤已滿，還未分出勝負，則顯示平局。

## (3) 程式的架構 Program Architecture

The project is organized as follows:
Tic-tac-toe AI/
│── create_board.py      # 定義遊戲棋盤
│── print_board.py       # 顯示棋盤
│── check_winner.py      # 檢查贏家
│── is_draw.py           # 檢查是否平局
│── minimax.py           # Minimax 演算法
├── find_best_move.py    # AI 的最佳移動
└── README.md          
## (4) 開發過程 Development Process
1.設計與規劃
OOXX遊戲是大家童年的回憶，而我想做出一個能生成棋盤，並能找到最佳下棋方法的AI來破解遊戲，也能讓大家能夠一個人與AI對戰。
2.實現基本功能
我先做出能讓兩人對戰的OOXX遊戲，其中包含判斷勝利的方法與下棋等程式。
3.實現進階功能
利用前面的程式，搭配minimax演算法，讓AI學會如何找最佳解，並能成功與人對戰。
4.測試與調適
改變棋盤樣式，並增加示當提醒，及時報告勝利。

## (5) 參考資料來源 References
1.iT邦幫忙 - (https://ithelp.ithome.com.tw/questions/10199335)提供OOXX基本邏輯
2. ChatGPT - 解釋minimax演算法並給我開源碼讓我去改。

## (6) 程式修改或增強的內容 Enhancements and Contributions
幾乎所有的內容都是我自己寫出來的，相較網路上普遍的OOXX AI，我新增了提示，勝負報告，下棋方式的調整，使整個程式運作起來很順手，介面也淺顯易懂
