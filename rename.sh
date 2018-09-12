#!/bin/bash

new_project_name="${1}"
[[ -z "${new_project_name}" ]] && { echo "New project name is empty"; exit 1; }

default_project_name='inhibition_ratiobar'
project_path=$(dirname "$(readlink -f "$0")")
new_project_path=$(dirname "${project_path}")/"${new_project_name}"

echo ${project_path}
echo ${new_project_path}

grep -rl --exclude-dir=.git "${default_project_name}" "${project_path}" | xargs sed -i "s/${default_project_name}/${new_project_name}/g"

# change name of project directory  
cd $(dirname "${project_path}") || { echo "Could not change directories to project parent path"; exit 1; }
mv "${default_project_name}" "${new_project_name}"

# change name of package directory
cd "${new_project_path}" || { echo "Could not change directories to new project path"; exit 1; }
mv "${default_project_name}" "${new_project_name}"
