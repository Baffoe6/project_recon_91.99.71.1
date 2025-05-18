from lxml import etree
import sys

def convert_xml_to_html(xml_file, xsl_file):
    try:
        dom = etree.parse(xml_file)
        xslt = etree.parse(xsl_file)
        transform = etree.XSLT(xslt)
        newdom = transform(dom)

        with open("nmap_report.html", "wb") as f:
            f.write(etree.tostring(newdom, pretty_print=True, method="html"))

        print("✔️ HTML report generated: nmap_report.html")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python nmap_xml_to_html.py <xml_file> <xsl_file>")
    else:
        convert_xml_to_html(sys.argv[1], sys.argv[2])
