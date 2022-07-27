import socket, pickle
from ulab import numpy as np

HOST = 'localhost'
PORT = 8080
# # Create a socket connection.

with open('/Users/leangsiv/Desktop/ulab/micropython/ports/unix/testing_file/publisher-consumer/greener_comfort_co2_10min.csv', 'r') as file:
    lists = []
    max_value = 0
    i = 0
    for line in file:
        if (i == 0):
            i += 1
            continue
        elif i == 6: 
            # Sending the lists to consumer with i = 6 which mean 5 rows are sending to consumer
            # Otherwise, without sending to consumer -> Maximun 222 data only
            break
        data = [x for x in line.strip().split(',')]
        room = 1 # Reset the room number for new line
        for index in range (2,len(data)):
            lists.append([room, int(float(data[index]))])
            room += 1
        # Create a socket connection.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        data_string = pickle.dumps(lists)

        # data_string = "exit" # If we want to stop publishing

        s.send(data_string)
        s.close()
        lists.clear() # Clear items
        i += 1
# print(lists)

# TODO: - The data that can be sent is only 183 points
# Pickle the object and send it to the server
# data_string = pickle.dumps(lists)
# s.send(data_string)

# s.close()