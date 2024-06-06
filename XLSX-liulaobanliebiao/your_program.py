import subprocess
import sys
import os
import uuid

try:
    import pandas as pd
except ImportError:
    print("pandas 未安装，正在安装...")
    subprocess.run(["pip", "install", "pandas"])
    try:
        import pandas as pd
    except:
        print("安装 pandas 失败，请手动安装后再运行程序。")
        sys.exit()

data = [
    ["佛子庄", 310],
    ["良乡", 296],
    ["常舍村", 90],
    ["陈家房", 300],
    ["二龙岗", 214],
    ["兴礼", 171],
    ["南白", 175],
    ["西班各庄", 612],
    ["石楼", 1050],
    ["南窑", 1225],
    ["大安山", 800]
]

df = pd.DataFrame(data, columns=["备注", "数量"])
df["单价"] = 60
df["金额"] = df["数量"] * df["单价"]
df.columns = ["备注", "数量", "单价", "金额"]  # 为 "单价" 和 "金额" 列指定列名

file_path = os.path.join(os.getcwd(), "output.xlsx")  # 指定文件路径
file_name = f"output_{uuid.uuid4()}.xlsx"
df.to_excel(file_path, index=False)