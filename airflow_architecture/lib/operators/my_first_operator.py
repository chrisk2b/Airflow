from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import logging as log


class MyFirstOperator(BaseOperator):

    @apply_defaults
    def __init__(self, param, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.param = param

    def execute(self, context):
        task_instance = context['task_instance']
        minute = task_instance.xcom_pull('task_id2', key='minute')
        log.info(minute)
        log.info(self.param)

class CustomDummyOperator(BaseOperator):

    @apply_defaults
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, context):
        print('Hello from a custom operator')
