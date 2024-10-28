# -*- coding: utf-8 -*-
import sys
import io
import os
from collections import Counter

# Fetch command history
os.system("history >> hist.txt")
# Ensure the script outputs in UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def draw_unicode_table(data):
    # Determine the maximum width for each column
    max_col_widths = [max(len(str(item))
                          for item in col) + 2 for col in zip(*data)]

    # Define horizontal line components based on column widths
    top_line = "╭" + "┬".join("─" * width for width in max_col_widths) + "╮"
    middle_line = "├" + "┼".join("─" * width for width in max_col_widths) + "┤"
    bottom_line = "╰" + "┴".join("─" * width for width in max_col_widths) + "╯"

    # Start with the top line of the table
    table_lines = [top_line]

    # Add each row of data with appropriate padding
    for i, row in enumerate(data):
        row_line = "│" + "│".join(str(item).center(width)
                                  for item, width in zip(row, max_col_widths)) + "│"
        table_lines.append(row_line)

        # Add the middle line after each row, except the last
        if i < len(data) - 1:
            table_lines.append(middle_line)

    # End with the bottom line of the table
    table_lines.append(bottom_line)

    # Join all lines into a single string
    return "\n".join(table_lines)


def get_command_history(file_path):
    # Read the history file line by line
    with open(file_path, 'r') as file:
        history_lines = file.readlines()
    return history_lines


def count_commands(history_lines):
    # Extract only the second column (the command name)
    commands = [line.split()[1]
                for line in history_lines if len(line.split()) > 1]
    command_counts = Counter(commands)
    return command_counts.most_common(10)


def main():
    file_path = "hist.txt"  # Path to your history file

    history_lines = get_command_history(file_path)
    top_commands = count_commands(history_lines)

    data = [
        ["Command", "Count"],
        *[[command, count] for command, count in top_commands]
    ]

    # Print the top 10 most used commands in the specified format
    print("Top 10 most used commands:")
    
    print(draw_unicode_table(data))


if __name__ == "__main__":
    main()
