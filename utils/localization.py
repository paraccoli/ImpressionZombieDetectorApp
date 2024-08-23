import gettext
import os
import locale
import codecs

# 言語ファイルのディレクトリを設定
localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'locales')
current_lang = 'en'  # デフォルト言語

def setup_localization():
    global _, current_lang
    try:
        # システムのデフォルト言語を取得
        system_lang, _ = locale.getdefaultlocale()
        if system_lang:
            current_lang = system_lang[:2]  # 言語コードの最初の2文字を使用
    except:
        pass  # システム言語の取得に失敗した場合はデフォルト言語を使用

    change_language(current_lang)

def change_language(lang):
    global _, current_lang
    current_lang = lang
    try:
        # UTF-8エンコーディングを明示的に指定
        with codecs.open(os.path.join(localedir, lang, 'LC_MESSAGES', 'messages.mo'), 'rb', encoding='utf-8') as file:
            translation = gettext.GNUTranslations(file)
        translation.install()
        _ = translation.gettext
    except Exception as e:
        print(f"Error changing language: {e}")
        # フォールバック: 組み込みの _ 関数を使用
        _ = gettext.gettext

setup_localization()