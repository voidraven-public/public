# hello_world.py
def get_hello_world_message():
    """
    Returns a simple hello world message.
    
    Returns:
        str: A greeting message
    """
    return "Hello, World!"

def print_hello_world():
    """
    Prints the hello world message to the console.
    """
    print(get_hello_world_message())

if __name__ == "__main__":
    print_hello_world()