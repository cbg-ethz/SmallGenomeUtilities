from sys import version_info, exit
from os import path
from setuptools import setup

# Will never support Py2
if version_info[0] == 2:
	exit("Sorry, Python 2 is not supported")

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name = "SmallGenomeUtilities",
	version = "0.0.1",
	author = "David Seifert",
	author_email = "david.seifert@bsse.ethz.ch",
	description = ("A collection of scripts that are useful for dealing with viral RNA NGS data."),
	license = "GPL2+",
	keywords = "NGS SAM BAM HIV-1 alignment",
	url = "https://github.com/SoapZA/SmallGenomeUtilities",
	packages=["SmallGenomeUtilities"],
	scripts=[
		"scripts/convert_qr",
		"scripts/convert_reference",
		"scripts/coverage_stats",
		"scripts/extract_sam",
		"scripts/extract_seq",
		"scripts/mapper",
		"scripts/pair_sequences",
		"scripts/remove_gaps_msa",
	],
	install_requires=[
		"biopython",
		"progress",
		"pysam",
	],
	long_description=long_description,
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Topic :: Scientific/Engineering :: Bio-Informatics",
		"Topic :: Utilities",
		"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
	]
)
