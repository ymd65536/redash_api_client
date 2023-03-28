from redash_client import base as cli
import os


if __name__ == '__main__':

    # 実行に必要な環境変数
    # ユーザーベースのトークン
    # redashのURL(ログイン時に利用するエンドポイント)
    redash_query_token = os.getenv('redash_user_token')
    redash_url = os.getenv('redash_url')

    api_client = cli.base_client(redash_query_token, redash_url)

    res = cli.base_client.get(api_client, 'data_sources')
    print(res.json())

    res = cli.base_client.get(api_client, 'data_sources/1')
    print(res.json())
