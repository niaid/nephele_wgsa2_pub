from snakemake.shell import shell

from utils import *


def main():
    try:
        shell_command = f"""
        checkm qa -o 2 --tab_table -t {threads} -f {output.qa_txt} {snakemake_input} {params.mag_qa} && \
        checkm tree_qa -o 2 --tab_table -f {output.tax} {params.mag_qa}
        """
        main_logger.info(f"Shell command for rule checkm_qa:\n{shell_command}")
        shell_command = cmd_with_error_report(shell_command)
        shell(shell_command)
    except Exception as e:
        rules_error_logger.error(
            f"Error in rule checkm_qa: {e}\ninputs: {snakemake_input}"
        )
        raise e


if __name__ == "__main__":
    main()
