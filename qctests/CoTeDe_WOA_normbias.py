from cotede_qc.cotede_test import get_qc

def test(p, parameters):
    '''Run the WOA normbias QC from the CoTeDe config.'''

    config   = 'cotede'
    testname = 'woa_normbias'

    return get_qc(p, config, testname)


