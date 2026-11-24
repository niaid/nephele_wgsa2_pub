from snakemake.shell import shell

from utils import *


def main():
    try:
        shell_command = f"""
        checkm profile -q {snakemake_input} --tab_table -f {output}
        """
        main_logger.info(f"Shell command for rule checkm_profile:\n{shell_command}")
        shell_command = cmd_with_error_report(shell_command)
        shell(shell_command)
    except Exception as e:
        rules_error_logger.error(
            f"Error in rule checkm_profile: {e}\ninputs: {snakemake_input}"
        )
        raise e


if __name__ == "__main__":
    main()
