import inspect
import logging
import os
from pathlib import Path

# Retrieve 'snakemake' from the main script that imported this module
snakemake = next(
    frame.frame.f_globals["snakemake"]
    for frame in inspect.stack()
    if "snakemake" in frame.frame.f_globals
)

config = snakemake.config
snakemake_input = snakemake.input
output = snakemake.output
params = snakemake.params
threads = snakemake.threads
log = snakemake.log
wildcards = snakemake.wildcards

## python loggers setup
logs_dir = Path(config["logs_dir_path"])
os.makedirs(logs_dir, exist_ok=True)
debug_logs_file_path = config["debug_logs_file_path"]

main_logger = logging.getLogger("main_logger")
main_logger.setLevel(logging.INFO)
main_logger.propagate = False
if not main_logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    main_logger.addHandler(console_handler)

rules_error_logger = logging.getLogger("rules_error_logger")
rules_error_logger.setLevel(logging.WARNING)
if not rules_error_logger.handlers:
    file_handler = logging.FileHandler(logs_dir / "rules_error_logs.log")
    file_handler.setLevel(logging.WARNING)
    rules_error_logger.addHandler(file_handler)


def cmd_with_error_report(commands):
    return f"""
    (
        {commands}
    ) 2> >(tee -a {debug_logs_file_path} >&2)
    """
