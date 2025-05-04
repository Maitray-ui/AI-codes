def chatbot():
    print("PizzaBot: Hi! Welcome to PizzaHub. How can I help you?")
    while True:
        user_input = input("You: ").lower()

        if "menu" in user_input:
            print("PizzaBot: We have Margherita, Pepperoni, and Veggie Supreme.")
        elif "order" in user_input:
            print("PizzaBot: Great! What pizza would you like to order?")
        elif "margherita" in user_input or "pepperoni" in user_input or "veggie" in user_input:
            print("PizzaBot: Awesome choice! Your order has been placed. 🍕")
        elif "bye" in user_input or "exit" in user_input:
            print("PizzaBot: Thanks for visiting! Have a cheesy day! 👋")
            break
        else:
            print("PizzaBot: Sorry, I didn't get that. Can you rephrase?")

chatbot()
