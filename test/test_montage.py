import os
import numpy as np

from nose.plugins.attrib import attr
from numpy.testing.decorators import skipif
from nose.tools import ok_, eq_, raises, assert_raises

import nimsdata
import nimsdata.tempdir as tempfile

# data is stored separately in nimsdata_testdata
# located at the top level of the testing directory
DATADIR = os.path.join(os.path.dirname(__file__), 'nimsdata_testdata')
if not os.path.isdir(DATADIR):
    DATADIR = None


class Test_NIMSMontage(object):

    @skipif(not DATADIR)
    def setUp(self):
        self.ds = nimsdata.parse(os.path.join(DATADIR, 'ge_dcm_mr_localizer.tgz'), load_data=True)

    @skipif(not DATADIR)
    def test001_write_png(self):
        """flat png montage"""
        with tempfile.TemporaryDirectory() as tempdir:
            outbase = os.path.join(tempdir, 'trashme')
            ok_(nimsdata.write(self.ds, self.ds.data, outbase=outbase, filetype='montage', mtype='png'))

    @skipif(not DATADIR)
    def test002_write_dir(self):
        """directory jpeg montage"""
        with tempfile.TemporaryDirectory() as tempdir:
            outbase = os.path.join(tempdir, 'trashme')
            ok_(nimsdata.write(self.ds, self.ds.data, outbase=outbase, filetype='montage', mtype='dir'))

    @skipif(not DATADIR)
    def test003_write_pyrdb(self):
        with tempfile.TemporaryDirectory() as tempdir:
            outbase = os.path.join(tempdir, 'trashme')
            ok_(nimsdata.write(self.ds, self.ds.data, outbase=outbase, filetype='montage', mtype='sqlite'))

    @skipif(not DATADIR)
    def test004_get_size(self):
        with tempfile.TemporaryDirectory() as tempdir:
            outbase = os.path.join(tempdir, 'trashme')
            nimsdata.write(self.ds, self.ds.data, outbase=outbase, filetype='montage')
            outfile = os.path.join(tempdir, os.listdir(tempdir)[0])
            ok_(nimsdata.medimg.nimsmontage.get_info(outfile))              # gets made?

    @skipif(not DATADIR)
    def test005_get_tile(self):
        with tempfile.TemporaryDirectory() as tempdir:
            outbase = os.path.join(tempdir, 'trashme')
            nimsdata.write(self.ds, self.ds.data, outbase=outbase, filetype='montage')
            outfile = os.path.join(tempdir, os.listdir(tempdir)[0])
            ok_(nimsdata.medimg.nimsmontage.get_tile(outfile, 0, 0, 0))     # all montage have 0, 0, 0
