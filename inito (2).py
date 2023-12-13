#!/usr/bin/env python
# coding: utf-8

# In[1]:


def create_directory(self, name, parent=None):
    # Create a new directory node
    return {
        "type": "directory",
        "name": name,
        "contents": {},
        "parent": parent
    }


# In[2]:


def main():
    # Create an instance of the InMemoryFileSystem
    file_system = InMemoryFileSystem()

    command_dict = {
        "mkdir": file_system.mkdir,
        "cd": file_system.cd,
        "ls": file_system.ls,
        "grep": file_system.grep,
        "cat": file_system.cat,
        "touch": file_system.touch,
        "echo": file_system.echo,
        "mv": file_system.mv,
        "cp": file_system.cp,
        "rm": file_system.rm,
    }

    while True:
        # Take user input for commands
        command = input("Enter command: ")

        # Check for the exit command
        if command == "exit":
            break
        # Check for save_state and load_state commands
        elif command.startswith("save_state"):
            _, path = command.split(" ")
            file_system.save_state(path)
        elif command.startswith("load_state"):
            _, path = command.split(" ")
            file_system.load_state(path)
        # Execute other commands using the command dictionary
        else:
            command_parts = command.split(" ")
            if command_parts[0] in command_dict:
                try:
                    command_dict[command_parts[0]](*command_parts[1:])
                except Exception as e:
                    print(f"Error: {str(e)}")
            else:
                print(f"Error: Command '{command_parts[0]}' not recognized.")

