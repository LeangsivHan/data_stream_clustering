
# TODO: - Implement Queue and Consumer
import socket, pickle
from ulab import numpy as np
import uasyncio
import data_stream_clustering_concept as streaming
# import queue

# Register IP and PORT
HOST = 'localhost'
PORT = 8080

# TODO: - Using Queue
# BUFFER_SIZE = 256 
# q = queue.Queue(BUFFER_SIZE)

lists = []

# Initialize Semaphore
semaphore = uasyncio.Lock()

# Make Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(20) # Size can be change later

async def receive():

    while(True):
        conn, _ = s.accept() # Connected by addr 
        data = conn.recv(4096) # Buffer size = 4096

        # Stop receiving data
        if (data.decode("utf-8") == "exit"):
            break

        await semaphore.acquire()
        # Get the data from client
        data_variable = pickle.loads(data)

        # print(data_variable)
        # await q.put(data_variable)
        # datas = q._get()
        # print("Total length of queue: ", len(datas)) 
        # print("data = ", datas)

        #TODO: - Apply with list 
        lists.extend(data_variable)

        if len(lists) >= 148: #148 = 74 * 2
            streaming.data_stream_clustering(lists, 148, 5)
            lists.clear()

        semaphore.release()
        # conn.close()

# Run the 
uasyncio.run(receive())
# Producer-comsuner with semaphore; https://cppsecrets.com/users/120612197115104981111171149751485164103109971051084699111109/Python-Implementation-of-Producer-Consumer-Solution-using-Semaphore.php
