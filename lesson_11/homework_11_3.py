import logging
import xml.etree.ElementTree as ET

# Logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_incoming_value(xml_file: str, group_number: int):
    """
    Searches for a <group> element with the given <number>
    and returns the value <timingExbytes>/<incoming>.
    """
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for group in root.findall("group"):
            number_tag = group.find("number")
            if number_tag is not None and number_tag.text == str(group_number):
                incoming_tag = group.find("timingExbytes/incoming")
                if incoming_tag is not None and incoming_tag.text:
                    logging.info(f"Group {group_number}: incoming = {incoming_tag.text}")
                    return incoming_tag.text
                else:
                    logging.info(f"Group {group_number}: the <incoming> element is missing")
                    return None

        logging.info(f"Group с number={group_number} not found.")
        return None

    except ET.ParseError as e:
        logging.error(f"Error parsing XML: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    xml_path = "groups.xml"
    group_num = 2
    get_incoming_value(xml_path, group_num)

