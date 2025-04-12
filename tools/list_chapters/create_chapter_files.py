#!/usr/bin/env python3

import os

def create_chapter_files():
    # Read the chapter list
    with open('chapter_list.txt', 'r', encoding='utf-8') as f:
        chapters = f.readlines()
    
    # Create a file for each chapter
    for chapter in chapters:
        chapter = chapter.strip()
        if not chapter:  # Skip empty lines
            continue
        
        # Create filename from chapter info
        filename = f"{chapter}.txt"
        
        # Create the file
        with open(filename, 'w', encoding='utf-8') as f:
            # Optionally add a title/header to the file
            f.write(f"# {chapter}\n\n")
        
        print(f"Created: {filename}")

if __name__ == "__main__":
    create_chapter_files()
    print("All chapter files have been created successfully!") 