class AddressParser:

    def number_checker(self, word):
        """
        Checks if this word is a number.
        If starting character in the word is a digit, this word is a house number.
        """
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        house_number = []
        flag = 1

        for i in range(len(word)):
            char = word[i]

            if char == " ":
                # Ignore leading/trailing whitespace.
                continue 

            if i==0 and char in digits:
                # This is a house number.
                house_number.append(char)
            elif i==0 and char not in digits:
                # This is street name.
                flag = 0
                break
            elif i>0 and flag:
                # Get the remainder of the house number
                house_number.append(char)

        house_number = "".join(house_number)
        return [flag, house_number]


    def address_parser_whitespace(self, address):
        """
        Splits given address based on whitespace delimitter or given delimitter.
        """

        words = address.split(" ")

        street_name = []
        house_number = []

        found_house_number_flag = 0
        found_house_number_delimitter = 0

        input_length = len(words)

        delimitters = ["No", "number", "Number"]

        for i in range(len(words)):
            word = words[i]


            if word in delimitters:
                # This is starting of a house number.

                if found_house_number_flag:
                    # Move this to street name.
                    street_name.append(house_number)
                    
                print(house_number)
                
                house_number_delimitter = word
                found_house_number_delimitter = 1

            elif found_house_number_flag and len(word) == 1:
                # Found a house number in previous word, current word length is 1, 
                # Hence this character should be appended to house number.
                house_number = [house_number, word]
                house_number = "".join(house_number)

            else:

                flag, parsed_house_number = self.number_checker(word)

                if flag:
                    if found_house_number_delimitter:
                        house_number = [house_number_delimitter, " ", parsed_house_number]
                        house_number = "".join(house_number)

                    else:
                        house_number = parsed_house_number
                    found_house_number_flag = 1
                else:
                    street_name.append(word)
                    if (i!= (input_length - 1)):
                        # Add a whitespace to reconstruct the street name.
                        street_name.append(" ")

        street_name = "".join(street_name)
        return [street_name, house_number]

    def address_parser_comma(self, address):
        """
        Parses given address based on comma delimitter.
        """

        a, b = address.split(',')

        street_name = []
        house_number = None

        a_flag, a_parsed_house_number = self.number_checker(a)

        b_flag, b_parsed_house_number = self.number_checker(b)

        if a_flag:
            # First word after delimitted by comma, is house number
            house_number = a_parsed_house_number
            street_name = b
        elif b_flag:
            # Second word after delimitted by comma, is house number
            house_number = b_parsed_house_number
            street_name = a

        return [street_name, house_number]

    def get_parser_output(self, input_text):
        """
        Parses the address into street name and house number.
        Disambiguates whether to split by comma or whitespace.
        Create the output JSON.
        """
        
        if ',' in input_text:
            # Let's split address into house number and street name based on ',' as delimitter
            street_name, house_number = self.address_parser_comma(input_text)
        else:
            street_name, house_number = self.address_parser_whitespace(input_text)

        print("Street name: ", street_name)
        print("House number: ", house_number)

        output_json = self.create_output_json(street_name, house_number)
        return output_json


    def create_output_json(self, street_name, house_number):
        """
        Create ouptut JSON.
        """
        output_json = {"street": street_name, "housenumber": house_number}
        return output_json


def main_run_tests(address_parser):
    """
    Run the test cases as provided.
    """
    print("----------------Test case 1---------------------")
    input_text = "Winterallee 3"
    print("Input: ", input_text)
    output_json = address_parser.get_parser_output(input_text)
    print(output_json)

    print("----------------Test case 2---------------------")
    input_text = "Musterstrasse 45"
    print("Input: ", input_text)
    output_json = address_parser.get_parser_output(input_text)
    print(output_json)

    print("----------------Test case 3---------------------")
    input_text = "Blaufeldweg 123B"
    print("Input: ", input_text)
    output_json = address_parser.get_parser_output(input_text)
    print(output_json)

    print("----------------Test case 4---------------------")
    input_text = "Am Bächle 23"
    print("Input: ", input_text)
    output_json = address_parser.get_parser_output(input_text)
    print(output_json)

    print("----------------Test case 5---------------------")
    input_text = "Auf der Vogelwiese 23 b"
    print("Input: ", input_text)
    output_json = address_parser.get_parser_output(input_text)
    print(output_json)

    print("----------------Test case 6---------------------")
    input_text = "Blaufeldweg 123B"
    print("Input: ", input_text)
    output_json = address_parser.get_parser_output(input_text)
    print(output_json)

    print("----------------Test case 7---------------------")
    input_text = "4, rue de la revolution"
    print("Input: ", input_text)
    output_json = address_parser.get_parser_output(input_text)
    print(output_json)

    print("----------------Test case 8---------------------")
    input_text = "200 Broadway Av"
    print("Input: ", input_text)
    output_json = address_parser.get_parser_output(input_text)
    print(output_json)

    print("----------------Test case 9---------------------")
    input_text = "Calle Aduana, 29"
    print("Input: ", input_text)
    output_json = address_parser.get_parser_output(input_text)
    print(output_json)

    print("----------------Test case 10---------------------")
    input_text = "Calle 39 No 1540"
    print("Input: ", input_text)
    output_json = address_parser.get_parser_output(input_text)
    print(output_json)

if __name__ == "__main__":

    address_parser = AddressParser()

    main_run_tests(address_parser)
