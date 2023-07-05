import logging
import platform
import socket

import psutil
import wmi
from prettytable import PrettyTable


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def getSystemInfo():
    try:
        general = {}
        cpu = {}
        memory = {}

        # Collecting general info
        general['System'] = platform.system()
        general['Platform'] = platform.platform()
        # general['Platform2'] = platform.uname()
        if 'window' in platform.system().lower():
            c = wmi.WMI()
            os = c.Win32_OperatingSystem()[0]
            general['Windows-Version'] = os.Caption
        else:
            general['Platform-Version'] = platform.version()
        general['Platform-Release'] = platform.release()
        # general['Platform-Version'] = platform.version()
        general['Architecture'] = platform.machine()
        general['Hostname'] = socket.gethostname()

        generalTable = PrettyTable(["", "General Information"])

        for key in general:
            generalTable.add_row([key, general[key]])

        print(generalTable)

        # Collecting CPU Info
        cpu['Processor'] = platform.processor()
        cpu['Physical_Cores'] = psutil.cpu_count(logical=False)
        cpu['Total_Cores'] = psutil.cpu_count(logical=True)
        cpufreq = psutil.cpu_freq()
        cpu['Max Frequency'] = f"{cpufreq.max}" + " Mhz"
        cpu['Min Frequency'] = f"{cpufreq.min}" + " Mhz"
        cpu['Current Frequency'] = f"{cpufreq.current}" + " Mhz"

        cpuTable = PrettyTable(["", "CPU Information"])

        for key in cpu:
            cpuTable.add_row([key, cpu[key]])

        print(cpuTable)

        # Collecting Memory Info
        mem = psutil.virtual_memory()
        memory['Total_Memory'] = get_size(mem.total)
        memory['Available_Memory'] = get_size(mem.available)
        memory['Used_Memory'] = get_size(mem.used)
        swap = psutil.swap_memory()
        memory['Total_Swap_Memory'] = get_size(swap.total)
        memory['Free_Swap_Memory'] = get_size(swap.free)
        memory['Used_Swap_Memory'] = get_size(swap.used)

        memoryTable = PrettyTable(["", "Memory Information"])

        for key in memory:
            memoryTable.add_row([key, memory[key]])

        print(memoryTable)

        # return json.dumps(general)

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    getSystemInfo()
