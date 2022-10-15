from calendar import c
import sys
import json
from json.decoder import JSONDecodeError

from utility.utils import allowed_types, number_to_words_mapper




def retrieve_data(input_file_path: str):

    try:
        with open(input_file_path) as json_file:
            try:
                json_input = json.load(json_file)

                json_data = json_input.get("message", None)
            except JSONDecodeError:
                raise JSONDecodeError(
                    "The JSON file is not properly formatted")

    except FileNotFoundError:
        raise FileNotFoundError("Specified file was not found!")

    counter = 1
    json_output = {}
    new_dict = {}

    for key, value in json_data.items():

        key_name = "key_" + number_to_words_mapper.get(counter)
        new_dict[key_name] = {  
            "type": allowed_types.get(type(value)),
            "tag": "",
            "description": "",
            "required": False, 
        }

        counter += 1
        json_output.update(new_dict)
    return json_output



def write_output_to_file(output_file_path: str, data: dict) -> bool:

    try:
        with open(output_file_path, 'w+') as result:
            result.write(json.dumps(data, indent=4))

    except Exception as e:
        raise(e)

    return True

def main() -> None:

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    if not input_file_path.endswith(".json") or not output_file_path.endswith(".json"):
        raise ValueError("input file or output file not defined properly")

    data = retrieve_data(input_file_path)
    write_output_to_file(output_file_path, data)


if __name__ == '__main__':
    main()
