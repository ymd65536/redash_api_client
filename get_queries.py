from redash_client import base as cli
# from redash_client import data_sources as ds
from redash_client import query as qu
from redash_client import io as output
import os

if __name__ == '__main__':

    # 実行に必要な環境変数
    # ユーザーベースのトークン
    # redashのURL(ログイン時に利用するエンドポイント)
    redash_query_token = os.getenv('redash_user_token')
    redash_url = os.getenv('redash_url')

    api_client = cli.base_client(redash_query_token, redash_url)

    queies_api = qu.queries(api_client)
    queries = queies_api.get_queries(page=1, page_size=150)

    results = queries["results"]
    query_info = []
    for result in results:
        output.output_sql('sql', result=result)
        # query_info.append(queies_api.get_query_info(result["id"]))
    # print(query_info)