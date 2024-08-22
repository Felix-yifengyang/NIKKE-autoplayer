参照[auto_player](https://github.com/anywhere2go/auto_player)和[NIKKE-helper](https://github.com/gdxxp/NIKKE-helper/tree/main)的仓库的大佬写的，目前版本基本还没有改动，仅做测试用。

因为是边学边做，所以写得会比较详细


## 文件夹：
- ocr: 使用ocr_main运行，与opencv无关，有单独的requirements.txt
- screen：screen_shot函数第二个argument可以引入文件名，将截图保存在screen中
- wanted：用作opencv识别

## 注意：
- OCR模式不适合NIKKE，因为很多选项不是文字而是图标
- 文件路径不要有中文
- 游戏窗口需要在前台
- 用管理员权限打开CMD来运行程序

## 修改：
- wanted的所有图片
- 按照home,base,ark,normal_activity四个函数重构
- find_touch_skewing()的distance参数

## Todo:
- 固定分辨率