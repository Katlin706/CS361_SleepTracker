import json
import zmq

failure_message = '{"status":"error"}'
success_message = '{"status":"success}'


def is_valid_json(input_string):
    try:
        json_message = json.loads(input_string)
    except ValueError as error:
        return "string"
    return "JSON"


def string_evaluation(input_string):
    if input_string == "confirm delete_all sleep entries":
        delete_all()
    else:
        socket.send_string(failure_message)


def json_evaluation(input_json):
    json_dictionary = json.loads(input_json)
    if "days_requested" in json_dictionary:
        retrieve_data(json_dictionary)
    elif "duration" in json_dictionary:
        log_data(json_dictionary)
    else:
        socket.send_string(failure_message)


def delete_all():
    with
    socket.send_string(success_message)


def retrieve_data(input_dictionary):
    socket.send_string("I got to days requested send!")


def log_data(input_dictionary):
    socket.send_string("i got here!")


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:9999")

while True:
    decoded_message = socket.recv().decode()
    if len(decoded_message) > 0:
        print(decoded_message)
        message_type = is_valid_json(decoded_message)
        if message_type == "string" and decoded_message == "Q":
            break
        elif message_type == "string":
            string_evaluation(decoded_message)
        elif message_type == "JSON":
            json_evaluation(decoded_message)
        else:
            socket.send_string(failure_message)

context.destroy()
