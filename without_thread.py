
def increment_counter(counter) -> int:
    for _ in range(10):
        counter += 1
        

if __name__ == "__main__":
    counter = 0
    increment_counter(counter)
    increment_counter(counter)
