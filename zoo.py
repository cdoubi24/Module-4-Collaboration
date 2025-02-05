# zoo.py

def hours():
    print("Open 9-5 daily")

# Test the function within the same script
if __name__ == "__main__":
    import zoo  # Normal import
    zoo.hours()

    import zoo as menagerie  # Import with alias
    menagerie.hours()
