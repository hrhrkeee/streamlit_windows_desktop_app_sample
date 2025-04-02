@echo off

cd app

@REM ビルド後のexeのファイル名を指定
set app_name="desktop_app_sample"

@REM REM config.tomlの [theme] を読み込み
for /f "delims=" %%i in ('python -c "import toml; cfg = toml.load(r'..\.streamlit\config.toml'); theme = cfg.get('theme', {}); print(' '.join([f'--theme.{k}={v}' for k,v in theme.items()]))"') do set STREAMLIT_OPTS=%%i

@REM @REM streamlit-desktop-appでexe化
streamlit-desktop-app build main.py ^
    --name "%app_name%.exe" ^
    --icon "./assets/app_icon.ico" ^
    --streamlit-options %STREAMLIT_OPTS% ^
    --pyinstaller-options ^
    --onefile ^
    --noconfirm ^
    --add-data util:util ^
    --add-data data:data ^
    --hidden-import streamlit_image_comparison ^
    --noconsole 

@REM dist/%app_name%.exeを親ディレクトリに移動
move dist\%app_name%.exe ..

@REM distフォルダを削除
rmdir /s /q dist
@REM buildフォルダを削除
rmdir /s /q build
@REM specファイルを削除
del /q *.spec

cd ..
