#!/usr/bin/env python3
# Take directory that contains all scripts
# Format and convert them into singular txt file
# Convert it into pdf

import datetime, os
from ModuleImporter import module_importer
fpdf = module_importer('fpdf', 'fpdf2')
from fpdf import FPDF

HEADER = '''
Netaji Subhash Engineering College
Department of Computer Science & Engineering
B. Tech CSE 2nd Year 3rd Semester
2021-2022
________________________________________________________________________________
Name of the Course: IT Workshop
Course Code: PCC-CS393
Name of the Student: %(name)s
Class Roll No.: 119
University Roll No: %(univ_roll)s
Date of Experiment: %(date)s
Date of Submission: %(date)s
________________________________________________________________________________
# Assignment No.: %(assign_num)d

'''

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 10)
        self.set_text_color(169, 169, 169)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 
                          align = 'C')

def createPdf(txtPath: str, fontpath: str, name: str) -> str:
    pdfPath = os.path.join(os.path.dirname(txtPath), os.path.basename(txtPath).replace('.txt', '.pdf'))
    pdf = PDF('P', 'mm', 'A4')
    pdf.add_font('CustomFont', '', fontpath, uni=True)
    pdf.alias_nb_pages()
    pdf.add_page()

    pdf.set_font('CustomFont', '', 10)
    pdf.set_title('Python Assignment')
    pdf.set_author(name)
    pdf.set_text_color(10, 10, 10)
    
    with open(txtPath, 'rb') as txtFile:
        content = txtFile.read().decode('latin-1')
        pdf.multi_cell(0, 5, content, align='J')
    pdf.output(pdfPath)
    return pdfPath

def main():
    import argparse, pty, glob, string

    parser = argparse.ArgumentParser()
    parser.add_argument('script_dir', nargs='?', help='Source dir containing scripts', default=os.getcwd())
    parser.add_argument('assign_num',            help='Specify assignment number', type=int)
    parser.add_argument('-n', '--name',          help='Specify name', default='Ananyobrata Pal')
    parser.add_argument('-u', '--univ-roll',     help='Specify University Roll', default='10900120122')
    parser.add_argument('-d', '--date',          help='Specify date in assignment', 
                                                 default=datetime.datetime.now().strftime("%d/%m/%Y"))
    parser.add_argument('-k', '--keep',          help='Keep text file', action='store_true')
    args = parser.parse_args()

    dirname = os.path.normpath(os.path.abspath(args.script_dir))
    if not os.path.exists(dirname):
        raise SystemExit("Invalid directory")

    details = dict(
        name = args.name,
        univ_roll = args.univ_roll,
        assign_num = args.assign_num,
        date = args.date
    )

    assignmentTxtPath = os.path.join(dirname, f'Assignment{args.assign_num}_{args.name}.txt')
    # create a master txt file
    with open(assignmentTxtPath, 'w') as assign_file:
        # append header in the txt file
        assign_file.write(HEADER % details)
        # find the scripts in the directory, sort
        script_paths = glob.glob(os.path.join(dirname, '*.py'))
        script_paths.sort()

        # for every script
        for script_path in script_paths:
            with open(script_path) as script:
                # write problem statement as the lines starting with '#'
                assign_file.write('Problem:')
                print()
                while True:
                    line = script.readline()
                    if line.startswith('#'):
                        assign_file.write(line.lstrip('#'))
                        print(line.lstrip('#'))
                    else: break
                assign_file.write('\nCode:')
                assign_file.write(line)

                # copy the code
                for line in script:
                    assign_file.write(line)
                
            assign_file.write('Output:\n')
            tempOutFile = os.path.join('/tmp', 
                           os.path.splitext(os.path.basename(script_path))[0] + '.out')
            # spawn a pseudo-terminal and record session with linux-util 'script'
            pty.spawn(('/bin/script', tempOutFile, '-c', f'python {script_path}'))
            # add session to the master file
            testOutput = open(tempOutFile).read().splitlines()[1:-1]
            for char in '\n'.join(testOutput):
                if char in string.printable:
                    assign_file.write(char)

            os.unlink(tempOutFile)  # delete temporary file
            assign_file.write('\n________________________________________________________________________________\n\n')
    pdfOut = createPdf(assignmentTxtPath, '/usr/share/fonts/TTF/NotoSansMono-Regular-Nerd-Font-Complete.ttf',
                        args.name)
    print(f"Assignment saved successfully at {pdfOut}")
    if not args.keep:
        os.unlink(assignmentTxtPath)


if __name__ == '__main__':
    main()

