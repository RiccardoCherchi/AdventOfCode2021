def main():
  numbers = []
  boards = []

  with open("_data.txt", "r") as f:
    data = f.read().split("\n")
    numbers = data[0].strip().split(",")
    boards = data[2:]

  def part1():
    for number in numbers:
      for board in boards:
        pass

  part1()

if __name__ == "__main__":
  main()