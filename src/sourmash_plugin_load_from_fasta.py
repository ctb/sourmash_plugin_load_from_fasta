"""xyz plugin description"""

import argparse
import sourmash

import screed
from sourmash.index import Index
from sourmash.logging import debug_literal
from sourmash.plugins import CommandLinePlugin
from sourmash.command_compute import ComputeParameters
from sourmash.signature import SourmashSignature

from sourmash.save_load import (Base_SaveSignaturesToLocation,
                                _get_signatures_from_rust)


###

#
# load_from plugin
#

def lazy_load_screed(location, *args, **kwargs):
    success = False
    try:
        with screed.open(location) as it:
            _ = next(iter(it))

            print('Returning ScreedFileIndex')
            return ScreedFileIndex(location)
            
    except:
        raise

lazy_load_screed.priority = 90

class ScreedFileIndex(Index):
    def __init__(self, filename):
        print(f"creating ScreedFileIndex('{filename}')")
        self.filename = filename

    def __len__(self):
        return 1

    @property
    def location(self):
        return self.filename

    def select(self, ksize=None, moltype=None, scaled=None, num=None,
               abund=None, containment=None):
        # actually do the sketching!

        if not ksize:
            ksize = 31
        if not moltype:
            moltype = 'DNA'
        if not scaled:
            assert not num
            scaled = 1000
            containment = True  # probably unnecessary?

        if abund is None:
            abund = True

        params = ComputeParameters(ksizes=[ksize],
                                   dna=True,
                                   scaled=scaled,
                                   num_hashes=0,
                                   protein=False,
                                   dayhoff=False,
                                   hp=False,
                                   track_abundance=abund)

        sig = SourmashSignature.from_params(params)
        
        with screed.open(self.filename) as fp:
            for record in fp:
                sig.add_sequence(record.sequence, force=True)

        self.sig = sig
        return self

    def insert(self, *args):
        raise NotImplementedError

    def load(self, *args):
        raise NotImplementedError

    def save(self, *args):
        raise NotImplementedError

    def signatures(self):
        return [self.sig]
    

