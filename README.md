cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=../venv ../raplcap/
make
make install
gcc -o rrr rrr.c -I./venv/include/raplcap -L./venv/lib -lraplcap-msr -Wl,-rpath,./venv/lib -std=c99

https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-vol-3b-part-2-manual.pdf

https://github.com/powercap/raplcap

https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_num