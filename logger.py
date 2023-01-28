import logging


my_logg = logging.getLogger('my_logg')
my_logg.setLevel(logging.INFO)
my_logg_handler = logging.FileHandler('log.txt')
log_formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
my_logg_handler.setFormatter(log_formatter)
my_logg.addHandler(my_logg_handler)
