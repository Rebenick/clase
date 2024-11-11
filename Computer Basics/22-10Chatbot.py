def chatbot():
    try:
        name = input("What's your name? ")
        if not name.strip():
            raise ValueError("The name cannot be empty")
        
        birth_date = input("What is your birthdate? (DD/MM/YYYY) ")
        if not birth_date.strip():
            raise ValueError("The birth date cannot be empty")

        hobbies = input("What are your hobbies?")
        if not hobbies.strip():
            raise ValueError("Hobbies cannot be empty.")
        
        print(f"Hi, {name}!")
        print(f"You were born on {birth_date}.")
        print(f"Your hobbies are: {hobbies}.")

    except ValueError as error:
        print(f"Error: {error}")

chatbot()
