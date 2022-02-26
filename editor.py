class Markdown:
    commands = {'help': '!help', 'exit': '!done'}
    messages = {'text': 'Text: ', 'label': 'Label: ', 'level': 'Level: ', 'url': 'URL: ', 'rows': 'Number of rows: '}
    errors = {'level': 'The level should be within the range of 1 to 6', 'rows': 'The number of rows should be greater than zero'}

    def __init__(self):
        self.formatters = {'plain': self.plain, 'bold': self.bold, 'italic': self.italic, 'inline-code': self.inline_code,
                           'link': self.link, 'header': self.header, 'new-line': self.new_line, 'ordered-list': self.lists,
                           'unordered-list': self.unordered_list}
        self.text = []

    @staticmethod
    def new_line():
        return '\n'

    def plain(self):
        return input(self.messages['text'])

    def bold(self):
        return f'**{input(self.messages["text"])}**'

    def italic(self):
        return f'*{input(self.messages["text"])}*'

    def inline_code(self):
        return f'`{input(self.messages["text"])}`'

    def link(self):
        return f'[{input(self.messages["label"])}]({input(self.messages["url"])})'

    def header(self):
        while True:
            level = input(self.messages["level"])
            if level.isdigit() and int(level) in range(1, 7):
                return int(level) * '#' + ' ' + input(self.messages["text"]) + '\n'
            else:
                print(self.errors['level'])

    def lists(self, ordered=True):
        output = []
        while True:
            rows = input(self.messages['rows'])
            if rows.isdigit() and int(rows) != 0:
                for i in range(1, int(rows) + 1):
                    output.append(f'{str(i) + ". " if ordered else  "* "}' + input(f'Row #{i}: ') + '\n')
                return ''.join(output)
            else:
                print(self.errors['rows'])

    def unordered_list(self):
        return self.lists(False)

    @staticmethod
    def save(inp):
        with open('output.md', 'w') as file:
            file.write(inp)

    def help(self):
        print('Available formatters:', *self.formatters)
        print('Special commands:', *self.commands.values())

    def main(self):
        while True:
            if self.text:
                print(*self.text, sep='')
            inp = input('Choose a formatter: ')
            if inp == self.commands['exit']:
                self.save(''.join(self.text))
                break
            elif inp == self.commands['help']:
                self.help()
            elif inp in self.formatters:
                self.text.append(self.formatters[inp]())
            else:
                print('Unknown formatting type or command')


run = Markdown()
run.main()
