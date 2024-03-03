import pyautogui as ag
import time
import pytesseract
import pyperclip
import numpy
import datetime

#各座標を辞書型変数に格納する
pos_kindle={"x":692,"y":846}
pos_deepl_clear={"x":1835,"y":174}
pos_deepl_copy={"x":2414,"y":1398}
pos_ocr_topleft={"x":359,"y":162}#{"x":120,"y":183}
pos_ocr_bottomright={"x":965,"y":1509}#{"x":1200,"y":1503}

#ocr領域の幅と高さを求め、変数に格納する
ocr_area_width=pos_ocr_bottomright["x"]-pos_ocr_topleft["x"]
ocr_area_height=pos_ocr_bottomright["y"]-pos_ocr_topleft["y"]

#翻訳結果を格納するためのからのリストを作成
translation_result=[]

for i in range(7):
    img=ag.screenshot(region=(pos_ocr_topleft["x"],pos_ocr_topleft["y"],ocr_area_width,ocr_area_height))#PIL画像として取得
    img_gray=img.convert("L") #Lはグレースケール 
    img_cv_gray=numpy.array(img_gray)#PIL(Python Imaging Library)からOpenCVで処理できる形式に変換
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\1612h\Tesseract-OCR\tesseract.exe"
    result=pytesseract.image_to_string(img_cv_gray,lang="jpn")#OCRを実行して、テキストを抽出 言語を指定しないと英語として認識される　数字の場合は英語のままで問題ない
    pyperclip.copy(result)#クリップボードにコピー
    ag.click(pos_deepl_clear["x"],pos_deepl_clear["y"],clicks=1)#Deeplのクリアボタンをクリック
    ag.hotkey("ctrl","v")#クリップボードのテキストを貼り付け
    time.sleep(1.5)#翻訳が完了するまで待つ
    ag.click(pos_deepl_copy["x"],pos_deepl_copy["y"],clicks=1)#翻訳結果をコピー
    translation_result.append(pyperclip.paste())#翻訳結果をリストに追加

    ag.click(pos_kindle["x"],pos_kindle["y"],clicks=1)#Kindleをアクティブ化
    ag.hotkey("pagedown")#次のページに移動

#翻訳結果リストをテキストファイルに書き込む
try:
    with open("translation_result.txt",encoding="utf-8",mode="x") as f: #mode="x"はファイルが存在しない場合のみ書き込む wは上書き
        f.writelines(translation_result) #witelinesはリストを書きこむ
except FileExistsError:
    newfilename = str(datetime.date.today()) + "_translation_result.txt"
    with open(newfilename,mode="x") as f:
        f.writelines(translation_result)
    ag.alert("ファイルが存在しています。"+newfilename+"として保存しました。")
