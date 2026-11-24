from snakemake.shell import shell

from utils import *


def main():
    try:
        shell_command = f"""
        checkm coding_plot --image_type pdf  -x {params.ftype} {params.mag_qa} {params.mag} {params.out} 95 || true
        checkm marker_plot --image_type pdf  -x {params.ftype} --dpi 400 {params.mag_qa} {params.mag} {params.out} || true
        checkm nx_plot --image_type pdf  -x {params.ftype} {params.mag} {params.out} || true
        touch {output}
        """
        main_logger.info(f"Shell command for rule checkm_plots:\n{shell_command}")
        shell_command = cmd_with_error_report(shell_command)
        shell(shell_command)
    except Exception as e:
        rules_error_logger.error(
            f"Error in rule checkm_plots: {e}\ninputs: {snakemake_input}"
        )
        raise e


if __name__ == "__main__":
    main()
