# PACKAGE = stltest-0.1.0

setup:
	# パッケージファイル作成
	poetry build
	# ファイルの解凍
	tar zxvf dist/$(PACKAGE).tar.gz -C ./dist
	# setup.pyのコピー
	cp dist/$(PACKAGE)/setup.py setup.py
	# 解凍したフォルダの削除
	rm -rf dist/$(PACKAGE)/