from time import sleep
from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("This task is async.")
    sleep(5)
    logger.info("async setelah 5 detik tidak blocking views")
    sleep(3)
    logger.info("async setelah 8 detik tidak blocking views")
