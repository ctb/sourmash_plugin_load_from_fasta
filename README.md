# sourmash_plugin_load_from_fasta

**This is an experimental plugin. Do not use for real work :).**

This is a sourmash plugin that will directly load a FASTA/FASTQ file as a
sketch. It does so in a "lazy" manner: the file is not sketched until
a specific ksize/moltype/scaled is requested.

For example, the following command is run directly on FASTA files!
```
% sourmash search examples/{47,63}.head.fa

select query k=31 automatically.
loaded query: NC_009665.1 Shewanella baltica... (k=31, DNA)
Returning ScreedFileIndex.head.fa'...
creating ScreedFileIndex('examples/63.head.fa')
--
loaded 1 total signatures from 1 locations.
after selecting signatures compatible with search, 1 remain.

1 matches above threshold 0.080:
similarity   match
----------   -----
 29.6%       NC_011663.1 Shewanella baltica OS223, complete genome
```

This means that you can immediately do comparisons with any k-mer
size, moltype, scaled, etc.

In exchange, the file is sketched each time.

Amusingly, this also lets you replace `sourmash sketch` calls with
`sig cat`:
```
sourmash sig cat examples/47.head.fa -k 12 -o 47.head.zip
```

(There's no real immediate purpose to this other than to explore the concept!)

## Installation

```
pip install sourmash_plugin_load_from_fasta
```

## Usage

More info goes here :).

## Support

We suggest filing issues in [the main sourmash issue tracker](https://github.com/dib-lab/sourmash/issues) as that receives more attention!

## Dev docs

`sourmash_plugin_load_from_fasta` is developed at
https://github.com/ctb/sourmash_plugin_load_from_fasta

### Generating a release

Bump version number in `pyproject.toml` and push.

Make a new release on github.

Then pull, and:

```
python -m build
```

followed by `twine upload dist/...`.
