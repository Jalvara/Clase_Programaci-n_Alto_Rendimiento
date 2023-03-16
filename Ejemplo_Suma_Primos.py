import math, sys, time
import numpy as np
import pp
#Algoritmo comentado
def isprime(n):
    """Returns True if n is prime and False otherwise"""
    #La funcion isisntance determina si el primer parametro es un objeto del tipo del 
    #segundo parametro. 
    if not isinstance(n, int):
        #Esto comprende una excepción 
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True

def sum_primes(n):
    return sum([x for x in range(2,n,1) if isprime(x)])    
# tuple of all parallel python servers to connect with
ppservers = ()
print("Contenido de la funcion argv: ",sys.argv)
if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    # Creates jobserver with ncpus workers
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    # Creates jobserver with automatically detected number of workers
    job_server = pp.Server(ppservers=ppservers)
#Imprimiendo el numero de trabajadores. 
print("Starting pp with", job_server.get_ncpus(), "workers") 
# Submit a job of calulating sum_primes(100) for execution.
# sum_primes - the function
# (100,) - tuple with arguments for sum_primes
# (isprime,) - tuple with functions on which function sum_primes depends
# ("math",) - tuple with module names which must be imported before sum_primes execution
# Execution starts as soon as one of the workers will become available
job1 = job_server.submit(sum_primes, (100,), (isprime,), ("math",))
# Retrieves the result calculated by job1
# The value of job1() is the same as sum_primes(100)
# If the job has not been finished yet, execution will wait here until result is available
result = job1()
#print("Sum od primes below 100 is: ",sum_primes(100))
#print( "Sum of primes below 100 is", result)
#job_server.print_stats()
start_time = time.time()
# The following submits 8 jobs and then retrieves the results
inputs = np.random.randint(100000,200000,30)
jobs = [(input, job_server.submit(sum_primes,(input,), (isprime,), ("math",))) for input in inputs]
S=0
for input, job in jobs:
    S+=job()
print("Suma Final: ",S)    
print( "Time elapsed: ", time.time() - start_time, "s")
job_server.print_stats()
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
start_time = time.time()
print("Parte no paralela")
jobs = [sum_primes(k) for k in inputs];
print("Suma Final: ",sum(jobs))
print( "Time elapsed: ", time.time() - start_time, "s")