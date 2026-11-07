file = open("bucket_list.txt", "w")
file.write("1. visit Japan\n")
file.write("2. learn to play the guitar\n")
file.write("3. attend a live concert\n")
file.close()
print("Bucket list has been saved to bucket_list.txt")


file = open("bucket_list.txt", "r")
content = file.read()
print("\n=== My Bucket List ===")
print(content)
file.close()   



file = open("bucket_list.txt", "r")
lines = file.readlines()   
print(f"You have {len(lines)} items on your bucket list.")
file.close()



file = open("bucket_list.txt", "a")
file.write("4. go skydiving\n")
file.write("5. write a book\n")
file.close()
print("\n2 more items added ")



file = open("bucket_list.txt", "r")
all_lines = file.readlines()
file.close()
print(all_lines)


file = open("bucket_list.txt", "r")
print("\n=== Updated Bucket List ===")
print(file.read())
file.close()
