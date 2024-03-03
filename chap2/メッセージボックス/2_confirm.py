import pyautogui as ag

result=ag.confirm(text="テキストメッセージ",title="confirm関数",buttons=["OK","NO","Cancel"])
print(result)