def process_elements(input_lst):
    while True:
        if input_lst is None or len(input_lst) <= 1:
            print("List is too short to process.")
            break

        for element in input_lst:
            if isinstance(element, (str, int)):
                if element.lower() != "stop":
                    try:
                        got_number = int(element)
                    except ValueError:
                        got_number = False
                    else:
                        if got_number > 0:
                            print("Got a positive number!")
                        elif got_number == 0:
                            print("Got zero.")
                        else:
                            print("Got a negative number.")
        break

# Use this function
input_lst = ["1", "-2", "3", "stop"]
process_elements(input_lst)
