#!/usr/bin/bash
project_dir=$(pwd)
echo "-------Installing Appower-------"
echo "-------Installing system dependencies-------"
sudo apt install python3 cmake gcc
# Check if the script is sourced, and if yes, activate the virtual environment
if [ "$_" = "$0" ]; then
    echo "Please run this script using 'source' or '.' to activate the virtual environment."
    echo "Usage: source install.sh"
else

    echo "-------Creating virtual environment-------"
    python3 -m venv "$project_dir/.venv"
    echo "-------Activating virtual environment-------"
    # shellcheck source="$project_dir/.venv/bin/activate"
    source "$project_dir/.venv/bin/activate"
    echo "-------Installinng python dependencies-------"
    pip install psutil
    echo "-------Building raplcap-------"
    mkdir "$project_dir/raplcap/build"
    cd "$project_dir/raplcap/build"
    cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="$project_dir/.venv" "$project_dir/raplcap"
    make install
    make
    cd "$project_dir"
    echo "-------Compiling C program for getting energy metrics-------"
    gcc -o energy energy.c -I./.venv/include/raplcap -L./.venv/lib -lraplcap-msr -Wl,-rpath,./.venv/lib -std=c99
    echo "-------Appower installation complete-------"
fi



