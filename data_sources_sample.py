from redash_client import base as cli
from redash_client import data_sources as ds
import os


if __name__ == '__main__':

    # 実行に必要な環境変数
    # ユーザーベースのトークン
    # redashのURL(ログイン時に利用するエンドポイント)
    redash_query_token = os.getenv('redash_user_token')
    redash_url = os.getenv('redash_url')

    api_client = cli.base_client(redash_query_token, redash_url)

    ds_client = ds.data_sources(api_client)
    print(ds_client.get_data_sources())

    ds_client = ds.data_sources(api_client)
    print(ds_client.get_data_source(1))
