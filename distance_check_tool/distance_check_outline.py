import pyautogui as ag
import time
import pytesseract
import pyperclip
import numpy
import cv2


#各座標を辞書型変数に格納する
pos_xl_departure={"x":1594,"y":457}
pos_xl_destination={"x":1750,"y":458}
pos_xl_checkresult={"x":2177,"y":460}

pos_map_departure={"x":401,"y":277}
pos_map_destination={"x":329,"y":338}

pos_ocr_topleft={"x":507,"y":735}
pos_ocr_bottomright={"x":552,"y":765}

#OCR領域の幅と高さを求め、変数に格納する
ocr_area_width=pos_ocr_bottomright["x"]-pos_ocr_topleft["x"]
ocr_area_height=pos_ocr_bottomright["y"]-pos_ocr_topleft["y"]


for i in range(10):
    #エクセル(出発地)
    time.sleep(0.5)
    ag.click(pos_map_departure["x"],pos_map_departure["y"],clicks=2,interval=0.5)#出発地の座標をクリック
    ag.click(pos_xl_departure["x"],pos_xl_departure["y"],clicks=2,interval=0.5)#出発地のセルをダブルクリック
    for j in range(i+1):
        ag.hotkey("down")#下矢印キーを押す
    ag.hotkey("ctrl","c")
    
    #マップ
    time.sleep(0.5)
    ag.click(pos_map_departure["x"],pos_map_departure["y"],clicks=3,interval=0.2)#出発地の座標をクリック 3クリックで全選択
    ag.hotkey("ctrl","v")

    #エクセル(目的地)
    time.sleep(0.5)
    ag.click(pos_xl_destination["x"],pos_xl_destination["y"],clicks=2,interval=0.5)#目的地のセルをダブルクリック
    for j in range(i+1):
        ag.hotkey("down")#下矢印キーを押す
    ag.hotkey("ctrl","c")

    #マップ
    time.sleep(0.5)
    ag.click(pos_map_destination["x"],pos_map_destination["y"],clicks=3,interval=0.2)#目的地の座標をクリック
    ag.hotkey("ctrl","v")

    ag.hotkey("enter")#ルート検索を実行
    time.sleep(3.5)#検索結果が表示されるまで待つ

    img=ag.screenshot(region=(pos_ocr_topleft["x"],pos_ocr_topleft["y"],ocr_area_width,ocr_area_height))#OCR領域(マップでの距離)をスクリーンショット
    # img.show()#スクリーンショットを表示
    img_gray=img.convert("L")#グレースケールに変換
    img_cv_gray=numpy.array(img_gray)#OpenCVで処理できる形式に変換
    retval,img_ocr=cv2.threshold(img_cv_gray,0,255,cv2.THRESH_OTSU)#閾値を自動で決めてくれる大津の二値化
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\1612h\Tesseract-OCR\tesseract.exe"
    result=pytesseract.image_to_string(img_ocr)#OCRを実行して、距離を抽出
    result=result.replace("\n","")#改行コードを削除
    pyperclip.copy(result)#クリップボードにコピー

    #エクセル(結果確認)
    ag.click(pos_xl_checkresult["x"],pos_xl_checkresult["y"],clicks=2,interval=0.5)#エクセルの結果確認セルをクリック
    for j in range(i+1):
        ag.hotkey("down")
    ag.hotkey("ctrl","v")

    ag.hotkey("left")#従業員申請距離のセルに移動
    ag.hotkey("ctrl","c")
    application_distance=pyperclip.paste()#クリップボードから従業員申請距離を取得

    ag.hotkey("right")#判定のセルに移動
    ag.hotkey("right")

    #従業員申請距離とマップでの距離を比較
    try:
        difference=float(application_distance)-float(result)
        if abs(difference) < float(result)*0.1: #差が10%以内ならOK abs()は絶対値を求める関数
            ag.write("OK")
        else:
            ag.write("NG")
    except:
        message=""
        pyperclip.copy(message)
        ag.hotkey("ctrl","v")