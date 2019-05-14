import json
import logging

from flask import Blueprint, request, Response

import src.utils.utils as utils
from src.services.clustering_service import Clustering
from src.services.data_lake_service import QueryDataLake

api = Blueprint('clustering_controller', __name__)
clustering: Clustering = None
queryDataLake: QueryDataLake = None


@api.route('/hierarchical', methods=['POST'])
def hierarchical():
    data = request.get_json() or {}

    if not data:
        logging.error("{}:{}".format("ContentLengthRequired", "Zero/No Content-Length"))
        return utils.error_response(411, "Zero/No Content-Length")

    if ['dataDesc', 'options'] != list(data.keys()) or None in [data[key] for key in data.keys()]:
        logging.error("{}:{}".format("Bad Request", "JSON Incomplete"))
        return utils.bad_request(
            "JSON incomplete. {} fields are necessary".format(['method', 'dataDesc']))

    if 'query' in data["dataDesc"]:
        return utils.bad_request("Query not implemented for hierarchical clustering method")

    df = queryDataLake.retrieve_data_as_data_frame(data["dataDesc"])
    n_clusters = data['options']['n_clusters']
    affinity = data['options']['distanceType']
    linkage = data['options']['linkage']
    message = clustering.agglomerativeClustering(n_clusters, affinity, linkage, df)
    response = {"clusters": message.tolist()}
    return Response(response=json.dumps(response, sort_keys=True, separators=(',', ':')),
                    content_type="application/json", status=200)
