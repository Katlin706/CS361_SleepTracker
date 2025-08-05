import zmq
import time

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:9999")

sent_message = '{"date":"2025-07-01", "duration":7}'
socket.send_string(sent_message)
time.sleep(10)
message = socket.recv().decode()
print(f"{message}")

sent_message = '{"date":"2025-07-01", "duration":6}'
socket.send_string(sent_message)
time.sleep(10)
message = socket.recv().decode()
print(f"{message}")

sent_message = '{"date":"2025-07-01", "duration":5}'
socket.send_string(sent_message)
time.sleep(10)
message = socket.recv().decode()
print(f"{message}")

sent_message = '{"date":"2025-07-02", "duration":1}'
socket.send_string(sent_message)
time.sleep(10)
message = socket.recv().decode()
print(f"{message}")

socket.send_string('{"days_requested":2}')
time.sleep(10)
message = socket.recv().decode()
print(f"{message}")

time.sleep(10)
socket.send_string("confirm delete_all sleep entries")
message = socket.recv().decode()
print(f"{message}")


socket.send_string('Q')

