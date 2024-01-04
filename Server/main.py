import os
import socket
import threading
import subprocess
import psutil
import time
import datetime
import platform
def get_running_processes():
    result = subprocess.check_output(['ps', '-A']).decode('utf-8')
    return result

# Hàm để giết một tiến trình theo tên
def kill_process(process_name):
    try:
        subprocess.call(['pkill', process_name])
        return True
    except Exception as e:
        print(f"Error killing process {process_name}: {e}")
        return False

def run_speedtest(timeout=60):
    try:
        process = subprocess.Popen(['speedtest'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(timeout=timeout)
        if process.returncode == 0:
            return output
        else:
            return f"Error running speedtest: {error}"
    except subprocess.TimeoutExpired:
        process.kill()
        return "Speedtest timeout."
def list_servers(timeout=60):
    try:
        process = subprocess.Popen(['speedtest', '-L'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(timeout=timeout)
        if process.returncode == 0:
            return output
        else:
            return f"Error listing servers: {error}"
    except subprocess.TimeoutExpired:
        process.kill()
        return "List servers timeout."

def run_nmap(command):
    try:
        nmap_command = ['nmap'] + command.split()
        process = subprocess.Popen(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        if process.returncode == 0:
            return output
        else:
            return f"Error running Nmap: {error}"
    except Exception as e:
        return f"Error running Nmap: {e}"

        

def handle_request(command):
    response = ""
    if command == 'REQUEST_FILE_LIST':
		# Handle lấy danh sách file
        file_list = os.listdir()
        response = '\n'.join(file_list)
    elif command == 'get_temp':
        try :
            # Handle temperature request (replace with actual code)
            temps = psutil.sensors_temperatures()
            if temps:
                for sensor, readings in temps.items():
                    for entry in readings:
                        #print(f"{sensor}: {entry.label} - {entry.current}°C")
                        if sensor == 'k10temp' and entry.label == 'Tctl':
                            cpu_temp = entry.current
                            print(f"CPU Temperature: {cpu_temp}°C")
            else:
                print("Không có thông tin nhiệt độ.")
            #cpu_temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
            response = str(cpu_temp)
        except KeyError:
            response = "Error: Sensor nhiệt CPU không được tìm thấy"
    elif command == "get_cpu_percent" :
        cpu_percent = psutil.cpu_percent()
        response = str(cpu_percent)
    elif command == "cpu_count" :
        cpu_count = psutil.cpu_count()
        response = str(cpu_count)
    elif command == "cpu_main_core" :
        cpu_main_core = psutil.cpu_count(logical = False)
        response = str(cpu_main_core)
    elif command == "get_ram_info" :
        ram_info = psutil.virtual_memory()
        response = f"Total RAM : {ram_info.total / (1024 ** 2)} MB" + ",  " + f"Available RAM : {ram_info.available/ (1024 ** 2)} MB" 
    elif command == "get_disk_info" :
        disk_info = psutil.disk_usage('/')
        response = f"Total DiskSpace : {disk_info.total / (1024 ** 2)} MB" + ",  " + f"Used DiskSpace : {disk_info.used/ (1024 ** 2)} MB" 
    elif command == 'shutdown':
        # Handle shutdown request
        subprocess.run(['sudo', 'shutdown', '-h', 'now'])
        response = "Shutdown command sent"
    elif command == 'reboot':
        # Handle reboot request
        subprocess.run(['sudo', 'reboot'])
        response = "Reboot command sent"
    elif command == "get_process_list":
        try:
            processes = []
            for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
                processes.append({
                'pid': process.info['pid'],
                'name': process.info['name'],
                'cpu_percent': process.info['cpu_percent'],
                'memory_info': process.info['memory_info'].rss / (1024 * 1024)  # Convert to MB
                })
                response = str(processes)
        except Exception as e:
            response = f"Error getting process list: {e}"
    elif command == "get_network_info":
        try:
            network_info = psutil.net_io_counters()
            response = f"Bytes Sent: {network_info.bytes_sent} bytes, Bytes Received: {network_info.bytes_recv} bytes"
        except Exception as e:
            response = f"Error getting network info: {e}"
    elif command == "get_os_info":
            try:
                os_info = {
                    'system': os.uname().sysname,
                    'node_name': os.uname().nodename,
                    'release': os.uname().release,
                    'version': os.uname().version,
                    'machine': os.uname().machine
                }
                response = str(os_info)
            except Exception as e:
                response = f"Error getting OS info: {e}"
    elif command == "get_system_info":
            try:
                system_info = {
                    'platform': platform.system(),
                    'processor': platform.processor(),
                    'architecture': platform.architecture(),
                    'python_version': platform.python_version()
                }
                response = str(system_info)
            except Exception as e:
                response = f"Error getting system info: {e}"
    elif command == "get_time":
    	response = datetime.datetime.now().strftime("%I:%M:%S %p")
    elif command == "get_date":
    	response = datetime.datetime.now().strftime("%d-%m-%Y")
    elif command == "get_network_connections":
            try:
                connections = psutil.net_connections()
                connection_info = []
                for conn in connections:
                    connection_info.append({
                        'fd': conn.fd,
                        'family': conn.family,
                        'type': conn.type,
                        'laddr': conn.laddr,
                        'raddr': conn.raddr,
                        'status': conn.status,
                        'pid': conn.pid
                    })
                response = str(connection_info)
            except Exception as e:
                response = f"Error getting network connections: {e}"
    elif command == "get_device_info":
            try:
                device_info = {
                    'device_name': platform.node(),
                    'system_version': platform.system() + ' ' + platform.version()
                }
                response = str(device_info)
            except Exception as e:
                response = f"Error getting device info: {e}"
    elif command == "get_memory_info":
            try:
                virtual_memory = psutil.virtual_memory()
                swap_memory = psutil.swap_memory()
                response = (
                    f"Total RAM: {virtual_memory.total / (1024 * 1024)} MB, "
                    f"Available RAM: {virtual_memory.available / (1024 * 1024)} MB, "
                    f"Used RAM: {virtual_memory.used / (1024 * 1024)} MB\n"
                    f"Total Swap: {swap_memory.total / (1024 * 1024)} MB, "
                    f"Used Swap: {swap_memory.used / (1024 * 1024)} MB"
                )
            except Exception as e:
                response = f"Error getting disk info: {e}"
    elif command == 'check':
        # Xử lý lệnh "check"
        response = run_speedtest()
    elif command == 'list_servers':
        # Xử lý lệnh "list_servers"
        response = list_servers()
    elif command == "get_disk_usage":
            try:
                disk_partitions = psutil.disk_partitions()
                disk_info = []
                for partition in disk_partitions:
                    usage = psutil.disk_usage(partition.mountpoint)
                    disk_info.append({
                    	'device' : partition.device,
                        'total': usage.total / (1024 * 1024),  # Convert to MB
                        'used': usage.used / (1024 * 1024),  # Convert to MB
                        'free': usage.free / (1024 * 1024),  # Convert to MB
                        'percent': usage.percent
                    })
                response = str(disk_info)
            except Exception as e:
                response = f"Error getting disk usage: {e}"
                
    elif command == 'list':
        # Gửi danh sách các tiến trình đang chạy
        processes = get_running_processes()
        response = processes
    elif command.startswith('kill'):
        # Tách tên tiến trình cần giết từ lệnh 'kill'
        _, process_name = command.split(' ', 1)

        # Giết tiến trình và gửi kết quả về client
        success = kill_process(process_name)
        if success:
            response = "Process killed successfully."
        else:
            response = "Error killing process."
    elif command.startswith('nmap'):
        # Tách lệnh Nmap từ command
        _, nmap_command = command.split(' ', 1)
        # Chạy lệnh Nmap và gửi kết quả về client
        response = run_nmap(nmap_command)
    else:
        response = "Invalid command."

    return response

def handle_client(client_socket, client_address):
    try:
        print(f"Accepted connection from {client_address}")

        data = client_socket.recv(1024).decode('utf-8')

        response = handle_request(data)

        client_socket.send(response.encode())
    except Exception as e:
        print(f"Error handling connection: {e}")
    finally:
        client_socket.close()


def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            local_ip = s.getsockname()[0]
        return local_ip
    except Exception as e:
        print(f"Error getting local IP: {e}")

def start_server():
    SERVER_HOST = get_local_ip()
    SERVER_PORT = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()


if __name__ == "__main__":
    start_server()
