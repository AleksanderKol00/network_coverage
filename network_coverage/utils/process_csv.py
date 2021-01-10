import csv

from utils.static import operators
from utils.tools import gps_cord_from_Lambert93


def process_csv_fn(in_file_path: str, out_file_path: str):
    """
    Add provider name by code.
    :return:
    """
    with open(in_file_path, mode="r", encoding="utf-8") as file_in, open(
        out_file_path, "w", encoding="utf-8"
    ) as file_out:
        reader = csv.reader(file_in, delimiter=";")
        csv_writer = csv.writer(file_out, delimiter=",")
        row_number = 0
        for row in reader:
            if row_number % 100 == 0:
                print(f"ROW NUMBER: {row_number}\n")
            elif row_number == 0:
                row.append("Operator")
                row.append("lat")
                row.append("lot")
            elif row_number >= 1:
                if row[0] in operators:
                    row.append(operators[row[0]])
                    cords = gps_cord_from_Lambert93(x=int(row[1]), y=int(row[2]))
                    row.append(str(cords.latitude))
                    row.append(str(cords.longitude))
                else:
                    raise RuntimeError(f"Can't find operator: {row[0]} in saved operators.")
            csv_writer.writerow(row)
            row_number += 1


if __name__ == "__main__":
    in_file_path = ""
    out_file_path = ""

    process_csv_fn(in_file_path, out_file_path)
