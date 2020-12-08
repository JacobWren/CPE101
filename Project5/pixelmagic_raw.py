# Name:         Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Pixel Magic!
# Term:         Winter 2020

import sys
from typing import List


def main(argv: List[str]) -> None:
   if len(argv) < 3: print('Usage: python3 pixelmagic.py <mode> <image>')
   if len(argv) < 3: return
   file_name = argv[2]
   try:
       open(file_name, "r")
   except FileNotFoundError:
       print('Error: Unable to open', file_name)
       return
   mode, data = argv[1], read_pixels(file_name)
   width = int(data[1].split(' ')[0])
   main_small(argv)
   if mode == 'fade':
       try:
           fade(argv[2], mode, data, argv[3], argv[4], argv[5], width)
       except IndexError: print('Usage: python3 pixelmagic.py fade <image> <row> <col> <radius>')
       except FileNotFoundError: print('Error: Unable to open {argv[1]}.ppm')
   if argv[1] == 'turn':
        temp = main_small_2(argv)
        if temp == None:
            return
   if argv[1] == 'flip':
        temp1 = main_small_3(argv)
        if temp1 == None:
            return
   if argv[1] == 'gray':
        temp2 = main_small_4(argv)
        if temp2 == None: return
   if argv[1] == 'blur':
       temp3 = main_small_5(argv)
       if temp3 == None: return


def main_small_2(argv: List[str]) -> None:
   if argv[1] == 'turn':
       if len(argv) == 3:
           print('Usage: python3 pixelmagic.py turn <image> <degree>')
       elif float(argv[3]) % 90 != 0:
            print('Error: Turn must be in 90 degree increments')

           #return
       else:
           try:
               file_name = argv[2]
               mode = argv[1]
               data = read_pixels(file_name)
               width = int(data[1].split(' ')[0])
               height = int(data[1].split(' ')[1])
               turn(argv[2], mode, data, argv[3], width, height)
           except FileNotFoundError:
               print('Error: Unable to open {argv[1]}.ppm')


def main_small(argv: List[str]) -> None:
   file_name = argv[2]
   mode = argv[1]
   data = read_pixels(file_name)
   if argv[1] != 'gray' and argv[1] != 'fade' and \
           argv[1] != 'flip' and argv[1] != 'turn' and argv[1] != 'blur':
       print('Error: Invalid mode')
       #return


def main_small_4(argv: List[str]) -> None:
   file_name = argv[2]
   mode = argv[1]
   data = read_pixels(file_name)
   if argv[1] == 'gray':
       try:
           gray(argv[2], mode, data)
       except FileNotFoundError:
           print('Unable to open {argv[1]}.ppm')


def main_small_3(argv: List[str]) -> None:
   file_name = argv[2]
   mode = argv[1]
   data = read_pixels(file_name)
   if argv[1] == 'flip':
       try:
           flip(argv[2], mode, data)
       except FileNotFoundError:
           print('Error: Unable to open {argv[1]}.ppm')


def main_small_5(argv: List[str]) -> None:
   file_name = argv[2]
   mode = argv[1]
   data = read_pixels(file_name)
   width = int(data[1].split(' ')[0] )
   height = int(data[1].split(' ')[1] )
   if argv[1] == 'blur':
       try:
           blur(argv[2], mode, data, width, height, int(argv[3]))
       except FileNotFoundError:
           print('Error: Unable to open {argv[1]}.ppm')


def read_pixels(file_name):
   inf = open(file_name, "r")
   line = inf.readlines()
   line = [i.replace('\n', '') for i in line]  # remove '\n'
   line = [line[i] for i in range(0, len(line))]
   return line
   inf.close()

'''
def header(file_name):
   l = data
   outf = open(file_name, "w")
   outf.write(l[0] + '\n')
   outf.write(l[1] + '\n')
   outf.write(l[2] + '\n')
   outf.close()
'''

def gray(file_name, mode, data):
   l = data
   x = open(mode + ".ppm", "w")
   x.write(l[0] + '\n')
   x.write(l[1] + '\n')
   x.write(l[2] + '\n')
   l = l[3:]
   for j in l:
       m = j.split()
       s = 0
       for d in m:
           d = int(d)
           s = d + s
       avg = s // 3
       res = str(avg)
       x.write(res + ' ' + res + ' ' + res + '\n')
   x.close()


def fade(file_name, mode, data, y_val, x_val, radius, width):
   l = data
   x = open(mode + ".ppm", "w")
   x.write(l[0] + '\n')
   x.write(l[1] + '\n')
   x.write(l[2] + '\n')
   l = l[3:]
   for i in range(len(l)):
       y_pix, x_pix  = i // width, i % width
       y_dist, x_dist = abs(y_pix - int(y_val)), abs(x_pix - int(x_val))
       cent_dist = ((y_dist ** 2) + (x_dist ** 2)) ** (1 / 2)
       scale_factor = (int(radius) - cent_dist) / int(radius)
       if scale_factor < .2:
           scale_factor = .2
       m, res = l[i].split(), ''
       for d in m:
           d = int(int(d) * scale_factor)
           res = res + ' ' + str(d)
       x.write(res.lstrip() + '\n')
   x.close()


def flip(file_name, mode, data):
   l = data
   x = open(mode + ".ppm", "w")
   x.write(l[0] + '\n')
   x.write(l[1] + '\n')
   x.write(l[2] + '\n')
   width = int(data[1].split(' ')[0] ) - 1
   width_fixed = int(data[1].split(' ')[0] ) - 1
   end = -1
   height = int(data[1].split(' ')[1] )
   l = l[3:]
   for k in range(height):
       for j in range(width, end, -1):
           row = j // width
           x.write(l[j] + '\n')
       width = width + width_fixed + 1
       end = width - width_fixed - 1
   x.close


def turn(file_name, mode, data, degree, width, height):
   l, x = data, open(mode + ".ppm", "w")
   if int(int(degree) // 90) % 2 == 0:
       x.write(l[0] + '\n'), x.write(l[1] + '\n'), x.write(l[2] + '\n')
   else:
       x.write(l[0] + '\n'), x.write(str(height) + ' ' + str(width) + '\n')
       x.write(l[2] + '\n')
   l = l[3:]
   for i in range(int(degree) // 90):
       a = []
       if i != 0:
           width, height = height, width
       start = (width * height) - width
       for k in range(width):
           for j in range(start, k - 1, -width):
               if i == ((int(degree) // 90) - 1):
                   x.write(l[j] + '\n')
               a.append(l[j])
           start = start + 1
       l = a.copy()
   x.close()


def blur(file_name, mode, data, width, height, reach = 4):
   l, x = data, open(mode + ".ppm", "w")
   x.write(l[0] + '\n'), x.write(l[1] + '\n'), x.write(l[2] + '\n')
   l = l[3:]
   for k in range(height):  # height
       row_min = max(0, k - int(reach))
       row_max = min(height - 1, k + int(reach))
       for j in range(width):  # width
           w, col_max = max(0, j - int(reach)), min(width - 1, j + int(reach))
           r, span_col, a = abs(row_max - row_min), abs(col_max - w), ''
           for p in range(3):
               d, s = (row_min, w), 0
               beg, end = d[1], d[1] + span_col + 1
               for m in range(d[0], d[0] + r + 1):
                   for i in range(beg, end):
                       s = s + int(l[int((m * width) + i)].split()[p])
               if p != 0:
                   a = a + ' ' + str(s // int( (r + 1) * (span_col + 1)))
                   #x.write(' ' + str(s // int((r + 1) * (span_col + 1))))
               else:
                   a = a + str(s // int( (r + 1) * (span_col + 1)))
                   #x.write(str(s // int((r + 1) * (span_col + 1))))
           x.write(a + '\n')
           #x.write('\n')


if __name__ == "__main__":
   main(sys.argv)
