import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)