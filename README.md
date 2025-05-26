# 太陽黒点相対数プロット

## Data

太陽黒点相対数は、国立天文台の[黒点相対数・黒点面積](https://solarwww.mtk.nao.ac.jp/jp/db_sunspot.html)から[月平均値](https://solarwww.mtk.nao.ac.jp/mitaka_solar/sunspots/number/mtkmonthly.txt)を使用しました。

## Read table data

オリジナルの月平均値には、観測方法変更の注釈が入っているので、それらを削除してデータのみにします。編集したデータは、`sunspots.txt`というファイル名で保存します。

```bash
wget https://solarwww.mtk.nao.ac.jp/mitaka_solar/sunspots/number/mtkmonthly.txt
awk '/^ [0-9]+[[:space:]]+[0-9]+/' mtkmonthly.txt > sunspots.txt
```

太陽黒点相対数のテーブル`sunspots.txt`は、一固定フォーマットになっているので、`sunspots2xls.py`で Excel 形式のファイルに変換します。なお、`sunspots2xls.py`を使用するには、`pandas`ライブラリーがインストールされている必要がります。

## Plot sunspots number

太陽黒点相対数の月平均値は、`R`によりプロットします。[RStudio](https://posit.co/download/rstudio-desktop/) のプロジェクトになっているので、プロジェクトファイル`sunspot.Rproj`を開きます。プロットの手順は、`sunspots.Rmd`に記載されています。
