import pysrt
from googletrans import Translator
import os

def translate_and_merge_subtitles(input_file, directory):
    # 檢查並重命名原始字幕文件（如果需要）
    if input_file.endswith('_en.srt'):
        original_file = input_file.replace('_en.srt', '-origin.srt')
        new_file = input_file.replace('_en.srt', '.srt')
    else:
        original_file = input_file.replace('.srt', '-origin.srt')
        new_file = input_file

    original_file_path = os.path.join(directory, original_file)
    new_file_path = os.path.join(directory, new_file)
    input_file_path = os.path.join(directory, input_file)

    # 重命名原始檔案
    os.rename(input_file_path, original_file_path)

    # 讀取原始英文字幕
    subs = pysrt.open(original_file_path)
    translator = Translator()

    # 翻譯字幕並合併
    for sub in subs:
        translated_text = translator.translate(sub.text, dest='zh-cn').text
        sub.text = "{}\n{}".format(sub.text, translated_text)

    # 儲存合併後的字幕到新檔案
    subs.save(new_file_path, encoding='utf-8')

    return new_file, original_file

def process_all_srt_files(directory):
    for file in os.listdir(directory):
        if file.endswith(".srt"):
            new_file, original_file = translate_and_merge_subtitles(file, directory)
            print("--------")
            print(f"已處理檔案：{file}")
            print(f"合併後的字幕檔案已保存為：{new_file}")
            print(f"原始檔案重新命名為：{original_file}")
            print("--------")

# 指定檔案目錄
directory = input("請輸入檔案目錄: ")
process_all_srt_files(directory)
