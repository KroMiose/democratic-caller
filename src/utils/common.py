import psutil


def close_process_by_port(port):
    """
    Close the process occupying the specified port.

    Parameters:
        port (int): The port number to be closed.
    """
    for process in psutil.net_connections():
        if process.laddr.port == port:  # type: ignore
            # print(f"Closing process {process.pid} using port {port}")
            psutil.Process(process.pid).kill()
