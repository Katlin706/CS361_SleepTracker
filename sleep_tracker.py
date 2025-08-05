import json
import zmq

failure_message = '{"status":"error"}'
success_message = '{"status":"success"}'


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
    with open("sleep.json", "w") as file:
        pass
        socket.send_string(success_message)


def retrieve_data(input_dictionary):
    with open("sleep.json", "r+") as file:
        contents = file.read()
        if len(contents) == 0:
            socket.send_string('{"status":"error, "details":"There are no sleep logs"}')
        file.seek(0)
        sleep_list = json.load(file)
        if len(sleep_list) < input_dictionary["days_requested"]:
            socket.send_string('{"status":"error, "details":"There are not enough sleep logs"}')
        else:
            sorted_sleep = sorted(sleep_list, key=lambda item: item["date"], reverse=True)
            running_sum = 0
            running_sleep_list = []
            for night in range(0, input_dictionary["days_requested"]):
                running_sleep_list.append(sorted_sleep[night])
                running_sum += sorted_sleep[night]["duration"]
            average = running_sum / input_dictionary["days_requested"]
            socket.send_string('{"sleep_data":' + str(running_sleep_list) + ', average:' + str(average) + '}')


def log_data(input_dictionary):
    with open("sleep.json", "r+") as file:
        contents = file.read()
        if len(contents) == 0:
            json.dump([], file)
        file.seek(0)
        sleep_list = json.load(file)
        sleep_list.append(input_dictionary)
        file.truncate()
        file.seek(0)
        json.dump(sleep_list, file, indent=4)
        file.close()
    socket.send_string(success_message)


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
