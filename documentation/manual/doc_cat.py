import os


def concatenate_files(directory_path, output_file_name):
    with open(output_file_name, 'w') as outfile:
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt") and filename != output_file_name:
                # split the filename and drop '.txt' extension
                module_name = os.path.splitext(filename)[0]

                outfile.write(f"Here's the '{module_name}' module:" + '\n\n')
                with open(os.path.join(directory_path, filename)) as infile:
                    for line in infile:
                        outfile.write(line)
                    outfile.write('\n\n')


concatenate_files(os.getcwd(), 'combined.txt')
