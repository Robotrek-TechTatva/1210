import csv

filename = "/home/hk/Qualifiers/Question3_Competetive_Programming/traingles.csv"


def areaOfT(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    T = 0
    # no of triangles inside
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]} {row[1]}  {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}. ')

            A = areaOfT(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]))
            Asub1 = areaOfT(int(row[1]), int(row[2]), int(row[3]), int(row[4]), 0, 0)
            Asub2 = areaOfT(int(row[1]), int(row[2]), 0, 0, int(row[5]), int(row[6]))
            Asub3 = areaOfT(0, 0, int(row[3]), int(row[4]), int(row[5]), int(row[6]))

            if (A == Asub1 + Asub2 + Asub3):
                T += 1
                print("inside")
            else:
                print("outside")

            line_count += 1


    print("\nValue of T is\n")
    print(T)
