from snakemake.shell import shell

from utils import *


def main():
    try:
        shell_command = f"""
        mkdir -p {params.outDIR}

        cp {snakemake_input} {params.outDIR}/{params.inFAA}
        sed -E  's/\\*//g' {params.outDIR}/{params.inFAA} > {params.outDIR}/{params.inFAAm}  


        echo "---- Starting RGI run for {wildcards.sample} ----"
        cp -r {params.carddb} {params.outDIR}/cardDB/
        cd {params.outDIR}  && rgi load --local -i cardDB/card.json
        rgi main --input_type {params.ftype} -i {params.inFAAm} --clean --local \
                 -o {params.prefix} --data wgs --num_threads {threads} 2> >(tee -a {params.rgi_log} >&2) 1> >(tee -a {params.rgi_log} >&1)
        

        cut -f '{params.colsAA}' {params.prefix}.txt |sed -E '{params.sedhdr}' >  {params.rgi_main} 
        cut -f1  {params.prefix}.txt > {params.hmphdrs}
        seqtk subseq {params.inFAA} {params.hmphdrs} > {params.rgi_faas}
        cp {params.prefix}.txt  {params.rgi_raw} 
        
        if [[ ! -s {params.rgi_faas} ]]; then
            echo "---- FAIL: RGI found no AMR genes in sample {wildcards.sample}"
        fi

        rm -rf _tmp* localDB cardDB
        """
        main_logger.info(f"Shell command for rule run_RGI:\n{shell_command}")
        shell_command = cmd_with_error_report(shell_command)
        shell(shell_command)
    except Exception as e:
        rules_error_logger.error(
            f"Error in rule run_RGI: {e}\ninputs: {snakemake_input}"
        )
        raise e


if __name__ == "__main__":
    main()
