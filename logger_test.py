from logger import Logger

logger = Logger("test_log.txt")
assert logger.file_name == "test_log.txt"

logger.write_metadata(100, 0.5, "Fake Disease", 0.5, 0.5)
logger.log_infection_survival(10, 10, 80, 10, 10, 10)
logger.log_interactions(10, 10, 10)
logger.log_time_step(10)
logger.final(10, 80, 10, "All the people died")
