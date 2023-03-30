import os
import urllib.request
import json

PYTHON_DIR_PATH = os.path.dirname(os.path.abspath(__file__))  # pyファイルが置かれているパス


# ファイルのダウンロード
def download_file(url, path):
    data = urllib.request.urlopen(url).read()
    with open(path, mode="wb") as f:
        f.write(data)


# ディレクトリを作成
def make_dir(dir_name):
    dir_path = os.path.join(PYTHON_DIR_PATH, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def download(url, file_name, path):
    if(len(url) == 0 or len(file_name) == 0 or len(path) == 0):
        return
    download_file(url, path)
    print("✅ ダウンロード完了: "+file_name+" ("+str(count+1) +
          "/"+str(len(emoji_json_value_list))+")")


# emoji.jsonを読み込む
emoji_json_path = os.path.join(PYTHON_DIR_PATH, "emoji.json")
with open(emoji_json_path, "r", encoding="utf-8") as f:
    emoji_json = json.load(f)

# 保存先ディレクトリを準備
save_dir_path = os.path.join(PYTHON_DIR_PATH, "emoji")
make_dir(save_dir_path)

style_list = emoji_json[list(emoji_json.keys())[0]]["styles"]
for style in style_list:
    dirpath = os.path.join(save_dir_path, style)
    make_dir(dirpath)

skintone_list = emoji_json["Waving hand"]["skintones"]

# 一括ダウンロード
emoji_json_value_list = emoji_json.values()
count = 0
for emoji in emoji_json_value_list:
    url = ""
    file_name = ""
    path = ""
    if("styles" in list(emoji.keys())):
        for style in style_list:
            url = str(emoji["styles"][style]).replace(" ", "%20")
            file_name = url.split("/")[-1]
            path = os.path.join(save_dir_path, style, file_name)
            download(url, file_name, path)
    if("skintones" in list(emoji.keys())):
        for style in style_list:
            for skintone in skintone_list:
                url = str(emoji["skintones"][skintone]
                          [style]).replace(" ", "%20")
                file_name = url.split("/")[-1]
                path = os.path.join(save_dir_path, style, file_name)
                download(url, file_name, path)
    count += 1

print("✅ すべてのダウンロードが完了しました")
