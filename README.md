# streamlit_windows_desktop_app_sample

StreamlitのアプリをWindowsのデスクトップアプリとしてexe化する方法のサンプル

ビルドで生成されるdistフォルダなどはすべて削除する。

ビルドで生成されるexeファイルをダブルクリックすることで、Streamlitのアプリが起動。


## 前提

- Windows環境下


## ビルド方法

このREADME.mdが存在するディレクトリをカレントディレクトリとして以下のコマンドを実行

```
build_exe.bat
```


## 開発について

このリポジトリを起動するための最小限の環境構築
（condaを使用）

```
conda create -n streamlit_dev python=3.11 --no-default-packages

conda activate streamlit_dev

pip install -r requirements.txt

```

開発環境の実行
```
python dev_run.py
```

## 特徴
- WebアプリのためのStreamlitをデスクトップアプリ化
- exe化することで、Python環境がなくても実行可能
- 単一ファイルのexe化
- .streamlit/config.tomlを使用して、アプリの設定を変更可能
- ビルド後に余計なファイルを削除し、exeファイルのみを残す
- exe化したアプリをダブルクリックすることで、Streamlitのアプリが起動
- exe化したアプリはあたかもWindowsのアプリのように
- 自作モジュールも実装可能
- Streamlitのカスタムコンポーネントも実装可能
