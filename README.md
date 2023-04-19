# simple-cmd-chat-application
The command line chat application using [P2P](https://github.com/DRS975/p2p-Architecture/blob/main/p2ptxt.txt). architecture works by creating a direct socket connection between two nodes on the same network.

Each node runs an instance of the chat application that listens on a specific port for incoming connections. When a node wants to initiate a chat with another node, it provides the IP address and port number of the listening chat application instance of the other node.

The nodes exchange messages over the socket connection, which is secured using end-to-end encryption. The encryption keys are generated using the [Diffie-Hellman](https://github.com/DRS975/Diffie-Hellman).key exchange algorithm, which allows the nodes to negotiate a shared secret key over an insecure channel.

The chat application implements full-duplex communication, which means that both nodes can send and receive messages at the same time. The chat application is also designed to handle concurrent connections, which allows multiple chat sessions to be established simultaneously.

The implementation is programmed in Python using the socket and cryptography modules for socket communication and encryption, respectively

HOW TO USE#########################################################################
TYPE AND RUN IN CMD:pip install argparse cryptography
SAVE CODE DRSCHAT.PY
TYPE AND ENTER: pyinstaller --onefile DRSCHAT.py
