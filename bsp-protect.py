# script by GAMMACASE

import sys
import os
import struct


def main(args):
	if not os.path.exists(args[0]):
		print("File doesn't exist!")
		return

	offs = [(0, 0)]

	print("Stripping entity lump...")

	with open(args[0], "rb") as file:
		file.seek(8, os.SEEK_SET)

		curr_offs = 8

		while len([x for x in offs if curr_offs + 4 in x]) == 0:
			curr_offs = file.tell()
			offs.append((struct.unpack("<i", file.read(4))[0], struct.unpack("<i", file.read(4))[0]))
			file.seek(8, os.SEEK_CUR)

		offs.pop(0)

		file.seek(0, os.SEEK_SET)
		filepart = [file.read(offs[0][0]), file.read(offs[0][1]), file.read()]

	#for i, off in enumerate(offs[1:]):
	#	if off[0] > offs[0][0]:
	#		changed_offs = struct.pack("<i", off[0] - offs[0][1] + 1)
	#		filepart[0] = filepart[0][:24 + i * 16] + changed_offs + filepart[0][28 + i * 16:]

	filepart[0] = filepart[0][:12] + struct.pack("<i", 1) + filepart[0][16:]

	with open(args[0] + ".noents", "wb") as out:
		out.write(filepart[0])
		out.write(b'\x00' * offs[0][1])
		out.write(filepart[2])

	print("Entity lump was stripped successfully!")
	input("Press enter to exit....")


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: protect.py <bspfile>");
	else:
		main(sys.argv[1:])
