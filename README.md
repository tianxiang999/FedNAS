## Deployment
PyTorch 1.4.0, MPI4Py 3.0.3 (https://pypi.org/project/mpi4py), Python 3.7.4, wandb, Anaconda 4.9.2

### Setup
1. Create environment space

> conda create --name fednas --file spec-list.txt
> conda activate fednas

2. Other packages: Wandb & torchsummaryX

> pip install --upgrade wandb; pip install torchsummaryX

3. NFS (Network File System) Configuration in your cluster

4. SSH log in without password

5. Wandb init
> wandb init $api-key

### Config MPI host file based on deployment settings (?)
Modify the hostname list in "mpi_host_file" to correspond to your actual physical network topology.
An example: Let us assume a network has a management node and four compute nodes (hostname: node1, node2, node3, node4).
If you want use node1 and node2 to run our program, the "mpi_host_file" should be:
> node1 \
> node2 \
> node3

## Experiments
Once the hardware and software environment are both ready, you can easily use the following command to run FedNAS.
Note:
1. you may find other packages are missing. Please install accordingly by "conda" or "pip".
2. Our default setting is 16 works. Please change parameters in "run_fed_nas_search.sh" based on your own physical servers and requirements.

- Homogeneous distribution (IID) experiment:
```
# search
sh run_fednas_search.sh 4 darts homo 50 5 64

# train
sh run_fednas_train.sh 4 darts homo 500 15 64
```

- Heterogeneous distribution (Non-IID) experiment:
```
# search
sh run_fednas_search.sh 4 darts hetero 50 5 64

# train
sh run_fednas_train.sh 4 darts hetero 500 15 64
```

We can also run code in a single 4 x NVIDIA RTX 2080Ti GPU server. 
In this case, we should decrease the batch size to 2 to guarantee that the total 17 processes can be loaded into the memory. 
The running script for such setting is:
```
# search
sh run_fednas_search.sh 4 darts hetero 50 5 8
```

