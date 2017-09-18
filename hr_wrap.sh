#!/usr/bin/env bash
mydir=$(dirname $(realpath $0))
set -euo pipefail
IFS=$'\n\t'
#=============================================
# FUNCTIONS
#=============================================
err() {
   echo "Error!: $*"
   exit -1
}

pbanner() {
    echo "====================================="
    echo "$*"
    echo "====================================="
}

#=============================================
# MAIN
#=============================================
test -z "${1:-""}" && {
    read url
} || {
    url="${1:-""}" 
}

${mydir}/hrdownload.py "${url}" >&2
ext=$(echo "${url}" | awk -F/ '{print $(NF -1)}')
echo ${mydir}/python/${ext}
