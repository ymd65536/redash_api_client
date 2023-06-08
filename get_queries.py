from redash_client import base as cli
# from redash_client import data_sources as ds
from redash_client import query as qu
import os


if __name__ == '__main__':

    # 実行に必要な環境変数
    # ユーザーベースのトークン
    # redashのURL(ログイン時に利用するエンドポイント)
    redash_query_token = os.getenv('redash_user_token')
    redash_url = os.getenv('redash_url')

    api_client = cli.base_client(redash_query_token, redash_url)

    queies_api = qu.queries(api_client)
    queries = queies_api.get_queries()

    # for query in queries:
    #    print(query)

    results = queries["results"]

    for result in results:
        print(result["id"])
