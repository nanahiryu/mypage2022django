# mypage2022django
djangoを使ったホームページのリポジトリ。
# ブランチ
- main：本番環境
- トピックブランチ：実際に開発を行うブランチ。まずissueを立て、そのissueを用いて次の命名規則に従い、ブランチを切る。```issue/<issue番号>-<内容>```
# 注意点
- mainを直接編集することは避ける
- ローカルでは ```python manage.py runserver --settings=config.settings.develop```でビルドインサーバーを立てましょう。
- 本番環境で変更があったら以下のコマンドを
  1. ```sudo systemctl restart gunicorn ``` 
  2. ```sudo nginx -t && sudo systemctl restart nginx```
# よく使うリンク
- [DjangoをVPSにデプロイする - Just Python](https://just-python.com/use_case/django/django-deploy-vps)
- [Django+nginx+gunicornで502 BAD GATEWAY【原因解明手段まとめ】](https://zenn.dev/ryo_t/articles/71e4ee16d76274)
- [Markdown記法 チートシート](https://gist.github.com/mignonstyle/083c9e1651d7734f84c99b8cf49d57fa)
- [【Python】Django おすすめのディレクトリ構成【django 3.2対応】(Best practice for Django project directory structure) – ＋IT（プラスアイティー）](https://plus-info-tech.com/django-pj-directory-structure)
- [本サイト](https://nanahiryu.com/)
