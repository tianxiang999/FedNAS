# hello.py
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    print("hello world from process ", rank)

if rank == 1:
    print("hello world from process ", rank)

#passRandomDraw.py
# import numpy
# from mpi4py import MPI
# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()

# randNum = numpy.zeros(1)
# rnk = -1 # EDIT

# if rank == 1:
#     randNum = numpy.random.random_sample(1)
#     print ("Process", rank, "drew the number", randNum[0])
#     comm.Send(randNum, dest=0, tag=rank) # EDIT

# if rank == 0:
#     print ("Process", rank, "before receiving has the number", randNum[0])
#     print ("Sender rank:", rnk)
#     status = MPI.Status()
#     comm.Recv(randNum, source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status) # EDIT
#     rnk = status.Get_source()
#     print ("Process", rank, "received the number", randNum[0])
#     print ("Sender rank:", rnk) # EDIT
