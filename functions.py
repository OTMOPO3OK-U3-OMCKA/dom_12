import json
class JsonF:
    def __init__(self, file):
        self.file = file
        self.oper = self.load_data()


    def load_data(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            return json.load(file)


    def filter_reverse(self, text):
        list_select = []
        file = self.load_data()
        for i in file:
            if text.lower() in i["content"].lower():
                list_select.append(i)
        list_select.reverse()
        return list_select


    def add_element(self, element):
        file_list = self.load_data()
        if file_list[-1] != element:
            file_list.append(element)

        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(file_list, file, ensure_ascii=False)
