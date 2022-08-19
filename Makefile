# 実行例：make setup version=stltest-0.1.1

setup:
	# パッケージファイル作成
	poetry build
	# ファイルの解凍
	tar zxvf ./dist/$(version).tar.gz -C ./dist
	# setup.pyのコピー
	cp ./dist/$(version)/setup.py setup.py
	# 解凍したフォルダの削除
	rm -rf dist/$(version)/