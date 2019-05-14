from flask import Flask

from src import settings
from src.controllers import clustering_controller
from src.services.clustering_impl import ClusteringImpl
from src.services.data_lake_service import QueryDataLake

application = Flask(__name__)

clustering_service = ClusteringImpl()
data_lake_service = QueryDataLake()

clustering_controller.clustering = clustering_service
clustering_controller.queryDataLake = data_lake_service

application.register_blueprint(clustering_controller.api, url_prefix="/clustering")

if __name__ == '__main__':
    application.run(settings.REST_URL, settings.REST_PORT)
