import argparse
from PyPDF2 import PdfFileMerger


def merge_pdfs(base, appended, outname):
    pdfs = [base, appended]
    merger = PdfFileMerger(strict=False)
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(outname)
    merger.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('f1', help='path to base document', type=str)
    parser.add_argument('f2', help='path to the document to append', type=str)
    parser.add_argument('outname', help='filename of final document', type=str)
    args = parser.parse_args()
    merge_pdfs(args.f1, args.f2, args.outname)
