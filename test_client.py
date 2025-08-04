import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:9999")

sent_message = '{"duration":8, "date":"2025-07-01"}'
print(f"Sending the request from the client: {sent_message}")
socket.send_string(sent_message)
message = socket.recv().decode()
print(f"{message}")

socket.send_string('{"days_requested":7}')
message = socket.recv().decode()
print(f"{message}")


socket.send_string('Q')

