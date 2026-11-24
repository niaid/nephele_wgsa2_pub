from snakemake.shell import shell

from utils import *


def main():
    try:
        shell_command = f"""
        checkm coverage -x {params.ftype} -t {threads} {params.mag} {output} {snakemake_input.bam}
        """
        main_logger.info(f"Shell command for rule checkm_coverage:\n{shell_command}")
        shell_command = cmd_with_error_report(shell_command)
        shell(shell_command)
    except Exception as e:
        rules_error_logger.error(
            f"Error in rule checkm_coverage: {e}\ninputs: {snakemake_input}"
        )
        raise e


if __name__ == "__main__":
    main()
