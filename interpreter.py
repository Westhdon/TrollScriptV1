from cmds import *

with open("myscript.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split(" ", 1)  # command + arguments
    command = parts[0]
    args = parts[1] if len(parts) > 1 else ""

    if command == "move_mouse_random":
        move_mouse_random()

    elif command == "open_browser":
        open_browser(args)

    elif command == "sleep":
        sleep(args)

    elif command == "message":
        parts = args.split(" ", 1)  # split args into 2 parts: text and title
        if len(parts) == 2:
            textformb, titleformb = parts
            message(textformb, titleformb)
        else:
            print("Error: message needs 2 arguments!")

    elif command == "flip_mouse":
        flip_mouse()

    elif command == "type_spam":
        type_spam(args)

    elif command == "say":
        say(args)

    elif command == "flashbang":
        flash()

    elif command == "fake_error":
        fake_error()

    elif command == "jumpscare":
        jumpscare()

    elif command == "toggle_caps":
        toggle_caps()

    elif command == "text_explode":
        text_explode(args)

    elif command == "error_spam":
        error_spam()

    elif command == "error_sound":
        errorsound()

    else:
        print(f"Unknown command: {command}")
