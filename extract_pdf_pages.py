from pathlib import Path
import pymupdf

PDF_PATH = Path(
    r"C:\Users\user\Desktop\data collection v2\data-collection"
    r"\pdfcoffee.com_a-bron-r-tripathi-b-tripathi-wolffx27s-anatomy-of-the-eye-and-orbit-crc-press-1998-pdf-pdf-free.pdf"
)

OUTPUT_PATH = Path("extracted_pages.txt")

PRINTED_PAGES = list(range(303, 371))
#PRINTED_PAGES = [443, 563 ]

# Based on the pages we checked so far.
# Verify this mapping at printed page 525 before relying on it.
PDF_OFFSET = 10


def main():
    if not PDF_PATH.exists():
        print(f"PDF not found: {PDF_PATH}")
        return

    extracted_sections = []

    with pymupdf.open(PDF_PATH) as pdf:
        for printed_page in PRINTED_PAGES:
            pdf_page_number = printed_page + PDF_OFFSET

            if not 1 <= pdf_page_number <= len(pdf):
                print(f"PDF page out of range: {pdf_page_number}")
                continue

            page = pdf[pdf_page_number - 1]
            page_text = page.get_text("text").strip()

            extracted_sections.append(
                f"\n{'=' * 50}\n"
                f"PRINTED PAGE: {printed_page}\n"
                f"PDF PAGE: {pdf_page_number}\n"
                f"{'=' * 50}\n"
                f"{page_text}\n"
            )

            print(
                f"Extracted printed page {printed_page} "
                f"(PDF page {pdf_page_number})"
            )

    OUTPUT_PATH.write_text(
        "\n".join(extracted_sections),
        encoding="utf-8"
    )

    print(f"\nSaved output to: {OUTPUT_PATH.resolve()}")


if __name__ == "__main__":
    main()
