python pi_numpy_serial.py >> pi_numpy.log
python pi_numpy_serial_blocks.py >> pi_numpy.log

python pi_numpy_parallel_worker.py 1 >> pi_numpy.log
python pi_numpy_parallel_worker.py 2 >> pi_numpy.log
python pi_numpy_parallel_worker.py 4 >> pi_numpy.log
python pi_numpy_parallel_worker.py 8 >> pi_numpy.log

python pi_numpy_parallel_worker.py --processes 1 >> pi_numpy.log
python pi_numpy_parallel_worker.py --processes 2 >> pi_numpy.log
python pi_numpy_parallel_worker.py --processes 4 >> pi_numpy.log
python pi_numpy_parallel_worker.py --processes 8 >> pi_numpy.log