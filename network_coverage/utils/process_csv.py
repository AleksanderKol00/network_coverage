import csv

from utils.static import operators


def process_csv_fn(in_file_path: str, out_file_path: str):
    """
    Add provider name by code and add GPS cordinates by Lambert93.
    :return:
    """
    with open(in_file_path, mode="r") as file_in, open(out_file_path, "w") as file_out:
        reader = csv.reader(file_in, delimiter=";")
        csv_writer = csv.writer(file_out, delimiter=";")
        row_number = 0
        for row in reader:
            if row_number == 0:
                row.append("Operator")
            elif row_number >= 1:
                if row[0] in operators:
                    row.append(operators[row[0]])
                else:
                    raise RuntimeError
            csv_writer.writerow(row)
            row_number += 1


if __name__ == "__main__":
    in_file_path = ""
    out_file_path = ""
    process_csv_fn(in_file_path, out_file_path)
