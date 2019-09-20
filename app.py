from fitz import Document
from html import unescape
from bs4 import BeautifulSoup
import argparse


def write_to_file(elements, output_file):
    for element in elements:
        if element == "":
            continue
        output_file.write(element + ", ")


def merge_results(pages_list):
    for i in range(len(pages_list) - 1):
        if pages_list[i].rstrip("n") == pages_list[i+1].rstrip("n"):
            pages_list[i] = pages_list[i].strip("n") + " e n"
            pages_list[i+1] = ""
    return pages_list


def results_cleaner(results_file):
    with open(results_file, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip(", \n")
    lines.sort()
    with open(results_file, "w") as file:
        for line in lines:
            file.write(line + "\n")
        file.truncate()


parser = argparse.ArgumentParser()
parser.add_argument("pdf_file", help="The PDF file to parse", nargs=1, type=str)
parser.add_argument("names", help="The names file", nargs=1, type=str)
parser.add_argument("output", help="The output file", nargs=1, type=str)
parser.add_argument("font_size", help="The body font size", nargs=1, type=int)
parser.add_argument("--delta", "-d", help="Page delta", nargs=1, type=int)
parser.add_argument("--start", "-s", help="Starting page", nargs=1, type=int)
parser.add_argument("--end", "-e", help="Ending page", nargs=1, type=int)
args = parser.parse_args()
end = None
if args.delta:
    page_delta = args.delta[0] + 1
else:
    page_delta = 1
if args.start:
    start = args.start[0]
else:
    start = 0
if args.end:
    end = args.end[0]
results_file = args.output[0]
font_standard = args.font_size[0]
pdf_file = args.pdf_file[0]
names_file = args.names[0]
with open(names_file, "r") as file:
    names_list = tuple(map(lambda x: str(x).strip("\n"), file.readlines()))
doc = Document(pdf_file)
if end is None:
    end = len(doc)
results = open(results_file, "a")
for name in names_list:
    print(f"Parsing: {name}")
    word_in_pages = []
    results.write(f"{name} ")
    for page in range(start, end):
        lines = unescape(doc[page].getText("html")).split("\n")
        for line in lines:
            item = line.replace("\t", " ")
            bs = BeautifulSoup(item, "html.parser")
            if bs.p is not None:
                if name.title() in str(bs.p.text) and str(
                        bs.p["style"]).find("top:84pt") == -1:
                    font_index = str(bs.p.span["style"]).find("font-size")
                    font_size = str(bs.p.span["style"][font_index:]
                                    ).lstrip("font-size:")[:2
                                ].rstrip("p").rstrip(".")
                    string_to_write = str(page + page_delta)
                    if int(font_size) < font_standard:
                        string_to_write += "n"
                    if string_to_write in word_in_pages:
                        continue
                    else:
                        print("\t'{}' found in page {}".format(name, page))
                        word_in_pages.append(string_to_write)
                    string_to_write = ""
    merged_pages = merge_results(word_in_pages)
    write_to_file(merged_pages, results)
    results.write("\n")
results.close()
doc.close()
results_cleaner(results_file)
