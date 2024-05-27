class DataPrinter:
    def print_screen(data):
        for d in data:
            print(d)

    def print_file(data):
        with open('output.txt', 'w', enconding = 'utf8') as file:
            for d in data:
                file.write(d)