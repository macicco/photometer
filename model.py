from __future__ import print_function, division
import traitlets

class SourceDetection(traitlets.HasTraits):
    """
    Model for (automatic) source detection.
    """
    
    def __init__(self):
        self._ccd = None
        self._fwhm = None
        self._sigma = None
        self._iters = None
        self._threshold = None

class AperturePhotometry(traitlets.HasTraits):
    """
    Model that links to the GUI to perform the aperture
    photometry on a given set of sources.
    """

    aperture_radius = traitlets.Float()
    annulus_inner_radius = traitlets.Float()
    annulus_outer_radius = traitlets.Float()
    aperture_net_counts = traitlets.Float()
    reject_outlying_pix = traitlets.Bool()
    execute = traitlets.Bool()

    '''
    snr = traitlets.Float()
    typical_sky_pix = traitlets.Integer()
    centroid_ra_dec = traitlets.Integer()
    centroid_pix_coords = traitlets.Integer()
    fwhm = ?
    '''

    def __init__(self):
        #super(AperturePhotometry, self).__init__(description='Photometry model')
        self._ccd_image = None
        self._sources = None
        self._gain = None
        self._N_R = None
        self._N_dark_pp = None
        
    #@traitlets.observe('aperture_radius', 
                       #'annulus_inner_radius', 
                       #'annulus_outer_radius')
    def perform_photometry(self, b):
        print("Function ran!")

    def calc_typical_sky_pix(self):
        pass
