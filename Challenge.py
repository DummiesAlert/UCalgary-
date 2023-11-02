# 1
# def draw_diamonds():
#     num_diamonds = int(input("Enter the number of diamonds you want to draw: "))
#     edge_lengths = input("Enter the edge lengths of each diamond (separated by spaces): ").split()

#     for length in edge_lengths:
#         length = int(length)
#         diamond = ""

#         # Draw the diamond
#         for i in range(length):
#             diamond += " " * (length - i - 1) + "*" * (2 * i + 1) + "\n"

#         print(diamond)

# draw_diamonds()
#2
# def draw_diamond(height):
#     for i in range(1, height + 1, 2):
#         spaces = (height - i) // 2
#         print(" " * spaces + "* " * (i // 2) + "*")
#     for i in range(height - 2, 0, -2):
#         spaces = (height - i) // 2
#         print(" " * spaces + "* " * (i // 2) + "*")

# def main():
#     num_diamonds = int(input("Enter the number of diamonds: "))

#     for _ in range(num_diamonds):
#         print("Enter the edge lengths for the diamond (choose from 3, 5, or 7):")
#         while True:
#             edge_length = int(input())
#             if edge_length in [3, 5, 7]:
#                 break
#             else:
#                 print("Please choose from 3, 5, or 7.")
#         draw_diamond(edge_length)

# if __name__ == "__main__":
#     main()

#3 

def draw_diamond(height):
    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "* " * (i // 2) + "*")
    for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "* " * (i // 2) + "*")

def main():
    num_diamonds = int(input("Enter the number of diamonds: "))

    for _ in range(num_diamonds):
        edge_length = int(input("Enter the edge length for the diamond: "))
        draw_diamond(edge_length)

if __name__ == "__main__":
    main()

