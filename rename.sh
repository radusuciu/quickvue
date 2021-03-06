#!/bin/bash

new_project_name="${1}"
[[ -z "${new_project_name}" ]] && { echo "New project name is empty"; exit 1; }

default_project_name='quickvue'
project_path=$(dirname "$(readlink -f "$0")")

grep -rli --exclude-dir=.git "${default_project_name}" "${project_path}" | xargs sed -i "s/${default_project_name}/${new_project_name}/gI"

# change name of package directory
cd "${project_path}" || { echo "Could not change directories to project path"; exit 1; }
mv "${default_project_name}" "${new_project_name}"
