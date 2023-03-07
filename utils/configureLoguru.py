from loguru import logger

from sys import stderr


def configure_loguru():
	logger.remove(0)
	loggerFormat = "<green>[{time:DD-MM-YY HH:mm:ss}]</green> " + \
		"<level>{level: <8}</level> | " + \
		"<level>{message}</level>"
	logger.add(stderr, format=loggerFormat, colorize=True)
