from src.myMLproject.config.configuration import ConfigurationManager
from src.myMLproject.components.model_evaluation import ModelEvaluation
from src.myMLproject import logger
import dagshub
import mlflow

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        dagshub.init(repo_owner='jbasurtod', repo_name='E2E_ml_flow_project', mlflow=True)

        #with mlflow.start_run():
        #    mlflow.log_param('parameter name', 'value')
        #    mlflow.log_metric('metric name', 1)
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
