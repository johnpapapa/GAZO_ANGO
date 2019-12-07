画像暗号

開発環境
macOS HighSierra version:10.13.6 
Python3.7.0
openCV 4.0.0.21
opencv-contrib-python 4.1.2.30
numpy 1.17.4
Pillow 6.2.1

[ 概要 ]
画像処理のお勉強も兼ねたプログラム。
動作は画像を切り貼りしている程度なので、ごく単純なアルゴリズムである。
目標としては暗号化したファイルのサイズが現状元のファイルの二倍なので、暗号化・復号化した画像データのサイズの縮小。
また、今回sharefileという暗号化したファイルの個数が二個であるが、可変数にもしてみたい。
最後にopenCVとPillowの偉大さに感謝した。

[ 使い方 ]
※動作させる際に環境によってはnumpyとopenCVとPillowのパッケージをインストールする必要がある。

**暗号化の場合**
	暗号化したい画像を用意し、コマンドライン引数に指定し、実行
	```
	$python3 image_encoder.py filename
	```
	
		filenameが"secret.png"の場合には
	```
	$python3 image_encoder.py secret.png
	```
	
	出力される"share1.png", "share2.png"が暗号化された画像。
	
**復号化の場合**	
	復号化したい画像を二枚用意し、コマンドライン引数に指定し、実行
	```
	$python3 image_encoder.py filename1 filename2
	```
	
		filename1が"share1.png"と、filename2が"share2.png"の場合には、
	```
	$python3 image_encoder.py secret.png
	```
	
	出力される"DecryptImage.png"が復号化された画像。
	