from snakemake.shell import shell

from utils import *


def main():
    try:
        shell_command = f"""
        checkm lineage_wf --tab_table --nt --pplacer_threads {threads} \
        -t {threads} -x {params.ftype} {params.basename} {params.out} 2> >(tee -a {log} >&2) 1> >(tee -a {log} >&1)
        """
        main_logger.info(f"Shell command for rule checkm_lineage_wf:\n{shell_command}")
        shell_command = cmd_with_error_report(shell_command)
        shell(shell_command)
    except Exception as e:
        rules_error_logger.error(
            f"Error in rule checkm_lineage_wf: {e}\ninputs: {snakemake_input}"
        )
        raise e


if __name__ == "__main__":
    main()
