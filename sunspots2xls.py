from pathlib import Path
import pandas as pd


def convert_fixedwidth_to_excel(input_path, output_path):
    # ファイルの読み込み
    lines = Path(input_path).read_text(encoding="utf-8").splitlines()
    lines = [line for line in lines if line.strip()]

    # カラム名と位置を定義（固定幅）
    header_line = lines[0]
    column_names = header_line.split()
    column_starts = [0, 6, 13, 23, 31, 39, 48, 57, 66, 75]
    column_widths = [6, 7, 10, 8, 8, 9, 9, 9, 9, None]

    # データ行を切り出し
    data_lines = lines[1:]
    records = []
    for line in data_lines:
        row = []
        for i, start in enumerate(column_starts):
            end = start + \
                column_widths[i] if column_widths[i] is not None else None
            row.append(line[start:end].strip())
        records.append(row)

    # DataFrameに変換
    df = pd.DataFrame(records, columns=column_names)
    df.replace('', None, inplace=True)

    # # DataFrameに変換して保存
    # df.to_csv(output_path, index=False)
    # print(f"CSVファイルを保存しました: {output_path}")

    # 数値変換（できる列のみ）
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # 数値化できない値は NaN に

    # Excelファイルとして保存
    df.to_excel(output_path, index=False, engine='openpyxl')
    print(f"Excelファイルを保存しました: {output_path}")


# 使用例
if __name__ == "__main__":
    convert_fixedwidth_to_excel("sunspots.txt", "sunspots_fixed.xlsx")
