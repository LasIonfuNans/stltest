# -*- coding: utf-8 -*-

import time
import streamlit as st


def main():
    # # Streamlit が対応している任意のオブジェクトを可視化する (ここでは文字列)
    # st.write('Hello, World!')

    # タイトル
    st.title('Application title')
    # ヘッダ
    st.header('Header')
    # 純粋なテキスト
    st.text('Some text')
    # サブレベルヘッダ
    st.subheader('Sub header')
    # マークダウンテキスト
    st.markdown('**Markdown is available **')
    # LaTeX テキスト
    st.latex(r'\bar{X} = \frac{1}{N} \sum_{n=1}^{N} x_i')
    # コードスニペット
    st.code('print(\'Hello, World!\')')
    # エラーメッセージ
    st.error('Error message')
    # 警告メッセージ
    st.warning('Warning message')
    # 情報メッセージ
    st.info('Information message')
    # 成功メッセージ
    st.success('Success message')
    # 例外の出力
    st.exception(Exception('Oops!'))
    # 辞書の出力
    d = {
        'foo': 'bar',
        'users': [
            'alice',
            'bob',
        ],
    }

    st.json(d)

    # 区切り
    st.text('------------------------------------')

    # プレースホルダーを用意する
    placeholder1 = st.empty()
    # プレースホルダーに文字列を書き込む
    placeholder1.write('Hello, World')

    placeholder2 = st.empty()
    # コンテキストマネージャとして使えば出力先をプレースホルダーにできる
    with placeholder2:
        # 複数回書き込むと上書きされる
        st.write(1)
        st.write(2)
        st.write(3)  # この場合は最後に書き込んだものだけ見える

    # 区切り
    st.text('------------------------------------')

    status_area = st.empty()

    # カウントダウン
    count_down_sec = 5
    for i in range(count_down_sec):
        # プレースホルダーに残り秒数を書き込む
        status_area.write(f'{count_down_sec - i} sec left')
        # スリープ処理を入れる
        time.sleep(1)

    # 完了したときの表示
    status_area.write('Done!')
    # 風船飛ばす
    # st.balloons()

    # 区切り
    st.text('------------------------------------')

    status_text = st.empty()
    # プログレスバー
    progress_bar = st.progress(0)

    for i in range(100):
        status_text.text(f'Progress: {i}%')
        # for ループ内でプログレスバーの状態を更新する
        progress_bar.progress(i + 1)
        time.sleep(0.1)

    status_text.text('Done!')
    st.balloons()

    # 区切り
    st.text('------------------------------------')


if __name__ == '__main__':
    main()