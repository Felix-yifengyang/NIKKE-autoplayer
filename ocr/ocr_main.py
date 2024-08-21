from ocr import PlayerOCR

# OCR文字识别 + 桌面模式
# 在屏幕上查找文字内容'挑战'或'点击屏幕继续'，找到哪个按哪个。
# 关键词's挑战'加前缀s表示只找内容严格等于'挑战'的，不加表示任意包含'挑战'的。
myplayer = PlayerOCR(accuracy=0.6)
myplayer.find_touch(['s挑战', '点击屏幕继续'])

