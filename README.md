# data_stream_clustering
Topic: Data stream clustering on low-cost machines using Micropython

First of all, to use `micropython-ulab`, you may follow the instruction in github repository here: 
https://github.com/v923z/micropython-ulab

Then cloning this repository, we can copy folder `implemention` and paste inside directory of ulab (e.g. `ulab/micropython/ports/unix/implementation`).

In `implemention` folder, you can:
* test the concept of data stream cluster -> run file `data_stream_clustering.py`
* test publisher-consumer concept -> run file `consumer.py` first and then run `publisher.py`
* etc.

# Note:
- To run the code, you need to go to `unix` folder, and write this command line: 
`./micropython-2 file_name`

- The main algorithm was inspired from the document below:
    - [C ́erin et al., 2022] Christophe C ́erin, Keiji Kimura, and Mamadou Sow. Data stream clustering for low-cost machines. Journal of Parallel and Distributed Computing, 166:57– 70, 2022.
