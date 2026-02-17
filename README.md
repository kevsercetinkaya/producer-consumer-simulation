# Producer–Consumer Synchronization Simulation
This project is a Python-based simulation of the classical Producer–Consumer problem, one of the fundamental synchronization problems in operating systems. The system is designed using semaphore-based synchronization to ensure safe and efficient access to a shared buffer between concurrent threads.

## Project Overview
In concurrent systems, multiple processes or threads often share common resources. Without proper synchronization, this can lead to race conditions, data corruption, or deadlocks. This project demonstrates how semaphores can be used to coordinate producer and consumer threads safely.

The simulation models:
- A producer thread that generates data items
- A consumer thread that processes the produced items
- A shared buffer with limited capacity
- Semaphore-based synchronization to maintain data integrity
  
## Key Features
- Multithreaded producer and consumer architecture
- Semaphore-based synchronization (mutex, full, empty)
- Prevention of buffer overflow and underflow
- FIFO (First-In, First-Out) data consistency
- Deadlock-free execution
  
## Technologies Used
- Python
- Multithreading
- Semaphore synchronization
- Operating Systems concepts

## Learning Outcomes
- Understanding of critical sections and race conditions
- Implementation of semaphore-based synchronization
- Design of concurrent systems
- Practical application of operating systems theory

## Contributors
- Kevser Çetinkaya



