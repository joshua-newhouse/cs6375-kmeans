#!/bin/bash
set -x

function Usage() {
    echo -e "Run the KMeans python script using the automobile mpg data set\n"
    echo -e "./$(basename "${0}") [options]\n"
    echo -e "Options:\n\t--clusters ##  : Integer number of clusters to use; defaults to 5\n\t--help|-h  : prints this usage message\n"

}

function Main() {
    local clusters=5

    while [[ $# -gt 0 ]]; do
        local arg="${1}"
        case "${arg}" in
            --clusters)
                shift
                clusters="${1}"
                shift
                ;;
            --help|-h)
                Usage
                exit 0
                ;;
            *)
                echo "Unknown argument: ${arg}"
                Usage
                exit 0
                ;;
        esac
    done

    [[ -z "${clusters}" ]] && echo "ERROR: clusters is empty; must be an integer value" && exit 1

    curl "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data" > auto-mpg.data
    datFileAbsPath="$(pwd)/auto-mpg.data"

    python3 src/main.py "${datFileAbsPath}" "${clusters}" 1000
}

Main "$@"
