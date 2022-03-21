# mypage2022django
djangoを使ったホームページのリポジトリ。
# ブランチ
- main：本番環境
- トピックブランチ：実際に開発を行うブランチ。まずissueを立て、そのissueを用いて次の命名規則に従い、ブランチを切る。```issue/<issue番号>-<内容>```
# 注意点
- mainを直接編集することは避ける
- ローカルでは ```python manage.py runserver --settings=config.settings.develop```でビルドインサーバーを立てましょう。
- 本番環境で変更があったら以下のコマンドを
-- ```sudo systemctl restart gunicorn ``` 
-- ```sudo nginx -t && sudo systemctl restart nginx```
