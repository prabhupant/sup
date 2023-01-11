import argparse


class CustomArgparseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, ' '.join(values))


parser = argparse.ArgumentParser()

parser.add_argument("--add", help="Add a new comamnd to sup", nargs='+', action=CustomArgparseAction)
parser.add_argument("--list", help="List all commands")
parser.add_argument("--search", help="Search for a command", nargs='+', action=CustomArgparseAction)
parser.add_argument("--description", help="Description for the command", nargs='+', action=CustomArgparseAction)


args = parser.parse_args()



class Sup:

    def __init__(self, command, description, search_text):
        self.command = command
        self.description = description
        self.search_text = search_text
        self.memory = {}


    def search(self, text):
        pass


    def add_command(self):
        self.brain[self.command] = self.description


    def delete_command(self):
        pass


    def edit_command(self):
        pass


    def list_all_commands(self):
        pass


    def sync_with_git(self):
        pass


def verify_cli_arguments(args):
    arg_add = args.add
    arg_list = args.list
    arg_search = args.search
    arg_description = args.description

    if arg_add and not arg_description:
        raise Exception("Can't add command without description")
    if not arg_add and arg_description:
        raise Exception("You drunk or what?")

    print(args)


if __name__ == '__main__':
    verify_cli_arguments(args)

    
    


        
