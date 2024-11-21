import os
import mlflow
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the MLflow tracking URI

mlflow.set_tracking_uri("https://dagshub.com/ranitsarkar/test_exp_tracking_yt_analysis.mlflow")

# DagsHub credentials (loaded from .env file)
os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")

mlflow.set_experiment("my_experiment")
# Start an MLflow run
with mlflow.start_run():
    # Log some random parameters
    mlflow.log_param("param1", random.randint(1, 100))
    mlflow.log_param("param2", random.random())

    # Log some random metrics
    mlflow.log_metric("metric1", random.random())
    mlflow.log_metric("metric2", random.uniform(0.5, 1.5))

    print("Logged random parameters and metrics.")